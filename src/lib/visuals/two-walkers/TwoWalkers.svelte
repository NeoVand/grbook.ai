<script lang="ts">
	import { onMount } from 'svelte';
	import * as THREE from 'three';
	import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
	import {
		DEFAULTS,
		PRESETS,
		WORLDS,
		formatLength,
		readouts,
		stretchMarks,
		tape,
		trails,
		visibleReadouts,
		walkerAt,
		type State,
		type WorldId
	} from './model.js';

	const { initial = 'football' }: { initial?: keyof typeof PRESETS } = $props();

	// The preset only seeds the demo; after that the reader owns the state.
	// svelte-ignore state_referenced_locally
	let view = $state<State>({ ...DEFAULTS, ...PRESETS[initial as string] });
	const world = $derived(WORLDS[view.world]);
	const values = $derived(readouts(view));
	const shown = $derived(visibleReadouts(view));

	// The scene is rebuilt from the model on every change; nothing about the physics lives in here.
	let canvas: HTMLCanvasElement;
	let scene: THREE.Scene;
	let camera: THREE.PerspectiveCamera;
	let renderer: THREE.WebGLRenderer;
	let controls: OrbitControls;
	let group: THREE.Group;
	let ready = $state(false);
	let playing = $state(false);

	const PALETTE = {
		blue: 0x2563eb,
		orange: 0xd97706,
		tape: 0x2c6a5c,
		surfaceLight: 0xe8eae4,
		surfaceDark: 0x3c4744,
		lineLight: 0x9aa39d,
		lineDark: 0x5c6763
	};
	const dark = () =>
		typeof document !== 'undefined' && document.documentElement.classList.contains('dark');

	/** Everything is drawn in units of the world's own size, so one camera framing works everywhere. */
	const unit = $derived(
		world.shape === 'plane' || world.shape === 'tube'
			? Math.max(world.walk, view.gap) / 2
			: world.shape === 'sphere'
				? world.radius
				: 0.35
	);

	/**
	 * A path drawn as a solid tube. WebGL ignores line widths, so a one-pixel line is invisible against a shaded
	 * surface; a tube of real radius reads as a stripe painted on the world, and the surface is pushed back a
	 * fraction (polygonOffset) so the stripe never fights it for the same pixels.
	 */
	function stripe(points: [number, number, number][], color: number, radius = 0.012) {
		const seen = points
			.map((p) => new THREE.Vector3(p[0] / unit, p[1] / unit, p[2] / unit))
			.filter((v, i, all) => i === 0 || v.distanceTo(all[i - 1]) > 1e-6);
		if (seen.length < 2) return new THREE.Group();
		const path = new THREE.CatmullRomCurve3(seen);
		return new THREE.Mesh(
			new THREE.TubeGeometry(path, Math.min(240, seen.length * 2), radius, 8, false),
			new THREE.MeshStandardMaterial({ color, roughness: 0.45, metalness: 0.05 })
		);
	}

	function marker(at: [number, number, number], color: number) {
		const dot = new THREE.Mesh(
			new THREE.SphereGeometry(0.038, 24, 16),
			new THREE.MeshStandardMaterial({ color, roughness: 0.35, metalness: 0.1 })
		);
		// Lifted a whisker along the outward normal so a walker sits on the world rather than half inside it.
		const out = new THREE.Vector3(at[0] / unit, at[1] / unit, at[2] / unit);
		const lift = world.shape === 'plane' ? new THREE.Vector3(0, 1, 0) : out.clone().normalize();
		dot.position.copy(out).addScaledVector(lift, 0.02);
		return dot;
	}

	function surface(): THREE.Object3D {
		const material = new THREE.MeshStandardMaterial({
			color: dark() ? PALETTE.surfaceDark : PALETTE.surfaceLight,
			roughness: 0.78,
			metalness: 0.02,
			side: THREE.DoubleSide,
			// Pushed a fraction away from the camera so the stripes painted on it always win the depth test.
			polygonOffset: true,
			polygonOffsetFactor: 2,
			polygonOffsetUnits: 2
		});
		const wire = new THREE.LineBasicMaterial({
			color: dark() ? PALETTE.lineDark : PALETTE.lineLight,
			transparent: true,
			opacity: dark() ? 0.45 : 0.55
		});
		const holder = new THREE.Group();
		if (world.shape === 'plane') {
			const size = (Math.max(world.walk, view.gap) * 1.4) / unit;
			const plane = new THREE.Mesh(new THREE.PlaneGeometry(size, size), material);
			plane.rotation.x = -Math.PI / 2;
			holder.add(
				plane,
				new THREE.LineSegments(
					new THREE.WireframeGeometry(new THREE.PlaneGeometry(size, size, 12, 12)),
					wire
				).rotateX(-Math.PI / 2)
			);
		} else if (world.shape === 'tube') {
			const r = world.radius / unit;
			const geometry = new THREE.CylinderGeometry(r, r, (world.walk * 1.2) / unit, 48, 1, true);
			const tube = new THREE.Mesh(geometry, material);
			tube.rotation.x = Math.PI / 2;
			holder.add(
				tube,
				new THREE.LineSegments(
					new THREE.WireframeGeometry(
						new THREE.CylinderGeometry(r, r, (world.walk * 1.2) / unit, 16, 4, true)
					),
					wire
				).rotateX(Math.PI / 2)
			);
		} else if (world.shape === 'sphere') {
			const r = world.radius / unit;
			holder.add(
				new THREE.Mesh(new THREE.SphereGeometry(r, 48, 32), material),
				new THREE.LineSegments(
					new THREE.WireframeGeometry(new THREE.SphereGeometry(r, 16, 12)),
					wire
				)
			);
		} else {
			const geometry = new THREE.TorusGeometry(0.25 / unit, 0.1 / unit, 24, 64);
			const torus = new THREE.Mesh(geometry, material);
			torus.rotation.x = Math.PI / 2;
			holder.add(
				torus,
				new THREE.LineSegments(
					new THREE.WireframeGeometry(new THREE.TorusGeometry(0.25 / unit, 0.1 / unit, 8, 24)),
					wire
				).rotateX(Math.PI / 2)
			);
		}
		return holder;
	}

	/**
	 * Points the camera at the walk rather than at the world's centre, so the two trails sit in the middle of the
	 * frame on every world. Called when the world changes and never while the reader is turning it themselves.
	 */
	function aimCamera() {
		if (!camera || !controls) return;
		const mid = walkerAt(view, world.walk / 2, view.gap / 2);
		const at = new THREE.Vector3(mid[0] / unit, mid[1] / unit, mid[2] / unit);
		if (world.shape === 'plane' || world.shape === 'tube') {
			// Flat worlds are looked at from above and to one side; the walk runs away down the -z axis.
			controls.target.set(0, 0, at.z);
			camera.position.set(1.3, 1.7, at.z + 2.0);
		} else {
			// On a ball or a ring the camera moves out along the surface's own outward direction at the halfway
			// point, so the reader faces the stretch of world the walkers cross.
			const out = at.clone().normalize();
			controls.target.set(0, 0, 0);
			camera.position
				.copy(out)
				.multiplyScalar(world.shape === 'torus' ? 2.35 : 2.9)
				.add(new THREE.Vector3(0.45, 0.1, 0.45));
		}
		controls.update();
	}

	/** Rebuilds the trails, the tape, the tick marks and the two walkers from the model. */
	function draw() {
		if (!group) return;
		group.clear();
		group.add(surface());

		const { blue, orange } = trails(view);
		group.add(stripe(blue, PALETTE.blue), stripe(orange, PALETTE.orange));
		group.add(stripe(tape(view), PALETTE.tape, 0.016));

		// Ticks across the walk, so the reader can count stretches and watch them close in.
		const walked = view.progress * world.walk;
		for (const at of stretchMarks(view)) {
			if (at > walked + 1e-9) continue;
			const across = Array.from({ length: 9 }, (_, i) => walkerAt(view, at, (view.gap * i) / 8));
			group.add(stripe(across, dark() ? 0xcdd6d1 : 0xffffff, 0.007));
		}

		group.add(marker(walkerAt(view, walked, 0), PALETTE.blue));
		group.add(
			marker(walkerAt(view, Math.max(0, walked - view.headStart), view.gap), PALETTE.orange)
		);
	}

	$effect(() => {
		// Re-read the whole view so any change redraws.
		void [view.world, view.gap, view.headStart, view.startCircle, view.stretches, view.progress];
		if (ready) draw();
	});

	onMount(() => {
		scene = new THREE.Scene();
		camera = new THREE.PerspectiveCamera(38, 1, 0.01, 100);
		camera.position.set(2.1, 1.5, 2.4);
		renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
		renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
		controls = new OrbitControls(camera, canvas);
		controls.enableDamping = true;
		controls.enablePan = false;
		// A key light and a dimmer fill from the far side, so a ball reads as a ball and not a flat disc.
		scene.add(new THREE.HemisphereLight(0xffffff, 0x4a5350, 0.8));
		const key = new THREE.DirectionalLight(0xffffff, 1.5);
		key.position.set(3, 4, 2);
		const fill = new THREE.DirectionalLight(0xffffff, 0.45);
		fill.position.set(-3, -1, -2.5);
		scene.add(key, fill);
		group = new THREE.Group();
		scene.add(group);
		ready = true;
		aimCamera();
		draw();

		const resize = () => {
			const width = canvas.clientWidth;
			const height = canvas.clientHeight;
			if (!width || !height) return;
			renderer.setSize(width, height, false);
			camera.aspect = width / height;
			camera.updateProjectionMatrix();
		};
		const observer = new ResizeObserver(resize);
		observer.observe(canvas);
		resize();

		let frame = 0;
		let last = performance.now();
		const tick = (now: number) => {
			const dt = (now - last) / 1000;
			last = now;
			if (playing) {
				const next = view.progress + dt / 6;
				view.progress = next >= 1 ? ((playing = false), 1) : next;
			}
			controls.update();
			renderer.render(scene, camera);
			frame = requestAnimationFrame(tick);
		};
		frame = requestAnimationFrame(tick);
		return () => {
			cancelAnimationFrame(frame);
			observer.disconnect();
			controls.dispose();
			renderer.dispose();
		};
	});

	function pick(id: WorldId) {
		const preset = id === 'swim-ring' ? 'swim-ring-inner' : id === 'earth' ? 'earth-equator' : id;
		view = { ...view, ...PRESETS[preset], progress: 0 };
		playing = false;
		aimCamera();
	}

	const pct = (x: number) => `${x.toFixed(x < 10 ? 2 : 1)}%`;
</script>

<figure class="not-prose overflow-hidden rounded-md border border-border bg-card">
	<div class="flex flex-wrap items-center gap-1 border-b border-border px-3 py-2">
		{#each Object.values(WORLDS) as w (w.id)}
			<button
				type="button"
				onclick={() => pick(w.id)}
				aria-pressed={view.world === w.id}
				class="rounded-sm px-2.5 py-1 font-mono text-[11px] tracking-wider uppercase transition-colors {view.world ===
				w.id
					? 'bg-primary text-primary-foreground'
					: 'text-muted-foreground hover:bg-accent'}"
			>
				{w.label}
			</button>
		{/each}
		<span class="ml-auto hidden text-xs text-muted-foreground sm:inline">{world.scale}</span>
	</div>

	<div class="grid lg:grid-cols-[1fr_15rem]">
		<div class="relative">
			<canvas
				bind:this={canvas}
				class="block h-[22rem] w-full touch-none lg:h-[26rem]"
				aria-label="Two walkers on {world.label}"
			></canvas>
			<p class="pointer-events-none absolute bottom-2 left-3 text-xs text-muted-foreground">
				Drag to turn · scroll to zoom
			</p>
		</div>

		<div class="grid content-start gap-3 border-t border-border p-3 lg:border-t-0 lg:border-l">
			<div>
				<p class="eyebrow">Gap between the paths</p>
				<p class="mt-0.5 font-mono text-2xl tabular-nums">
					{formatLength(values.gap, view.world)}
				</p>
				<p class="font-mono text-xs text-muted-foreground tabular-nums">
					{values.gapChange >= 0 ? '+' : ''}{values.gapChange.toFixed(
						values.gapChange > -10 && values.gapChange < 10 ? 3 : 1
					)} mm since the start
				</p>
			</div>
			<dl class="grid grid-cols-2 gap-x-3 gap-y-2 text-sm lg:grid-cols-1">
				<div>
					<dt class="eyebrow">Share of the start</dt>
					<dd class="font-mono tabular-nums">{pct(values.gapShare)}</dd>
				</div>
				<div>
					<dt class="eyebrow">Extra per stretch</dt>
					<dd class="font-mono tabular-nums">
						{values.extraShare >= 0 ? '' : '−'}{pct(Math.abs(values.extraShare))}
					</dd>
				</div>
				{#if shown.has('alongPathPart')}
					<div>
						<dt class="eyebrow">Along the path</dt>
						<dd class="font-mono tabular-nums">
							{formatLength(values.alongPathPart, view.world)}
						</dd>
					</div>
					<div>
						<dt class="eyebrow">Whole string</dt>
						<dd class="font-mono tabular-nums">{formatLength(values.stringLength, view.world)}</dd>
					</div>
				{/if}
				<div>
					<dt class="eyebrow">Walked</dt>
					<dd class="font-mono tabular-nums">{formatLength(values.distanceWalked, view.world)}</dd>
				</div>
			</dl>
		</div>
	</div>

	<div class="grid gap-3 border-t border-border px-3 py-3 sm:grid-cols-2">
		<label class="grid gap-1">
			<span class="eyebrow flex justify-between">
				<span>Walk</span>
				<span class="font-mono">{(view.progress * 100).toFixed(0)}%</span>
			</span>
			<div class="flex items-center gap-2">
				<input
					type="range"
					min="0"
					max="1"
					step="0.005"
					bind:value={view.progress}
					class="w-full accent-primary"
					aria-label="How far they have walked"
				/>
				<button
					type="button"
					onclick={() => {
						if (view.progress >= 1) view.progress = 0;
						playing = !playing;
					}}
					class="shrink-0 rounded border border-border px-2 py-1 font-mono text-[11px] tracking-wider uppercase hover:border-primary hover:text-primary"
				>
					{playing ? 'Pause' : 'Walk'}
				</button>
			</div>
		</label>

		<label class="grid gap-1">
			<span class="eyebrow flex justify-between">
				<span>Starting gap</span>
				<span class="font-mono">{formatLength(view.gap, view.world)}</span>
			</span>
			{#if world.gapParam === 'gap-m'}
				<input
					type="range"
					min="1"
					max={view.world === 'earth' ? 1000 : 100}
					step="1"
					bind:value={view.gap}
					class="accent-primary"
					aria-label="Starting gap in metres"
				/>
			{:else}
				<input
					type="range"
					min="0.2"
					max="10"
					step="0.1"
					value={view.gap * 100}
					oninput={(e) => (view.gap = Number(e.currentTarget.value) / 100)}
					class="accent-primary"
					aria-label="Starting gap in centimetres"
				/>
			{/if}
		</label>

		<label class="grid gap-1">
			<span class="eyebrow flex justify-between">
				<span>Stretches</span>
				<span class="font-mono">{view.stretches}</span>
			</span>
			<input
				type="range"
				min="2"
				max="12"
				step="1"
				bind:value={view.stretches}
				class="accent-primary"
				aria-label="Number of stretches"
			/>
		</label>

		{#if view.world === 'swim-ring'}
			<div class="grid gap-1">
				<span class="eyebrow">Start circle</span>
				<div class="flex gap-1">
					{#each ['inner', 'outer'] as circle (circle)}
						<button
							type="button"
							onclick={() =>
								(view = { ...view, startCircle: circle as 'inner' | 'outer', progress: 0 })}
							aria-pressed={view.startCircle === circle}
							class="rounded-sm border px-2 py-1 font-mono text-[11px] tracking-wider uppercase {view.startCircle ===
							circle
								? 'border-primary text-primary'
								: 'border-border text-muted-foreground'}"
						>
							{circle}
						</button>
					{/each}
				</div>
			</div>
		{:else if world.gapParam === 'gap-m'}
			<label class="grid gap-1">
				<span class="eyebrow flex justify-between">
					<span>Head start for the orange walker</span>
					<span class="font-mono">{view.headStart.toFixed(1)} m</span>
				</span>
				<input
					type="range"
					min="0"
					max="10"
					step="0.5"
					bind:value={view.headStart}
					class="accent-primary"
					aria-label="Head start in metres"
				/>
			</label>
		{/if}
	</div>

	<figcaption class="border-t border-border px-3 py-2 text-sm text-muted-foreground">
		Two walkers start side by side and never steer. The green tape joins them at matching step
		counts.
		{#if world.shape === 'plane' || world.shape === 'tube'}
			This world is flat: the tape never changes, however far they walk.
		{:else if world.shape === 'sphere'}
			This world curves the same way everywhere, so the tape shrinks until they meet at the pole.
		{:else}
			A swim ring curves one way over the top and the other way through the hole, so the tape grows
			or shrinks depending on where they start.
		{/if}
	</figcaption>
</figure>
