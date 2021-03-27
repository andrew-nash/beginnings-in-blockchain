import time
from hashlib import sha256
from Transaction import Transaction


class Block:
    def __init__(self, prev_hash, transactions, timestamp=None):
        if timestamp==None:
            timestamp = time.time()
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.DIFFICULTY = '0'*DIFFICULTY+'f'*(64-DIFFICULTY)
        self.transactions = transactions
        self.hash_transactions()


    def hash(self):
        return sha256(str(self).encode('utf-8')).hexdigest()

    def __str__(self):
        return str(self.timestamp)+';'+str(self.prev_hash)+';'+str(self.transaction_hash)+';'+\
               str(self.nonce)

    def hash_transactions(self):
        hashes = [x.hash() for x in self.transactions]
        self.transaction_hash = sha256(''.join(hashes).encode('utf-8')).hexdigest()
