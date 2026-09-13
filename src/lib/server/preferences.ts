import { eq } from 'drizzle-orm';
import { db } from '#lib/server/db/index.js';
import { userPreference } from '#lib/server/db/schema.js';

export type Preferences = typeof userPreference.$inferSelect;
export type PreferencesPatch = Partial<Omit<Preferences, 'userId' | 'updatedAt'>>;

export const DEFAULT_PREFERENCES: Omit<Preferences, 'userId' | 'updatedAt'> = {
	theme: 'system',
	tutorVoice: 'marin',
	narrationVoiceId: null,
	narrationModel: 'eleven_multilingual_v2',
	narrationSpeed: 1
};

export async function getPreferences(userId: string): Promise<Preferences> {
	const [row] = await db.select().from(userPreference).where(eq(userPreference.userId, userId)).limit(1);
	return row ?? { userId, ...DEFAULT_PREFERENCES, updatedAt: new Date() };
}

export async function savePreferences(userId: string, patch: PreferencesPatch): Promise<void> {
	const now = new Date();
	await db
		.insert(userPreference)
		.values({ userId, ...DEFAULT_PREFERENCES, ...patch, updatedAt: now })
		.onConflictDoUpdate({ target: userPreference.userId, set: { ...patch, updatedAt: now } });
}
