import unittest
from services.damerau_levenshtein import DamerauLevenshtein

class TestDamerauLevenshtein(unittest.TestCase):
    def setUp(self):
        self.dl = DamerauLevenshtein()

    def test_same_words(self):
        word = "kissa"
        distance = self.dl.damerau_levenshtein_distance(word, word)
        self.assertEqual(distance, 0)

    def test_empty_strings(self):
        word1 = ""
        word2 = ""
        distance = self.dl.damerau_levenshtein_distance(word1, word2)
        self.assertEqual(distance, 0)

    def test_different_words(self):
        word1 = "kissa"
        word2 = "koira"
        distance = self.dl.damerau_levenshtein_distance(word1, word2)
        self.assertEqual(distance, 3)

    def test_one_empty_string(self):
        word1 = "kissa"
        word2 = ""
        distance = self.dl.damerau_levenshtein_distance(word1, word2)
        self.assertEqual(distance, len(word1))
