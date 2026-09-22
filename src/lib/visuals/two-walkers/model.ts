/**
 * The model behind the "Two walkers set off side by side" demo.
 *
 * It implements the contract in knowledge/visuals/two-walkers-set-off-side-by-side.json: the same worlds, the same
 * closed-form gap law, the same readouts. The component draws what this file computes and nothing else, so the
 * spec's twenty numerical tests (src/lib/visuals/two-walkers/model.spec.ts) test what a reader actually sees.
 *
 * Every length here is in metres; the readouts convert.
 */

export type WorldId = 'playground' | 'can-label' | 'football' | 'earth' | 'swim-ring';
export type StartCircle = 'inner' | 'outer';

export interface World {
	id: WorldId;
	label: string;
	/** 'plane' and 'tube' are flat: rolling paper into a tube changes no length along it. */
	shape: 'plane' | 'tube' | 'sphere' | 'torus';
	/** Length of the walk, metres. Progress 1 is the end of it. */
	walk: number;
	/** Sphere radius, or the tube radius of the can, metres. */
	radius: number;
	/** Which gap control this world uses, and the unit the reader sets it in. */
	gapParam: 'gap-m' | 'gap-cm';
	scale: string;
}

/** A swim ring: tube radius r around a centre line of radius Rc. */
export const RING = { centre: 0.25, tube: 0.1 };

export const WORLDS: Record<WorldId, World> = {
	playground: {
		id: 'playground',
		label: 'Playground',
		shape: 'plane',
		walk: 100,
		radius: 0,
		gapParam: 'gap-m',
		scale: 'flat floor, 100 m walk'
	},
	'can-label': {
		id: 'can-label',
		label: "Can's label",
		shape: 'tube',
		walk: 0.3,
		radius: 0.3 / (2 * Math.PI),
		gapParam: 'gap-cm',
		scale: '30 cm around, 30 cm walk'
	},
	football: {
		id: 'football',
		label: 'Football',
		shape: 'sphere',
		walk: (Math.PI * (0.7 / (2 * Math.PI))) / 2,
		radius: 0.7 / (2 * Math.PI),
		gapParam: 'gap-cm',
		scale: '70 cm around, equator to pole'
	},
	earth: {
		id: 'earth',
		label: 'Earth',
		shape: 'sphere',
		walk: (Math.PI * (4e7 / (2 * Math.PI))) / 2,
		radius: 4e7 / (2 * Math.PI),
		gapParam: 'gap-m',
		scale: '40 000 km around, equator to pole'
	},
	'swim-ring': {
		id: 'swim-ring',
		label: 'Swim ring',
		shape: 'torus',
		walk: Math.PI * RING.tube,
		radius: RING.tube,
		gapParam: 'gap-cm',
		scale: 'tube 10 cm, hole 25 cm, over the top'
	}
};

export interface State {
	world: WorldId;
	/** Starting gap in metres, whichever control set it. */
	gap: number;
	/** How far behind the blue walker the orange one starts, metres. */
	headStart: number;
	startCircle: StartCircle;
	stretches: number;
	/** 0 at the start of the walk, 1 at its end. */
	progress: number;
}

export const DEFAULTS: State = {
	world: 'football',
	gap: 0.02,
	headStart: 0,
	startCircle: 'inner',
	stretches: 6,
	progress: 0
};

/** Presets from the spec, by id. */
export const PRESETS: Record<string, Partial<State>> = {
	playground: { world: 'playground', gap: 10, headStart: 0, stretches: 6 },
	'playground-head-start': { world: 'playground', gap: 1, headStart: 3, stretches: 6 },
	'can-label': { world: 'can-label', gap: 0.02, headStart: 0, stretches: 6 },
	football: { world: 'football', gap: 0.02, headStart: 0, stretches: 6 },
	'earth-equator': { world: 'earth', gap: 100, headStart: 0, stretches: 6 },
	'earth-twelve-stretches': { world: 'earth', gap: 100, headStart: 0, stretches: 12 },
	'earth-one-metre': { world: 'earth', gap: 1, headStart: 0, stretches: 6 },
	'earth-head-start': { world: 'earth', gap: 1, headStart: 3, stretches: 6 },
	'swim-ring-inner': {
		world: 'swim-ring',
		gap: 0.003,
		headStart: 0,
		startCircle: 'inner',
		stretches: 6
	},
	'swim-ring-outer': {
		world: 'swim-ring',
		gap: 0.003,
		headStart: 0,
		startCircle: 'outer',
		stretches: 6
	}
};

/**
 * The gap between the two straight walks after walking `s` metres, measured along the curve of matching counts.
 * Flat worlds keep it; a ball closes it as cos(s/a); a swim ring scales it with the distance from the hole's axis.
 * The law continues through s = 0 and past the end of the walk, which the extra-share readout needs.
 */
export function gapAt(state: State, s: number): number {
	const world = WORLDS[state.world];
	switch (world.shape) {
		case 'plane':
		case 'tube':
			return state.gap;
		case 'sphere':
			return state.gap * Math.cos(s / world.radius);
		case 'torus': {
			const { centre: Rc, tube: r } = RING;
			const sign = state.startCircle === 'inner' ? -1 : 1;
			return (state.gap * (Rc + sign * r * Math.cos(s / r))) / (Rc + sign * r);
		}
	}
}

/** Gaussian curvature where the walkers stand, per square metre. Zero on both flat worlds. */
export function curvatureAt(state: State, s: number): number {
	const world = WORLDS[state.world];
	if (world.shape === 'plane' || world.shape === 'tube') return 0;
	if (world.shape === 'sphere') return 1 / world.radius ** 2;
	const { centre: Rc, tube: r } = RING;
	const psi = state.startCircle === 'inner' ? Math.PI + s / r : s / r;
	return Math.cos(psi) / (r * (Rc + r * Math.cos(psi)));
}

export interface Readouts {
	/** Metres between the paths. */
	gap: number;
	/** Millimetres gained or lost since the start. */
	gapChange: number;
	/** Percentage of the starting gap. */
	gapShare: number;
	/** Percentage the gap falls short of a straight continuation, over one stretch. */
	extraShare: number;
	/** Metres of the string that lie along the path, when the orange walker has a head start. */
	alongPathPart: number;
	/** Metres of string from one walker to the other. */
	stringLength: number;
	/** The two below travel with the readouts so the component never re-derives them. */
	distanceWalked: number;
	curvature: number;
}

export function readouts(state: State): Readouts {
	const world = WORLDS[state.world];
	const s = state.progress * world.walk;
	const gap = gapAt(state, s);
	const h = world.walk / state.stretches;

	// Minus the second difference of the gap over one stretch, as a share of the gap: the curvature a walker can read
	// off the tape. On a ball the quotient is the same everywhere, so it is taken in closed form: at the pole the gap
	// is zero (to rounding, 6e-17 rather than 0) and dividing by it would print a number that means nothing.
	let extraShare: number;
	if (world.shape === 'sphere') extraShare = 200 * (1 - Math.cos(h / world.radius));
	else if (world.shape === 'torus')
		extraShare = (-(gapAt(state, s + h) - 2 * gap + gapAt(state, s - h)) / gap) * 100;
	else extraShare = 0;

	return {
		gap,
		gapChange: (gap - state.gap) * 1000,
		gapShare: (gap / state.gap) * 100,
		extraShare,
		alongPathPart: state.headStart,
		stringLength: Math.hypot(gap, state.headStart),
		distanceWalked: s,
		curvature: curvatureAt(state, s)
	};
}

/** The readouts the demo shows: the string parts appear only when the orange walker has a head start. */
export function visibleReadouts(state: State): Set<keyof Readouts> {
	const shown = new Set<keyof Readouts>(['gap', 'gapChange', 'gapShare', 'extraShare']);
	if (state.headStart > 0) {
		shown.add('alongPathPart');
		shown.add('stringLength');
	}
	return shown;
}

/** A point on the world's surface, for the 3D scene. Metres, in the world's own frame. */
export type Point = [number, number, number];

/**
 * Where a walker stands after walking `s` metres, `offset` metres to the right of the blue walker's start.
 * The blue walker is at offset 0; the orange one at the starting gap, minus any head start along the path.
 */
export function walkerAt(state: State, s: number, offset: number): Point {
	const world = WORLDS[state.world];
	switch (world.shape) {
		case 'plane':
			return [offset, 0, -s];
		case 'tube': {
			const a = world.radius;
			const angle = offset / a;
			return [a * Math.sin(angle), a * Math.cos(angle), -s];
		}
		case 'sphere': {
			const a = world.radius;
			const lat = s / a; // colatitude measured up from the equator
			const lon = offset / a;
			return [
				a * Math.cos(lat) * Math.sin(lon),
				a * Math.sin(lat),
				a * Math.cos(lat) * Math.cos(lon)
			];
		}
		case 'torus': {
			const { centre: Rc, tube: r } = RING;
			const psi = state.startCircle === 'inner' ? Math.PI + s / r : s / r;
			const ringRadius = Rc + r * Math.cos(psi);
			const angle = offset / ringRadius;
			return [ringRadius * Math.sin(angle), r * Math.sin(psi), ringRadius * Math.cos(angle)];
		}
	}
}

/** The two trails, sampled for drawing: `steps` points each from the start to where the walkers stand now. */
export function trails(state: State, steps = 96): { blue: Point[]; orange: Point[] } {
	const world = WORLDS[state.world];
	const s = state.progress * world.walk;
	const blue: Point[] = [];
	const orange: Point[] = [];
	for (let i = 0; i <= steps; i++) {
		const t = (s * i) / steps;
		blue.push(walkerAt(state, t, 0));
		orange.push(walkerAt(state, Math.max(0, t - state.headStart), state.gap));
	}
	return { blue, orange };
}

/** The tape at matching counts, from the blue walker across to the orange one. */
export function tape(state: State, steps = 48): Point[] {
	const world = WORLDS[state.world];
	const s = state.progress * world.walk;
	const points: Point[] = [];
	for (let i = 0; i <= steps; i++) points.push(walkerAt(state, s, (state.gap * i) / steps));
	return points;
}

/** Distances walked at each white tick mark, metres. */
export function stretchMarks(state: State): number[] {
	const world = WORLDS[state.world];
	return Array.from({ length: state.stretches + 1 }, (_, i) => (world.walk * i) / state.stretches);
}

/** Formats a length for a reader: metres on the big worlds, centimetres or millimetres on the small ones. */
export function formatLength(metres: number, world: WorldId): string {
	if (world === 'earth')
		return metres >= 1000
			? `${(metres / 1000).toLocaleString('en', { maximumFractionDigits: 1 })} km`
			: `${metres.toFixed(1)} m`;
	if (world === 'playground') return `${metres.toFixed(metres < 10 ? 2 : 1)} m`;
	return `${(metres * 100).toFixed(2)} cm`;
}
