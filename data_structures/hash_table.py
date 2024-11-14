class HashTable:
    def __init__(self, capacity=10):
        # Initialize the hash table with given capacity
        self.capacity = capacity
        self.table = [[] for _ in range(self.capacity)]  # Create an array of empty lists

    def _hash_function(self, key):
        # Hash function 
        return sum(ord(char) for char in key) % self.capacity

    def insert(self, key, value):
        index = self._hash_function(key)
        # Check if key already exists in the chain
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value  # Update the value if key is found
                return
        self.table[index].append([key, value])  # Insert as a new item in the chain

    def search(self, key):
        index = self._hash_function(key)
        # Search through the chain to find the key
        for item in self.table[index]:
            if item[0] == key:
                return item[1]  # Return the value if key is found
        return None  # Return None if key is not found

    def delete(self, key):
        index = self._hash_function(key)
        # Traverse the chain to find and remove the key
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]  # Remove the item from the chain
                return
        print("Key not found!")

    def display(self):
        # Display the hash table
        for i, chain in enumerate(self.table):
            if chain:
                print(f"Bucket {i}: {chain}")
            else:
                print(f"Bucket {i}: Empty")


if __name__ == "__main__":
    ht = HashTable()

    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("grapes", 30)
    ht.insert("melon", 40)
    
    ht.display()

    print("\nSearch for 'apple':", ht.search("apple"))
    print("Search for 'orange':", ht.search("orange"))

    ht.delete("banana")
    ht.display()

    ht.delete("orange")  # Key not found
