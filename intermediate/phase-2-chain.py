from Block import Block
from Transaction import Transaction
MINING_REWARD = 12.5
class Blockchain:
    def __init__(self):
        self.chain = []
        self.transaction_pool = set([])
        self.processed_transactions = set([])
        # genesis block
        self.genesis = Block('0'*64, [], None, 0, reward_address = '0'*64)
        self.chain.append(self.genesis)
        self.accounts = {}

    def mine(self, reward_address):
        new_block = Block(self.chain[-1].hash(), list(self.transaction_pool), \
        timestamp=None, DIFFICULTY=5, mined = (False, None), reward_address = reward_address)
        self.transaction_pool = set([])
        self.chain.append(block)

    def queue_transaction(self, transaction):
        if transaction.sender == '0':
            if transaction.amount!=MINING_REWARD:
                return None
            else:
                self.transaction_pool.add(transaction)
                return

        if transaction.sender not in self.accounts:
            if transaction.amount!=0:
                return None
            self.accounts[transaction.sender]=0
        if self.accounts[transaction.sender]<transaction.amount:
            return None
        self.transaction_pool.add(transaction)

    def verify_block(self, block):
        for transaction in block.transactions:
            if transaction.sender == '0':
                if transaction.amount!=MINING_REWARD:
                    return False
                continue

            if transaction.sender not in self.accounts:
                if transaction.amount!=0:
                    return False
                self.accounts[transaction.sender]=0
            if self.accounts[transaction.sender]<transaction.amount:
                return False
        return True

    def valid(self, chain, accounts):
        # check if the passed chain is valid
        # processing a dictionary of accounts and balances
        if chain[0]!=self.genesis:
            return False
        for i in range(1,len(chain)):
            if chain[i-1].hash()!=chain[i].prev_hash:
                return False
            for transaction in block.transactions:
                if not transaction.check_signature():
                    return False
                if transaction.sender not in accounts:
                    return False
                if accounts[transaction.sender]<transaction.amount:
                    return False
                accounts[transaction.sender]-=transaction.amount
                if transaction.recipient not in accounts:
                    accounts[transaction.recipient]=0
                accounts[transaction.recipient]+=transaction.amount

        return True
