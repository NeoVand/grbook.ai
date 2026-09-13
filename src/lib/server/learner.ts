import { and, desc, eq, isNotNull } from 'drizzle-orm';
import { db } from '#lib/server/db/index.js';
import { learningEvent, tutorSession } from '#lib/server/db/schema.js';

/**
 * A compact, factual summary of the learner for seeding a tutor session (kept well under the 8,192-token
 * startup history limit). Only recorded evidence is used; nothing is inferred.
 */
export async function learnerSummary(userId: string): Promise<string | null> {
	const events = await db
		.select()
		.from(learningEvent)
		.where(eq(learningEvent.userId, userId))
		.orderBy(desc(learningEvent.createdAt))
		.limit(40);
	const [lastSession] = await db
		.select({ summary: tutorSession.summary, endedAt: tutorSession.endedAt })
		.from(tutorSession)
		.where(and(eq(tutorSession.userId, userId), isNotNull(tutorSession.summary)))
		.orderBy(desc(tutorSession.startedAt))
		.limit(1);

	const byKind = (kind: string) => [...new Set(events.filter((e) => e.kind === kind).map((e) => e.subjectId))].slice(0, 8);
	const notes = (kind: string) =>
		events
			.filter((e) => e.kind === kind && typeof e.payload?.note === 'string')
			.slice(0, 4)
			.map((e) => e.payload!.note as string);

	const parts = [
		byKind('visited').length ? `Recently studied: ${byKind('visited').join(', ')}.` : null,
		notes('asked').length ? `Recent questions: ${notes('asked').join(' | ')}.` : null,
		notes('demonstrated').length ? `Has shown understanding of: ${notes('demonstrated').join(' | ')}.` : null,
		notes('misconception').length ? `Misconceptions observed before: ${notes('misconception').join(' | ')}.` : null,
		lastSession?.summary ? `Last tutor session: ${lastSession.summary}` : null
	].filter(Boolean);
	return parts.length ? parts.join('\n') : null;
}
