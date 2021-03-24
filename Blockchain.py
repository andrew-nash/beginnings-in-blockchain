from Block import Block
from Transaction import Transaction
MY_ADDRESS = "f"*64
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

    def mine(self):
        new_block = Block(self.chain[-1].hash(), list(self.transaction_pool), \
        timestamp=None, DIFFICULTY=5, mined = (False, None), reward_address = MY_ADDRESS)
        self.add_block(new_block)

    def queue_transaction(self, t):
        self.transaction_pool.add(t)

    def verify_block(self, block):
        for transaction in block.transactions:
            if transaction.sender == '0':
                if transaction.amount!=MINING_REWARD:
                    return False
                continue

            if not transaction.check_signature():
                print("USNGINED")
                return False
            if transaction.sender not in self.accounts:
                if transaction.amount!=0:
                    return False
                self.accounts[transaction.sender]=0
            if self.accounts[transaction.sender]<transaction.amount:
                return False
        return True

    def add_block(self, block):
        if block.prev_hash!=self.chain[-1].hash():
           return False
        if not self.verify_block(block): return
        for transaction in block.transactions:
            if transaction.sender != '0':
                self.accounts[transaction.sender]-=transaction.amount
            if transaction.recipient not in self.accounts:
                self.accounts[transaction.recipient]=0
            self.accounts[transaction.recipient]+=transaction.amount
            self.processed_transactions.add(transaction)
        self.chain.append(block)


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


    def process_fork(self, candidates):
        best_work = sum([x.work() for x in self.chain])
        # replace the chain with a fork chain, if necessary
        for candidate_chain in candidates:
            total_work = sum([x.work() for x in candidate_chain.chain])

            if total_work > best_work:
                d = {}
                if self.valid(candidate_chain.chain, d):
                    need_renewing = self.processed_transactions - candidate_chain.processed_transactions
                    self.transaction_pool -= candidate_chain.processed_transactions
                    self.transaction_pool += need_renewing
                    self.processed_transactions = candidate_chain.processed_transactions
                    self.accounts = d
                    self.chain = candidate_chain
                    best_work = total_work
