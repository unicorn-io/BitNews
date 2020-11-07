from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from .ipfs import *
from .main import *
from .news import *
from app.bit_system.models import Contracts

bit_system = Blueprint('process', __name__, url_prefix="/process")

CONNECTED_NODE_ADDRESS="http://127.0.0.1:5000"

posts=[]
pos_dict = {'QmfSJCG7sqbbJrha2XbhyDgDJdnPbQgAwwFJc4BBhHnZTW': [4, 0], 'QmTc7Sqn3Ltce1P8jN1qjAN38C9NVcd7yetBdF4ZLwbi5n': [4, 0], 'QmQHoda8AH1L9HX2qhPjgD6SYfhVovy7Pzz6g1Hf6ow5Hd': [4, 0], 'QmVtvtWmh5eWtnEzHiArketEfK9K66uS3UbE8wnrr19gxR': [4, 0], 'QmbPrG7uZBQf262k4FMm5J6785gUGasegVyDBimj3FRr83': [4, 0], 'QmbYPbUqH8Lb3jF9yX71s1QvwZh24zcQMTSmMhHyPs7RF8': [4, 0], 'QmPVgEnWSgbqMxsE23sh5voGQJN8x2GHjU1Hg8GrrQ3FoZ': [4, 0], 'QmcEBd8BkNeUXh3dhwLixMcL9Ku2knD4zwBsr561TcA825': [4, 0], 'QmaBJin8favo3D6Tn61dySjdAPpVy1UsA5WugQCtSmq1wE': [4, 0], 'QmZJsBT75upJKMQAHPe5mm3woYTHTJv69ibAqNWnbCKPXP': [4, 0], 'QmdXWF7rKJsho267T6yy3HcmYhxPjQGu5BUH2ZTv2uDcdi': [4, 0], 'QmVJrsLdvZxKufeMCqJ3MQayfi6JgPdHioJWdwu4vf6Ls5': [4, 0], 'Qma49NApCJ2DSueZw5Bdm1CYkzNxeVTm3Z7HHUbfEacFEu': [4, 0]}
pos_lis = ['QmfSJCG7sqbbJrha2XbhyDgDJdnPbQgAwwFJc4BBhHnZTW', 'QmTc7Sqn3Ltce1P8jN1qjAN38C9NVcd7yetBdF4ZLwbi5n', 'QmQHoda8AH1L9HX2qhPjgD6SYfhVovy7Pzz6g1Hf6ow5Hd', 'QmVtvtWmh5eWtnEzHiArketEfK9K66uS3UbE8wnrr19gxR', 'QmbPrG7uZBQf262k4FMm5J6785gUGasegVyDBimj3FRr83', 'QmbYPbUqH8Lb3jF9yX71s1QvwZh24zcQMTSmMhHyPs7RF8', 'QmPVgEnWSgbqMxsE23sh5voGQJN8x2GHjU1Hg8GrrQ3FoZ', 'QmcEBd8BkNeUXh3dhwLixMcL9Ku2knD4zwBsr561TcA825', 'QmaBJin8favo3D6Tn61dySjdAPpVy1UsA5WugQCtSmq1wE', 'QmZJsBT75upJKMQAHPe5mm3woYTHTJv69ibAqNWnbCKPXP', 'QmdXWF7rKJsho267T6yy3HcmYhxPjQGu5BUH2ZTv2uDcdi', 'QmVJrsLdvZxKufeMCqJ3MQayfi6JgPdHioJWdwu4vf6Ls5', 'Qma49NApCJ2DSueZw5Bdm1CYkzNxeVTm3Z7HHUbfEacFEu']
#pos_dict = {}
#pos_lis = []
peers = set()
parsed_keys=[]
blockchain = Blockchain()
total_population = 5


@bit_system.route('/new_transaction', methods=['POST'])
def new_transaction():
    tx_data = request.get_json()
    required_fields = ["Hash"]

    for field in required_fields:
        if not tx_data.get(field):
            return "Invalid transaction data", 404

    tx_data["timestamp"] = time.time()

    blockchain.add_new_transaction(tx_data)

    return "Success", 201


@bit_system.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})

# Endpoint to add new peers to the network
@bit_system.route('/register_node', methods=['POST'])
def register_new_peers():
    # The host address of the peer node.
    node_address = request.get_json()['node_address']
    if not node_address:
        return "Invalid data", 400

    # Add the node to the peer list
    peers.add(node_address)
    # Syncing the block chain with the newly created node.
    return get_chain()

@bit_system.route('/register_with', methods=['POST'])
def register_with_existing_node():
    """
    Internally calls the `register_node` endpoint to
    register current node with the remote node specified in the
    request, and sync the blockchain as well with the remote node.
    """
    node_address = request.get_json()['node_address']
    if not node_address:
        return "Invalid data", 400
    
    data = {"node_address": request.host_url}
    headers = {"Content-Type": "application/json"}

    # Make a request to register with remote node and obtain information
    response = requests.post(node_address + "/process/register_node", data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        global blockchain
        global peers
        # update chain and the peers
        chain_dump = response.json()['chain']
        blockchain = create_chain_from_dump(chain_dump)
        peers.update(response.json()['peers'])
        return "Registration succesful", 200
    else:
        # if something goes wrong, pass it on to the API Response
        return response.content, response.status_code

def create_chain_from_dump(chain_dump):
    blockchain = Blockchain()
    for idx, block_data in enumerate(chain_dump):
        block = Block(block_data['index'],
                    block_data['transactions'],
                    block_data['timestamp'],
                    block_data['previous_hash'])
        
        proof = block_data['hash']
        if idx > 0:
            added = blockchain.add_block(block, proof)
            if not added:
                raise Exception("The chain dump is tempered!!")
        else: # The block is a genesis block aka the first block, no verification is needed.
            blockchain.chain.append(block)
    return blockchain

def fetch_posts():
    """
    Function to fetch the chain from a blockchain node, parse the
    data, and store it locally.
    """
    get_chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["index"] = block["previous_hash"]
                content.append(tx)
    
    global posts
    posts = sorted(content, key = lambda k : k['timestamp'], reverse = True)

# endpoint to add a block mined by someone else to
# the node's chain. The node first verifies the block
# and then adds it to the chain.
@bit_system.route('/add_block', methods=['GET'])
def verify_and_add_block():
    block_data = get_json(request.args.get('q'))
    block = Block(block_data["index"],
                  block_data["transactions"],
                  block_data["timestamp"],
                  block_data["previous_hash"])

    proof = block_data['hash']
    added = blockchain.add_block(block, proof)

    if not added:
        return "The block was discarded by the node", 400

    return "Block added to the chain", 201


def announce_new_block(block):
    """
    A function to announce to the network once a block has been mined.
    Other blocks can simply verify the proof of work and add it to their
    respective chains.
    """
    for peer in peers:
        url = "{}add_block".format(peer)
        requests.post(url, data=json.dumps(block.__dict__, sort_keys=True))

def consensus():
    """
    Our simple consensus algorithm. If a longer valid chain is
    found, our chain is replaced with it.
    """
    global blockchain

    longest_chain = None
    current_len = len(blockchain.chain)

    for node in peers:
        response = requests.get('{}/chain'.format(node))
        length = response.json()['length']
        chain = response.json()['chain']
        if length > current_len and blockchain.check_chain_validity(chain):
              # Longer valid chain found!
            current_len = length
            longest_chain = chain

    if longest_chain:
        blockchain = longest_chain
        return True

    return False



@bit_system.route('/mine', methods=['GET'])
def mine_unconfirmed_transactions():
    result = blockchain.mine()
    if not result:
        return "No transactions to mine"
    else:
        # Making sure we have the longest chain before announcing to the network
        chain_length = len(blockchain.chain)
        consensus()
        if chain_length == len(blockchain.chain):
            # announce the recently mined block to the network
            announce_new_block(blockchain.last_block)
        return "Block #{} is mined.".format(blockchain.last_block.index)
    

@bit_system.route('/pending_tx')
def get_pending_tx():
    return json.dumps(blockchain.unconfirmed_transactions)

@bit_system.route('/approve')
def approve():  
    hash = request.args.get('q')
    pos_dict[hash][0] += 1
    if (float(pos_dict[hash][0]/total_population) >= 0.8):
        #add the news to the blockchain
        print("Add to the chain")
        parsed_keys.append(hash)
        redirect("/process/add_block?q="+hash)
    print(len(blockchain.chain))
    return redirect("/process/blog")

@bit_system.route('/disapprove')
def disapprove():
    hash = request.args.get('q')
    pos_dict[hash][1] += 1  
    if (float(pos_dict[hash][1]/total_population) >= 0.6):
        pass #remove the post from consideration
    return "success", 200

@bit_system.route("/verify")
def check_chain():
    hash = request.args.get('q')
    if (parsed_keys.count(hash) > 0):
        return redirect('/view-post?q='+hash+"&real=1")
    else: 
        return redirect('/view-post?q='+hash+"&real=2")


@bit_system.route('/post', methods=['GET','POST'])
def publish():
    title = request.form.get('title')
    content = request.form.get('content')
    url = request.form.get('url')
    urlToImage = request.form.get('urlToImage')
    subject = request.form.get('subject')

    objString = {
        "title": title,
        "subject": subject,
        "content": content,
        "url": url,
        "urlToImage": urlToImage,
    }
    
    
    hash = upload_json(json.dumps(objString))
    
    hash_obj_gen = {
        'Hash': hash
    }
    print(hash_obj_gen)

    pos_dict[hash] = [0,0] # upvotes, downvotes
    pos_lis.insert(0,hash)
    print(pos_lis)
    # TODO : Append the machine learning model value here.
    
    return redirect('/view-post?q='+hash)
    
    # new_tx_address = "{}/process/new_transaction".format(CONNECTED_NODE_ADDRESS)

    # request.post(new_tx_address, json=hash_obj_gen,headers = {'Content'})

    


@bit_system.route('/blog')
def blog():
    with open("blog_data.html", 'w') as blg:
        for hashh in pos_lis:
            blg_data = get_json(hashh)
            print(blg_data)
            blg.write(get_blog_html(blg_data, hashh))
    return render_template('blog.html', post_content=open("blog_data.html", 'r').read())

def get_blog_html(article,   hash):
    return '''<div class="post_content">
                <div class="post_body">
                  <h1> {title} </h1>
                  <p class="post_p">
                    {content}
                  </p>    
                  <span>Hash -- {hash}</span>
                  <span class="butt"></span>
                    
                    <a href="/process/approve?q={hash}"><button class="btn btn-success">Approve</button></a>
                    <a href="/process/disapprove?q={hash}"><button class="btn btn-danger">Disapprove</button></a>
                    <a href="/view-post?q={hash}"><button class="btn btn-dark">Post</button></a>
                  </span>
                </div>
              </div>'''.format(title=article['title'], content=article['content'], hash=hash)
