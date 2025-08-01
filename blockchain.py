import hashlib
import json
from time import time
from utils.crypto import sign_vote, verify_vote


class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_votes = []
        self.voted_ids = set() 
        self.create_block(previous_hash="0", proof=1)  # Genesis block

    def create_block(self, proof, previous_hash):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "votes": self.pending_votes,  # Add all pending votes to the block
            "proof": proof,
            "previous_hash": previous_hash,
        }
        self.pending_votes = []  # Clear pending votes
        self.chain.append(block)
        return block

    def add_vote(self, voter_id, candidate_id):
        if voter_id in self.voted_ids:
            # Reject the vote if the voter has already voted
            return False  # Can return False or raise an exception
        else:
            vote_data = "{voter_id}:{candidate_id}"
            signature = sign_vote(vote_data)
            self.pending_votes.append({
                "voter_id": voter_id,
                "candidate_id": candidate_id,
                "signature": signature
            })
            self.voted_ids.add(voter_id)  # Add the voter ID to the set of voted IDs
            return True  # Successfully added the vote

    def validate_votes(self, votes):
        for vote in votes:
            vote_data = f"{vote['voter_id']}:{vote['candidate_id']}"
            if not verify_vote(vote_data, vote["signature"]):
                return False
        return True

    def proof_of_work(self, previous_proof):
        new_proof = 1
        while True:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()
            ).hexdigest()
            if hash_operation[:4] == "0000":
                return new_proof
            new_proof += 1

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate previous hash
            if current_block["previous_hash"] != self.hash(previous_block):
                return False

            # Validate votes
            if not self.validate_votes(current_block["votes"]):
                return False

            # Validate proof of work
            proof = current_block["proof"]
            previous_proof = previous_block["proof"]
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()
            ).hexdigest()
            if hash_operation[:4] != "0000":
                return False

        return True
