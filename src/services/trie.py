class TrieNode:
    def __init__(self, char):
        """class constructor which describes a single node of the trie

        Args: char (str): the character of the node
        """
        self.children = {}
        self.end_of_word = False
        self.char = char

class Trie:
    def __init__(self):
        """Class constructor which initializes a new Trie object
        """
        self.root = TrieNode("")
        self.content = []

    def insert(self, word):
        """Inserts words into the trie

        Args:
            word (str): the word to be inserted
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        """Searchs for a given word from the trie

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

    def _dfs(self, node, prev):
        """Depth-first search to collect all words from the trie

        Args:
            node (TrieNode): the current node
            prev (str): previous letter
        """
        if node.end_of_word:
            self.content.append(prev + node.char)

        for child in node.children.values():
            self._dfs(child, prev + node.char)


    def get_trie_content(self):
        """Returns content of the trie

        Returns:
            list: content of the trie
        """
        self._dfs(self.root, "")
        return self.content

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
