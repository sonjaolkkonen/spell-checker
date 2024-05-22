class Trie:
    def __init__(self):
        """Class constructor which initializes a new Trie object (now it's a an empty dictionary)
        """
        self.words = {}
    
    def insert(self, word):
        """Inserts words into the trie (currently dictionary).

        Args:
            word (str): The word to be inserted.
        """
        self.words[word] = True

    def keys(self):
        """Returns all the words stored in the trie (currentyly dictionary).

        Returns:
            dict_keys: An iterable view of the dictionary's keys.
        """
        return self.words.keys()
