from Block import Block
from Transaction import Transaction

class Blockchain:
    def __init__(self):
        self.chain = []
        # genesis block
        self.genesis = Block('0'*64, [])
        self.chain.append(self.genesis)
        self.chain.append(Block(self.chain[-1].hash(), [Transaction("1113212221", "1111265498221", 1.5)]))
