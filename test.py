from Blockchain import Blockchain
from Transaction import Transaction
from Client import Client
import time

blockchain = Blockchain()
clients = [Client() for i in range(10)]

t=clients[0].send_money(clients[1].address(), 0)
blockchain.queue_transaction(t)
t=clients[0].send_money(clients[2].address(), 0)
blockchain.queue_transaction(t)
t=clients[3].send_money(clients[1].address(), 0)
blockchain.queue_transaction(t)
t=clients[2].send_money(clients[2].address(), 0)
blockchain.queue_transaction(t)

def get_transactions(pool=False):
    if pool:
        ts = blockchain.transaction_pool
    else:
        ts = blockchain.processed_transactions
    for t in ts:
        if not pool:
            print('###### MINED ########')
        else:
            print('###### PENDING ########')
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(t.timestamp)))
        print(f"{t.amount} from: {t.sender[:50]}... to : {t.recipient[:50]}...")
get_transactions(True)
blockchain.mine()
print('\n\n\n')
get_transactions()
