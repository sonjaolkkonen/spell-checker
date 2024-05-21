class Trie:
    def __init__(self):
        self.words = {}
    
    def insert(self, word):
        self.words[word] = True

    def keys(self):
        return self.words.keys()
