import hashlib
import json
import os
from datetime import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()
        
    def calculate_hash(self):
        """Calculates the hash of the block's contents."""
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """Proof-of-work algorithm to find a valid hash."""
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def to_dict(self):
        """Returns the block's data as a dictionary."""
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "hash": self.hash
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Block instance from a dictionary."""
        return cls(data['index'], data['timestamp'], data['data'], data['previous_hash'], data['nonce'])

class Blockchain:
    def __init__(self, path, difficulty):
        self.path = path
        self.difficulty = difficulty
        self.chain = self.load_chain()
        if not self.chain:
            # Create genesis block if chain is empty
            genesis_block = Block(0, str(datetime.now()), "Genesis Block", "0")
            genesis_block.mine_block(difficulty)
            self.chain = [genesis_block]
            self.save_chain()

    def add_block(self, data):
        """Add a new block to the chain with the given data."""
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), str(datetime.now()), data, last_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.save_chain()

    def validate_chain(self):
        """Check if the blockchain is valid."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            # Validate hash
            if current.hash != current.calculate_hash():
                return False
            # Validate chain link
            if current.previous_hash != previous.hash:
                return False
        return True

    def save_chain(self):
        """Save the blockchain to the specified path."""
        os.makedirs(self.path, exist_ok=True)
        for block in self.chain:
            block_path = os.path.join(self.path, f"block_{block.index}.json")
            with open(block_path, "w") as file:
                json.dump(block.to_dict(), file)

    def load_chain(self):
        """Load the blockchain from the specified path."""
        chain = []
        if os.path.exists(self.path):
            files = sorted(os.listdir(self.path), key=lambda x: int(x.split('_')[1].split('.')[0]))
            for file_name in files:
                with open(os.path.join(self.path, file_name), "r") as file:
                    block_data = json.load(file)
                    chain.append(Block.from_dict(block_data))
        return chain
if __name__ == "__main__":
    path = "./blockchain_data"
    difficulty = 2  # Adjust the difficulty level
    blockchain = Blockchain(path, difficulty)
    
    # Adding a new block
    user_data = input("Enter data for the new block: ")
    blockchain.add_block(user_data)
    
    # Validating blockchain integrity
    if blockchain.validate_chain():
        print("Blockchain is valid.")
    else:
        print("Blockchain is invalid.")