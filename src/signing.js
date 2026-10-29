import { createHash, createHmac } from 'node:crypto';

export function deriveAddress(publicKey) {
  return `0x${createHash('sha256').update(publicKey).digest('hex').slice(-40)}`;
}

export function signMessage(message, secret) {
  return createHmac('sha256', secret).update(message).digest('hex');
}

export function verifyMessage(message, signature, secret) {
  return signMessage(message, secret) === signature;
}
