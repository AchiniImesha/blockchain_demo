import hashlib
import json
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

# --- Create blockchain ---
my_chain = Blockchain()
my_chain.add_block(Block(1, time.time(), "Alice sends 5 BTC to Bob", ""))
my_chain.add_block(Block(2, time.time(), "User123 sends 2 BTC to ShopXYZ", ""))  # Personal data example
my_chain.add_block(Block(3, time.time(), "Charlie sends 1 BTC to Dave", ""))

print("Blockchain valid?", my_chain.is_chain_valid())

# --- Simulate GDPR 'delete' request ---
print("\n[GDPR] Modifying personal data in Block 2...")
my_chain.chain[2].data = "DATA REMOVED PER GDPR REQUEST"
my_chain.chain[2].hash = my_chain.chain[2].calculate_hash()

print("Blockchain valid after GDPR edit?", my_chain.is_chain_valid())

# --- Save blockchain to JSON file ---
output_data = []
for block in my_chain.chain:
    output_data.append({
        "index": block.index,
        "timestamp": block.timestamp,
        "data": block.data,
        "previous_hash": block.previous_hash,
        "hash": block.hash
    })

with open("chain_output.json", "w") as f:
    json.dump(output_data, f, indent=4)

print("\nBlockchain data saved to chain_output.json")
