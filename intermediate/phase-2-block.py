import time
from hashlib import sha256
from Transaction import Transaction

MINING_REWARD = 12.5

class Block:
    def __init__(self, prev_hash, transactions, timestamp=None):
        if timestamp==None:
            timestamp = time.time()
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.transaction_hash = None
        self.transactions = transactions
        seld.nonce = 1
        self.DIFFICULTY = '0'*5+'f'*
        self.hash_transactions()


    def hash(self):
        return sha256(str(self).encode('utf-8')).hexdigest()

    def __str__(self):
        return str(self.timestamp)+';'+str(self.prev_hash)+';'+str(self.transaction_hash)+';'+\
               str(self.nonce)

    def hash_transactions(self):
        hashes = [x.hash() for x in self.transactions]
        self.transaction_hash = sha256(''.join(hashes).encode('utf-8')).hexdigest()

    def mine(self, raddr):
        reward = Transaction('0', raddr, MINING_REWARD)
        self.transactions.append(reward)
        self.hash_transactions()

        while int(self.hash(),16)>int(self.DIFFICULTY,16):
            self.nonce+=1
        return


#00001fffffffffffffff
#00023454234fffffffff
