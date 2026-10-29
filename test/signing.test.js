import test from 'node:test';
import assert from 'node:assert/strict';
import { deriveAddress, signMessage, verifyMessage } from '../src/signing.js';

test('derives a stable address from a public key', () => {
  assert.equal(deriveAddress('public-key').length, 42);
  assert.equal(deriveAddress('public-key'), deriveAddress('public-key'));
});

test('verifies only the original message and secret', () => {
  const signature = signMessage('approve 10 PORT', 'demo-secret');
  assert.equal(verifyMessage('approve 10 PORT', signature, 'demo-secret'), true);
  assert.equal(verifyMessage('approve 11 PORT', signature, 'demo-secret'), false);
});
