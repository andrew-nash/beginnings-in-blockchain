from Transaction import Transaction
from Crypto.Cipher import PKCS1_v1_5
import Crypto.Random
from Crypto.PublicKey import RSA
import binascii

class Client:
    def __init__(self):
        self.generate_wallet()


    def generate_wallet(self):
        random_no = Crypto.Random.new().read
        private_key = RSA.generate(2048, random_no)
        self.private_key = private_key.exportKey(format='DER')
        public_key = private_key.publickey()
        self.public_key = public_key.exportKey(format='DER')
    def address(self):
        return binascii.hexlify(self.public_key).decode('ascii')
    def load_wallet(self):
        pass

    def send_money(self, recipient, amount):
        return Transaction(binascii.hexlify(self.public_key).decode('ascii'), recipient, amount, self.private_key)
