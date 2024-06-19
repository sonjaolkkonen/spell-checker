import unittest
from services.damerau_levenshtein import DamerauLevenshtein

class TestDamerauLevenshtein(unittest.TestCase):
    def setUp(self):
        self.dl = DamerauLevenshtein()
        self.word1 = "aalto"
        self.word2 = "aaltoallas"

    def test_same_words(self):
        distance = self.dl.damerau_levenshtein_distance(self.word1, self.word1)
        self.assertEqual(distance, 0)

    def test_empty_strings(self):
        distance = self.dl.damerau_levenshtein_distance("", "")
        self.assertEqual(distance, 0)

    def test_different_words(self):
        distance = self.dl.damerau_levenshtein_distance(self.word1, self.word2)
        self.assertEqual(distance, 5)

    def test_one_empty_string(self):
        self.assertEqual(self.dl.damerau_levenshtein_distance(self.word2, ""), len(self.word2))
        self.assertEqual(self.dl.damerau_levenshtein_distance("", self.word2), len(self.word2))
