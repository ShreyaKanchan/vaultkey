"""Password-wrapped demo keystore; use audited encryption for real keys."""
import hashlib, hmac, secrets
def derive_key(password, salt): return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100_000, 32)
def seal(secret, password):
    salt = secrets.token_bytes(16); key = derive_key(password, salt); mask = hmac.new(key, b"keystore", hashlib.sha256).digest(); return salt.hex(), bytes(a ^ b for a, b in zip(secret, mask)).hex()
