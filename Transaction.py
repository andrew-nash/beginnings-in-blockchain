import time
from hashlib import sha256
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
import binascii
class Transaction:
    def __init__(self, sender, recipient, amount, private_key=None, signature=None):
        self.timestamp = time.time()
        self.amount = amount
        self.sender = sender
        self.recipient = recipient
        if private_key!=None:
            self.sign(private_key)
        elif signature !=None:
            self.signature = signature
        else:
            assert sender == '0'
            self.signature = "MINING_REWARD:NA"

    def __hash__(self):
        return int(self.hash(), 16)
    def hash(self):
        return sha256(((str(self.timestamp)+';'+self.sender+';'+self.recipient+';'\
               +str(self.amount)).encode('utf-8'))).hexdigest()
    def binary_hash(self):
        hasher = SHA256.new()
        hasher.update((str(self.timestamp)+';'+self.sender+';'+self.recipient+';'\
               +str(self.amount)).encode('utf-8'))
        return hasher
    def sign(self, pk):
        private_key = RSA.importKey(pk)
        signer = PKCS1_v1_5.new(private_key)
        self.signature = signer.sign(self.binary_hash())

    def check_signature(self):
        public_key = RSA.importKey(binascii.unhexlify(self.sender))
        verifier = PKCS1_v1_5.new(public_key)
        h = self.binary_hash()
        return verifier.verify(h, self.signature)

    def __eq__(self, t2):
        return self.hash()==t2.hash()

    def __str__(self):
        return str(self.timestamp)+';'+self.sender+';'+self.recipient+';'\
               +str(self.amount)+';'+self.signature
