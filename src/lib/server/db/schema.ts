import { index, integer, primaryKey, real, sqliteTable, text, uniqueIndex } from 'drizzle-orm/sqlite-core';
import { user } from './auth.schema';

const id = () =>
	text('id')
		.primaryKey()
		.$defaultFn(() => crypto.randomUUID());
const userId = () =>
	text('user_id')
		.notNull()
		.references(() => user.id, { onDelete: 'cascade' });
const createdAt = () =>
	integer('created_at', { mode: 'timestamp_ms' })
		.notNull()
		.$defaultFn(() => new Date());
const updatedAt = () =>
	integer('updated_at', { mode: 'timestamp_ms' })
		.notNull()
		.$defaultFn(() => new Date())
		.$onUpdateFn(() => new Date());

export const PROVIDERS = ['openai', 'elevenlabs'] as const;
export type Provider = (typeof PROVIDERS)[number];

/** Per-user settings for display, the voice tutor, and narration. */
export const userPreference = sqliteTable('user_preference', {
	userId: text('user_id')
		.primaryKey()
		.references(() => user.id, { onDelete: 'cascade' }),
	theme: text('theme', { enum: ['system', 'light', 'dark'] })
		.notNull()
		.default('system'),
	tutorVoice: text('tutor_voice').notNull().default('marin'),
	narrationVoiceId: text('narration_voice_id'),
	narrationModel: text('narration_model').notNull().default('eleven_multilingual_v2'),
	narrationSpeed: real('narration_speed').notNull().default(1),
	updatedAt: updatedAt()
});

/** Bring-your-own provider keys, encrypted with AES-256-GCM. Only `last4` is ever shown to the user. */
export const providerCredential = sqliteTable(
	'provider_credential',
	{
		id: id(),
		userId: userId(),
		provider: text('provider', { enum: PROVIDERS }).notNull(),
		ciphertext: text('ciphertext').notNull(),
		iv: text('iv').notNull(),
		tag: text('tag').notNull(),
		last4: text('last4').notNull(),
		createdAt: createdAt(),
		updatedAt: updatedAt()
	},
	(t) => [uniqueIndex('provider_credential_user_provider').on(t.userId, t.provider)]
);

export const EVENT_KINDS = ['visited', 'listened', 'asked', 'attempted', 'demonstrated', 'misconception'] as const;
export const SUBJECT_TYPES = ['unit', 'concept', 'lesson', 'lab', 'equation'] as const;

/**
 * Append-only learning evidence. Kinds stay distinct: visiting or listening is not demonstrating.
 * `idempotencyKey` (for example a tutor tool call id) prevents duplicate writes on retries.
 */
export const learningEvent = sqliteTable(
	'learning_event',
	{
		id: id(),
		userId: userId(),
		kind: text('kind', { enum: EVENT_KINDS }).notNull(),
		subjectType: text('subject_type', { enum: SUBJECT_TYPES }).notNull(),
		subjectId: text('subject_id').notNull(),
		payload: text('payload', { mode: 'json' }).$type<Record<string, unknown>>(),
		idempotencyKey: text('idempotency_key').unique(),
		createdAt: createdAt()
	},
	(t) => [index('learning_event_user_time').on(t.userId, t.createdAt), index('learning_event_user_subject').on(t.userId, t.subjectId)]
);

/** Current understanding per concept id, derived from learning events. */
export const conceptState = sqliteTable(
	'concept_state',
	{
		userId: userId(),
		conceptId: text('concept_id').notNull(),
		status: text('status', { enum: ['unseen', 'introduced', 'practicing', 'secure'] })
			.notNull()
			.default('unseen'),
		evidenceCount: integer('evidence_count').notNull().default(0),
		lastEvidenceAt: integer('last_evidence_at', { mode: 'timestamp_ms' }),
		updatedAt: updatedAt()
	},
	(t) => [primaryKey({ columns: [t.userId, t.conceptId] })]
);

/** What the learner says they want to understand, linked to concept ids when known. */
export const learnerGoal = sqliteTable('learner_goal', {
	id: id(),
	userId: userId(),
	text: text('text').notNull(),
	conceptIds: text('concept_ids', { mode: 'json' }).$type<string[]>().notNull().default([]),
	status: text('status', { enum: ['active', 'done', 'dropped'] })
		.notNull()
		.default('active'),
	createdAt: createdAt()
});

/** One GPT-Live conversation, with the summary that seeds the next session. */
export const tutorSession = sqliteTable(
	'tutor_session',
	{
		id: id(),
		userId: userId(),
		liveSessionId: text('live_session_id').notNull(),
		context: text('context', { mode: 'json' }).$type<Record<string, unknown>>(),
		startedAt: createdAt(),
		endedAt: integer('ended_at', { mode: 'timestamp_ms' }),
		usageSeconds: integer('usage_seconds'),
		summary: text('summary')
	},
	(t) => [index('tutor_session_user_time').on(t.userId, t.startedAt)]
);

export const note = sqliteTable(
	'note',
	{
		id: id(),
		userId: userId(),
		subjectType: text('subject_type', { enum: SUBJECT_TYPES }).notNull(),
		subjectId: text('subject_id').notNull(),
		body: text('body').notNull(),
		createdAt: createdAt(),
		updatedAt: updatedAt()
	},
	(t) => [index('note_user_subject').on(t.userId, t.subjectId)]
);

export * from './auth.schema';
