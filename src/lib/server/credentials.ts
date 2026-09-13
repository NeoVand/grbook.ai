import { and, eq } from 'drizzle-orm';
import { CREDENTIALS_ENCRYPTION_KEY } from '$app/env/private';
import { db } from '#lib/server/db/index.js';
import { providerCredential, type Provider } from '#lib/server/db/schema.js';
import { openSecret, sealSecret } from '#lib/server/crypto.js';

export interface ProviderKeyStatus {
	provider: Provider;
	last4: string;
	updatedAt: Date;
}

function keyMaterial(): string {
	if (!CREDENTIALS_ENCRYPTION_KEY) throw new Error('CREDENTIALS_ENCRYPTION_KEY is not set');
	return CREDENTIALS_ENCRYPTION_KEY;
}

/** Stores or replaces a user's provider key, encrypted at rest. */
export async function saveProviderKey(userId: string, provider: Provider, apiKey: string): Promise<ProviderKeyStatus> {
	const trimmed = apiKey.trim();
	if (trimmed.length < 16 || /\s/.test(trimmed)) throw new Error('That does not look like an API key');
	const sealed = sealSecret(trimmed, keyMaterial());
	const now = new Date();
	const values = { userId, provider, ...sealed, last4: trimmed.slice(-4), updatedAt: now };
	await db
		.insert(providerCredential)
		.values(values)
		.onConflictDoUpdate({ target: [providerCredential.userId, providerCredential.provider], set: values });
	return { provider, last4: values.last4, updatedAt: now };
}

/** Returns the decrypted key for server-side use only. Never send the result to the browser or log it. */
export async function getProviderKey(userId: string, provider: Provider): Promise<string | null> {
	const [row] = await db
		.select()
		.from(providerCredential)
		.where(and(eq(providerCredential.userId, userId), eq(providerCredential.provider, provider)))
		.limit(1);
	return row ? openSecret(row, keyMaterial()) : null;
}

export async function listProviderKeys(userId: string): Promise<ProviderKeyStatus[]> {
	const rows = await db
		.select({ provider: providerCredential.provider, last4: providerCredential.last4, updatedAt: providerCredential.updatedAt })
		.from(providerCredential)
		.where(eq(providerCredential.userId, userId));
	return rows;
}

export async function deleteProviderKey(userId: string, provider: Provider): Promise<void> {
	await db
		.delete(providerCredential)
		.where(and(eq(providerCredential.userId, userId), eq(providerCredential.provider, provider)));
}
