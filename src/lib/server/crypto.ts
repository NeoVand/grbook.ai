import { createCipheriv, createDecipheriv, createHash, randomBytes } from 'node:crypto';

export interface SealedSecret {
	ciphertext: string;
	iv: string;
	tag: string;
}

const MIN_KEY_MATERIAL = 32;

function deriveKey(material: string): Buffer {
	if (!material || material.length < MIN_KEY_MATERIAL) {
		throw new Error(`Encryption key material must be at least ${MIN_KEY_MATERIAL} characters`);
	}
	return createHash('sha256').update(material).digest();
}

/** Encrypts a secret with AES-256-GCM. A fresh 96-bit IV is used for every call. */
export function sealSecret(plaintext: string, keyMaterial: string): SealedSecret {
	const iv = randomBytes(12);
	const cipher = createCipheriv('aes-256-gcm', deriveKey(keyMaterial), iv);
	const ciphertext = Buffer.concat([cipher.update(plaintext, 'utf8'), cipher.final()]);
	return {
		ciphertext: ciphertext.toString('base64'),
		iv: iv.toString('base64'),
		tag: cipher.getAuthTag().toString('base64')
	};
}

/** Decrypts a sealed secret; throws if the key is wrong or the data was tampered with. */
export function openSecret(sealed: SealedSecret, keyMaterial: string): string {
	const decipher = createDecipheriv('aes-256-gcm', deriveKey(keyMaterial), Buffer.from(sealed.iv, 'base64'));
	decipher.setAuthTag(Buffer.from(sealed.tag, 'base64'));
	return Buffer.concat([decipher.update(Buffer.from(sealed.ciphertext, 'base64')), decipher.final()]).toString('utf8');
}
