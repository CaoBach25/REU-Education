import hashlib
import time
import os

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(value.encode()).hexdigest()

    def save_to_file(self):
        filename = f"block_{self.index}.txt"
        with open(filename, "w") as file:
            file.write(f"Index: {self.index}\n")
            file.write(f"Timestamp: {self.timestamp}\n")
            file.write(f"Data: {self.data}\n")
            file.write(f"Previous Hash: {self.previous_hash}\n")
            file.write(f"Hash: {self.hash}\n")

def create_genesis_block():
    return Block(0, "0", "Genesis Block")

def add_block(previous_block, data):
    index = previous_block.index + 1
    new_block = Block(index, previous_block.hash, data)
    new_block.save_to_file()
    return new_block

blockchain = [create_genesis_block()]
blockchain[0].save_to_file()

# Tạo thêm các block
for i in range(1, 5):
    data = f"Block {i} data"
    new_block = add_block(blockchain[-1], data)
    blockchain.append(new_block)
def is_chain_valid():
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]
        
        # Kiểm tra mã băm của block
        if current_block.hash != current_block.calculate_hash():
            return False
        # Kiểm tra mã băm của block trước
        if current_block.previous_hash != previous_block.hash:
            return False
    return True
def hack_block(index, new_data):
    filename = f"block_{index}.txt"
    with open(filename, "r") as file:
        lines = file.readlines()

    # Thay đổi dữ liệu của block
    lines[2] = f"Data: {new_data}\n"

    # Ghi đè file với dữ liệu mới
    with open(filename, "w") as file:
        file.writelines(lines)
# Hack vào dữ liệu của block 2
hack_block(2, "Hacked Data")

# Kiểm tra tính hợp lệ của blockchain
if is_chain_valid():
    print("Blockchain is valid.")
else:
    print("Blockchain is invalid!")