# blockchain.py
import hashlib
import json
from time import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash})"


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_votes = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Create the first block in the blockchain."""
        genesis_block = Block(0, "0", time(), "Genesis Block", self.hash_block(0, "0", time(), "Genesis Block"))
        self.chain.append(genesis_block)

    def add_vote(self, voter_id, candidate_name):
        """Add a new vote to the blockchain."""
        vote = {"voter_id": voter_id, "candidate_name": candidate_name}
        self.current_votes.append(vote)

    def create_block(self):
        """Create a new block with the current votes."""
        if not self.current_votes:
            return None
        last_block = self.chain[-1]
        index = last_block.index + 1
        timestamp = time()
        data = self.current_votes
        previous_hash = last_block.hash
        block_hash = self.hash_block(index, previous_hash, timestamp, data)
        block = Block(index, previous_hash, timestamp, data, block_hash)
        self.chain.append(block)
        self.current_votes = []  # Clear current votes after adding block
        return block

    def hash_block(self, index, previous_hash, timestamp, data):
        """Hash a block using SHA-256."""
        block_string = json.dumps({"index": index, "previous_hash": previous_hash, "timestamp": timestamp, "data": data}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def validate_chain(self):
        """Validate the blockchain."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate the hash of the current block
            if current_block.hash != self.hash_block(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                print(f"Invalid hash at block {current_block.index}")
                return False

            # Validate the previous hash
            if current_block.previous_hash != previous_block.hash:
                print(f"Invalid previous hash at block {current_block.index}")
                return False
        return True
