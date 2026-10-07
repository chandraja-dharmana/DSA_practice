class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word
    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

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

# Search
if trie.search("app"):
    print("Found")
else:
    print("Not Found")