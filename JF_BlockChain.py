import hashlib
import time
import json
import os

# 🧱 Block class: defines structure and mining process
class Block:
    def __init__(self, index, data, previous_hash, difficulty=3):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.mine_block()

    def mine_block(self):
        target = '0' * self.difficulty
        print(f"\n⛏️ Mining block {self.index} with difficulty {self.difficulty}...")
        start_time = time.time()

        while True:
            block_content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
            block_hash = hashlib.sha256(block_content.encode()).hexdigest()

            if block_hash.startswith(target):
                elapsed = time.time() - start_time
                print(f"✅ Mined in {elapsed:.2f}s | Nonce: {self.nonce} | Hash: {block_hash}")
                return block_hash

            if self.nonce % 10000 == 0:
                print(f"🔄 Trying nonce {self.nonce}...")

            self.nonce += 1

    def to_dict(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "hash": self.hash
        }

# ⛓ Blockchain class: manages chain and file storage
class Blockchain:
    def __init__(self, filename="JFblockchain.json"):
        self.filename = filename
        self.difficulty = 3
        self.chain = self.load_chain()

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0", self.difficulty)

    def load_chain(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                chain_data = json.load(file)
                chain = []
                for block_dict in chain_data:
                    block = Block(
                        block_dict["index"],
                        block_dict["data"],
                        block_dict["previous_hash"],
                        self.difficulty
                    )
                    block.timestamp = block_dict["timestamp"]
                    block.nonce = block_dict["nonce"]
                    block.hash = block_dict["hash"]
                    chain.append(block)
                print(f"📂 Loaded existing blockchain with {len(chain)} blocks.")
                return chain
        else:
            print("🆕 Creating new blockchain...")
            return [self.create_genesis_block()]

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, prev_block.hash, self.difficulty)
        self.chain.append(new_block)
        self.write_chain_to_file()
        self.display_block_ascii(new_block)

    def write_chain_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump([block.to_dict() for block in self.chain], file, indent=4)

    def display_block_ascii(self, block):
        print("\n🧱 Block Confirmed:")
        print(r"""
        .--------.
      .'          '.
     /   BLOCK     \
    |   MINED ✅   |
    |  JF777 Chain |
     \     {}      /
      '.______.'""".format(block.index))
        print(f"🔢 Nonce: {block.nonce}")
        print(f"🔗 Hash: {block.hash}")
        print(f"📦 Data: {block.data}")
        print(f"⏱️ Timestamp: {block.timestamp:.2f}")
        print("-" * 40)

# 🚀 Run the blockchain program interactively
if __name__ == "__main__":
    my_chain = Blockchain()

    while True:
        user_input = input("\n🔹 Enter data to store in blockchain (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("📘 Blockchain saved to JFblockchain.json. Goodbye! 🚀")
            break

        my_chain.add_block(user_input)