# Search Word: Insert ["apple", "app", "bat"] into 
# a Trie and check whether "app" exists.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def __repr__(self):
        return f"TrieNode(children={self.children.keys()}, is_end={self.is_end})"

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word
    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            #important
            current = current.children[char]

        current.is_end = True

    # Search for a complete word
    def search(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        return current.is_end


# Create Trie
trie = Trie()

# Insert words
trie.insert("apple")
trie.insert("app")
trie.insert("bat")

print(trie.root)

# Search
if trie.search("app"):
    print("Found")
else:
    print("Not Found")