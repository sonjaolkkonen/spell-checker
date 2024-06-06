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
        """Saves words from the file into trie
        """
        words = self.trie.load_words(os.path.join(dirname, "../", "data", "words.txt"))
        for word in words:
            self.trie.insert(word.lower())

    def find_word(self, word):
        """Finds the word from trie

        Args:
            word (str): the word to be searched

        Returns:
            bool: True, if the word is found, False if not
        """
        for char in word:
            if char.isnumeric():
                return False
        return self.trie.search(word.lower())

    def suggest(self, word, one_word = False):
        """Suggests the closest word from the trie to the given word

        Args:
            word (str): the word for which to find the closest match
            one_word(bool): boolean value which determines if the method returns one or more words

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
            distance = self.dl.damerau_levenshtein_distance(word.strip().lower(), vocabulary_word)
            if distance <= 1:
                suggestions.append(vocabulary_word)
                if one_word:
                    return suggestions
        return suggestions

    def fix_typos(self, words):
        """Fixes typos in the text

        Args:
            words (list): a list of words

        Returns:
            list: list of fixed words
        """
        corrected_words = []
        for word in words:
            if len(word) > 1 and not self.find_word(word.lower()):
                suggestions = self.suggest(word.lower(), True)
                if suggestions == "Ei kirjoitusvirheitä":
                    corrected_words.append(word)
                else:
                    corrected_words.append(suggestions[0])

            else:
                corrected_words.append(word)

        return corrected_words

    def parse_text(self, text):
        """Splits text into separated words

        Args:
            text (str): the text which needs to be parsed

        Returns:
            list: list of parsed words
        """
        return text.split()

    def return_into_text(self, words):
        """Returns words into coherent text

        Args:
            words (list): list of words which needs to be combined

        Returns:
            str: combined text
        """
        return " ".join(words)
