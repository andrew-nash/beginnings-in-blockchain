import time
from hashlib import sha256


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.timestamp = time.time()
        self.amount = amount
        self.sender = sender
        self.recipient = recipient

    def hash(self):
        return sha256(((str(self.timestamp)+';'+self.sender+';'+self.recipient+';'\
               +str(self.amount)).encode('utf-8'))).hexdigest()
    def __str__(self):
        return str(self.timestamp)+';'+self.sender+';'+self.recipient+';'\
               +str(self.amount)
