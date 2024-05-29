import os
from services.trie import Trie
from services.damerau_levenshtein import DamerauLevenshtein

dirname = os.path.dirname(__file__)

class SpellChecker():
    def __init__(self):
        """Class constructor which creates a new DamerauLevenshtein object
        """
        self.trie = Trie()
        self.dl = DamerauLevenshtein()
        self.words = Trie.load_words(os.path.join(dirname, "../", "data", "words.txt"))
        for word in self.words:
            self.trie.insert(word)

    def suggest(self, word):
        """Suggest the closest word from the dictionary to the given word

        Args:
            word (str): the word for which to find the closest match

        Returns:
            str: the closest matching word from the trie (currently dictionary)
        """

        if self.trie.search(word):
            return "Ei kirjoitusvirheitä"

        suggestions = []
        candidates = self.trie.get_words_with_prefix(word[0])
        for candidate in candidates:
            distance = self.dl.damerau_levenshtein_distance(word, candidate)
            if distance <= 1:
                suggestions.append(candidate)
        return suggestions
