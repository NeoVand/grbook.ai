import { describe, expect, it } from 'vitest';
import { openSecret, sealSecret } from './crypto';

const KEY = 'test-key-material-that-is-long-enough-1234';

describe('provider key encryption', () => {
	it('round-trips a secret', () => {
		const sealed = sealSecret('sk-test-abcdefghijklmnop', KEY);
		expect(sealed.ciphertext).not.toContain('sk-test');
		expect(openSecret(sealed, KEY)).toBe('sk-test-abcdefghijklmnop');
	});

	it('uses a fresh IV each time', () => {
		expect(sealSecret('same', KEY).iv).not.toBe(sealSecret('same', KEY).iv);
	});

	it('rejects tampered ciphertext and wrong keys', () => {
		const sealed = sealSecret('secret-value', KEY);
		const tampered = { ...sealed, ciphertext: Buffer.from('x' + Buffer.from(sealed.ciphertext, 'base64').toString('latin1')).toString('base64') };
		expect(() => openSecret(tampered, KEY)).toThrow();
		expect(() => openSecret(sealed, `${KEY}-different`)).toThrow();
	});

	it('refuses short key material', () => {
		expect(() => sealSecret('x', 'short')).toThrow(/at least 32/);
	});
});
