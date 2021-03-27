from Transaction import Transaction
from Crypto.Cipher import PKCS1_v1_5
import os
from Crypto.PublicKey import RSA
import binascii

class Client:
    def __init__(self):
        self.public_key = None
        self.private_key = None
        self.generate_wallet()

    def generate_wallet(self):
        private_key = RSA.generate(2048)
        self.private_key = private_key.exportKey(format='DER')
        public_key = private_key.publickey()
        self.public_key = public_key.exportKey(format='DER')
    def address(self):
        return binascii.hexlify(self.public_key).decode('ascii')

    def send_money(self, recipient, amount):
        return Transaction(self.address(), recipient, amount, self.private_key)
