from Blockchain import Blockchain
from Transaction import Transaction
from Client import Client
import time

blockchain = Blockchain()
myclient = Client()
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
        print(f"{t.amount} from: ...{t.sender[-20:]} to: ...{t.recipient[-20:]}")
get_transactions(True)
blockchain.mine(myclient.address())
print('\n\n\n')
get_transactions()
t=myclient.send_money(clients[0].address(),1.5)
blockchain.queue_transaction(t)
t=myclient.send_money(clients[1].address(),0.005)
blockchain.queue_transaction(t)
# this (below) is an orphaned transaction
# notice how it thrown out 
t=clients[0].send_money(clients[3].address(),0.05)
blockchain.queue_transaction(t)
t=myclient.send_money(clients[5].address(),0.05)
blockchain.queue_transaction(t)
blockchain.mine(myclient.address())
print('\n\n\n')
get_transactions()
