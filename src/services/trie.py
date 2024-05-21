import pygtrie

class Trie:
    def __init__(self):
        self.trie = pygtrie.CharTrie()
    
    def insert(self, word):
        self.trie[word] = True

    def keys(self):
        return self.trie.keys()

