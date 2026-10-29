"""Toy wallet flow using HMAC to make the signing lifecycle visible."""
import hashlib, hmac, secrets

class Wallet:
    def __init__(self):
        self.private_key = secrets.token_bytes(32)
        self.address = hashlib.sha256(self.private_key).hexdigest()[:40]

    def sign(self, message: str) -> str:
        return hmac.new(self.private_key, message.encode(), hashlib.sha256).hexdigest()

    def verify(self, message: str, signature: str) -> bool:
        return hmac.compare_digest(self.sign(message), signature)

if __name__ == "__main__":
    wallet = Wallet(); message = "approve:42"
    signature = wallet.sign(message)
    print({"address": wallet.address, "signature": signature, "valid": wallet.verify(message, signature)})
