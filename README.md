# VaultKey

> A local wallet-learning project that makes key generation, address derivation, message signing, and verification easy to inspect.

![VaultKey](assets/logo.svg)

Local wallet demo showing key generation, address derivation, and message signing with the Python standard library.

```bash
python3 vaultkey.py
```

This is a teaching example. It is not a secure wallet: use audited cryptographic libraries and hardware-backed keys for real funds.

## Workflow

The wallet creates a random private key, derives a display address, signs a UTF-8 message, and verifies the signature with constant-time comparison. The example is deliberately transparent so the lifecycle can be inspected in a debugger.

## Production notes

Never print or commit private keys. A real wallet should use standard elliptic-curve signatures, encrypted keystore files, secure backups, chain-specific address encoding, nonce management, and hardware or OS key protection.
