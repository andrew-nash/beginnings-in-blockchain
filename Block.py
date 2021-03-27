import time
from hashlib import sha256
from Transaction import Transaction

MINING_REWARD = 12.5

class Block:
    def __init__(self, prev_hash, transactions, timestamp=None, DIFFICULTY=5,\
     mined=(False, None), reward_address=None):
        # the mined argument, if has True as element 0,
        if timestamp==None:
            timestamp = time.time()
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.DIFFICULTY = '0'*DIFFICULTY+'f'*(64-DIFFICULTY)
        self.transactions = transactions
        self.hash_transactions()
        if not mined[0]:
            self.mine(reward_address)
        else:
            self.nonce = mined[1]
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
        self.nonce = 1
        while self.hash()>self.DIFFICULTY:
            self.nonce+=1
        return

    def work(self):
        return 16**5
