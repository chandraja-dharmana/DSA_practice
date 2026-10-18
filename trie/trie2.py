# Check Prefix: Insert ["apple", "application", "banana"] and
# check whether any word starts with "app"

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

            #important
            current = current.children[char]

        current.is_end = True

    # Search for a prefix
    def search_prefix(self, prefix):
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]

        return True   #only change

# Create Trie
trie = Trie()

# Insert words
trie.insert("apple")
trie.insert("application")
trie.insert("banana")

# Search word by word
if trie.search_prefix("app"):
    print("Found")
else:
    print("Not Found")