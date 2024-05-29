class TrieNode:
    def __init__(self):
        """class constructor which describes a single node of the trie
        """
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        """Class constructor which initializes a new Trie object
        """
        self.root = TrieNode()
    
    def insert(self, word):
        """Inserts words into the trie

        Args:
            word (str): the word to be inserted
        """
        node = self.root
        for char in word:
            if char not in node.children:
                 node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        """Search for a given word from the trie

        Args:
            word (str): The word to be searched

        Returns:
            bool: True if the word is found, otherwise False
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word
    
    def get_words(self):
        """Get all the words stored in the trie

        Returns:
            list: list of words stored in the trie
        """
        words = []
        self._dfs(self.root, "", words)
        return words
    
    def _dfs(self, node, prefix, words):
        """Depth-first search to collect all words from the trie

        Args:
            node (TrieNode): the current node
            prefix (str): the current prefix of the word
            words (list): the list to collect words
        """
        if node.end_of_word:
            words.append(prefix)
        for char, next_node in node.children.items():
            self._dfs(next_node, prefix + char, words)

    @staticmethod
    def load_words(file_path):
        """Loads words from a file and returns them as a list

        Args:
            file_path (str): Path to the file containing words

        Returns:
            list: a list of words
        """
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
