/** ElevenLabs returns character-level timings; narration highlighting works on words. */

export interface CharacterAlignment {
	characters: string[];
	character_start_times_seconds: number[];
	character_end_times_seconds: number[];
}

export interface WordTiming {
	text: string;
	/** Seconds from the start of the clip. */
	start: number;
	end: number;
	/** Character offsets into the synthesized text, end exclusive. */
	charStart: number;
	charEnd: number;
}

export function wordsFromAlignment(alignment: CharacterAlignment, offsetSeconds = 0): WordTiming[] {
	const { characters, character_start_times_seconds: starts, character_end_times_seconds: ends } = alignment;
	const words: WordTiming[] = [];
	let current: WordTiming | null = null;
	for (let i = 0; i < characters.length; i++) {
		const ch = characters[i];
		if (/\s/.test(ch)) {
			if (current) words.push(current);
			current = null;
			continue;
		}
		if (!current) {
			current = { text: '', start: starts[i] + offsetSeconds, end: ends[i] + offsetSeconds, charStart: i, charEnd: i + 1 };
		}
		current.text += ch;
		current.end = ends[i] + offsetSeconds;
		current.charEnd = i + 1;
	}
	if (current) words.push(current);
	return words;
}

/** Index of the word being spoken at `time`, or -1 before the first word. */
export function wordAt(words: WordTiming[], time: number): number {
	let lo = 0;
	let hi = words.length - 1;
	let found = -1;
	while (lo <= hi) {
		const mid = (lo + hi) >> 1;
		if (words[mid].start <= time) {
			found = mid;
			lo = mid + 1;
		} else {
			hi = mid - 1;
		}
	}
	return found;
}
