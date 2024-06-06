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

    def suggest(self, word, one_word = False):
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
            distance = self.dl.damerau_levenshtein_distance(word.strip().lower(), vocabulary_word)
            if distance <= 1:
                suggestions.append(vocabulary_word)
                if one_word:
                    return suggestions
        return suggestions
    
    def fix_typos(self, words):
        corrected_words = []
        unable_to_correct = False
        for word in words:
            if len(word) <1 and not self.find_word(word.lower()):
                suggestions = self.suggest(word.lower(), True)
                if suggestions == "Ei kirjoitusvirheitä":
                    corrected_words.append(word)
                    unable_to_correct = True
                else:
                    corrected_words.append[suggestions[0]]

            else:
                corrected_words.append(word)
        
        return corrected_words, unable_to_correct
    
            
