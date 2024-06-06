import os
from services.trie import Trie
from services.damerau_levenshtein import DamerauLevenshtein

dirname = os.path.dirname(__file__)

class SpellChecker():
    def __init__(self):
        """Class constructor which creates a new SpellChecker object
        """
        self.trie = Trie()
        self.dl = DamerauLevenshtein()
        self.create_vocabulary()

    def create_vocabulary(self):
        words = self.trie.load_words(os.path.join(dirname, "../", "data", "words.txt"))
        for word in words:
            self.trie.insert(word.lower())

    def find_word(self, word):
        for char in word:
            if char.isnumeric():
                return False
        return self.trie.search(word.lower())

    def suggest(self, word):
        """Suggest the closest word from the trie to the given word

        Args:
            word (str): the word for which to find the closest match

        Returns:
            list: the closest matching words from the trie
        """

        if not word:
            return "Anna sana"

        if self.trie.search(word):
            return "Ei kirjoitusvirheitä"

        vocabulary = self.trie.get_trie_content()
        suggestions = []
        for vocabulary_word in vocabulary:
            distance = self.dl.damerau_levenshtein_distance(word, vocabulary_word)
            if distance <= 1:
                suggestions.append(vocabulary_word)
        return suggestions
    
    def suggest_text(self, text):
        """Suggest closest word from the trie to all the owrds of the given text

        Args:
            text (str): the words for which to find the closest match

        Returns:
            dict: the closest matching words for each word from the trie
        """
        words = text.split()
        suggestions = {}
        for word in words:
            suggestion = self.suggest(word)
            if suggestion != "Ei kirjoitusvirheitä":
                suggestions[word] = suggestion
        if not suggestions:
            return "Ei kirjoitusvirheitä"
        return suggestions
