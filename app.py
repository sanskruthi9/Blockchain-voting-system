from flask import Flask, render_template, request
from blockchain import Blockchain
from utils.crypto import get_public_key_pem

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/vote', methods=['POST'])
def vote():
    voter_id = request.form['voter_id']
    candidate_id = request.form['candidate_id']
    
    # Attempt to add the vote
    if blockchain.add_vote(voter_id, candidate_id):
        signature = blockchain.pending_votes[-1]["signature"]
        return render_template("success.html", voter_id=voter_id, candidate_id=candidate_id, signature=signature)
    else:
        # If the voter has already voted, return an error message
        return render_template("error.html", message="You have already voted!")

@app.route('/mine', methods=['GET'])
def mine_block():
    if not blockchain.pending_votes:
        return render_template("error.html", message="No votes to mine. Please cast votes first!")
    previous_block = blockchain.chain[-1]
    proof = blockchain.proof_of_work(previous_block["proof"])
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    return render_template("block_mined.html", block=block)

@app.route('/chain', methods=['GET'])
def view_chain():
    public_key = get_public_key_pem()
    return render_template("view_chain.html", chain=blockchain.chain, public_key=public_key)

@app.route('/results', methods=['GET'])
def results():
    vote_count = {}
    for block in blockchain.chain:
        for vote in block["votes"]:
            candidate = vote["candidate_id"]
            vote_count[candidate] = vote_count.get(candidate, 0) + 1
    return render_template("results.html", results=vote_count)

@app.route('/validate', methods=['GET'])
def validate_chain():
    is_valid = blockchain.is_chain_valid()
    message = "Blockchain is valid." if is_valid else "Blockchain has been tampered with!"
    return render_template("validation.html", message=message)

@app.route('/public_key', methods=['GET'])
def public_key():
    from utils.crypto import get_public_key_pem
    key_pem = get_public_key_pem()
    return render_template("public_key.html", public_key=key_pem)

if __name__ == '__main__':
    app.run(debug=True)


