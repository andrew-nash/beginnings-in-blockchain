from Blockchain import Blockchain
from Transaction import Transaction
from Client import Client
app = Flask(__name__)

blockchain = Blockchain()
client = Client()


@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/information/address')
def get_address():
    return client.public_key

@app.route('/transactions/make', methods=['POST'])
def new_transaction():
    values = request.form
    
    
