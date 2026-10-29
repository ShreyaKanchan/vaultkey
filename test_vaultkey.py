import unittest
from vaultkey import Wallet

class WalletTests(unittest.TestCase):
    def test_signature_is_message_bound(self):
        wallet = Wallet(); signature = wallet.sign("hello")
        self.assertTrue(wallet.verify("hello", signature))
        self.assertFalse(wallet.verify("goodbye", signature))

    def test_wallet_addresses_are_unique(self):
        self.assertNotEqual(Wallet().address, Wallet().address)

if __name__ == "__main__": unittest.main()
