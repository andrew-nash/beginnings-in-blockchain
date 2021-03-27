from Blockchain import Blockchain
from Transaction import Transaction
from Client import Client
import json

app = Flask(__name__)

blockchain = Blockchain()
client = Client()

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/information/address', methods=['GET'])
def get_address():
    return binascii.hexlify(client.public_key).decode('ascii'), 201

def new_transaction(recip_address, amount):
    t = client.send_money(recip_address, amount)
    blockchain.queue_transaction(t)
