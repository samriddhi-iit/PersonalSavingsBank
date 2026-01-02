
import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0 
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        
        content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(content.encode()).hexdigest()

    def mine_block(self, difficulty):
       
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"  Block {self.index} mined with hash: {self.hash} ")

class Blockchain:
    def __init__(self):
        self.chain = []
        
        self.difficulty = 2 
        self.create_genesis_block()

    def create_genesis_block(self):
       
        genesis = Block(0, "Genesis Block", "0")
        genesis.mine_block(self.difficulty)
        self.chain.append(genesis)

    def add_block(self, data):
       
        last_block_hash = self.chain[-1].hash
        new_block = Block(len(self.chain), data, last_block_hash)
        
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if current.hash != current.calculate_hash():
                return False

            
            if current.previous_hash != previous.hash:
                return False
        
        return True


my_ledger = Blockchain()

while True:
    print("\n[ 1: Add Transaction | 2: View Blockchain | 3: Quit ]")
    choice = input("What would you like to do? ")

    if choice == '1':
        user_input = input("Enter transaction details: ")
        my_ledger.add_block(user_input)
        print(f"Is the chain still valid? {my_ledger.is_valid()}")

    elif choice == '2':
        print("\n Current Blockchain State ")
        for x in my_ledger.chain:
            print(f"Index: {x.index}")
            
             print(f"Data: {x.data}")
            print(f"Hash: {x.hash}")
            print(f"Prev: {x.previous_hash}")
            print("-" * 40)

    elif choice == '3':
        print("Closing the program")
        break
    
    else:
        print("Invalid choice. Please pick 1, 2, or 3.")
