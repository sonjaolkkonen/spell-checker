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
        if not word:
            return False
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

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

    def get_words_with_prefix(self, prefix):
        """Get all the words with the given prefix

        Args:
            prefix (str): prefix of the given word

        Returns:
            list: list of words that start with the given prefix
        """
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return []
            current = current.children[letter]

        words = []
        self._dfs(current, prefix, words)
        return words

    @staticmethod
    def load_words(file_path):
        """Loads words from a file and returns them as a list

        Args:
            file_path (str): Path to the file containing words

        Returns:
            list: a list of words
        """
        with open(file_path, 'r', encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
