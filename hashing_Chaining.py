# ----------------------------
# Hash Table with Chaining
# ----------------------------

class Node:
    """Node for linked list used in chaining."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size
        self.count = 0  # Number of elements in the table

    def hash_function(self, key):
        """A simple hash function using modulo."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self.hash_function(key)
        new_node = Node(key, value)

        # Insert at head of linked list (chaining)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.count += 1

    def search(self, key):
        """Search for a key in the hash table and return its value."""
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None  # Key not found

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.count -= 1
                return True  # Successfully deleted
            prev = current
            current = current.next
        return False  # Key not found

    def display(self):
        """Display the hash table contents."""
        for i, node in enumerate(self.table):
            chain = []
            current = node
            while current:
                chain.append(f"({current.key}: {current.value})")
                current = current.next
            print(f"Slot {i}: {' -> '.join(chain)}")

# ----------------------------
# Test the Hash Table
# ----------------------------
if __name__ == "__main__":
    ht = HashTable(size=7)  # Small size to see collisions easily

    # Insert key-value pairs
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("grape", 30)
    ht.insert("orange", 40)
    ht.insert("mango", 50)

    print("Hash Table after insertions:")
    ht.display()

    # Search for keys
    print("\nSearch for 'banana':", ht.search("banana"))
    print("Search for 'cherry':", ht.search("cherry"))

    # Delete a key
    ht.delete("grape")
    print("\nHash Table after deleting 'grape':")
    ht.display()
