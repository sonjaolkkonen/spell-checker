import unittest
from services.spell_checker import SpellChecker
from services.trie import Trie
from services.damerau_levenshtein import DamerauLevenshtein

class TestSpellChecker(unittest.TestCase):
    def setUp(self):
        self.spell_checker = SpellChecker()
        self.spell_checker.trie = Trie()
        self.spell_checker.dl = DamerauLevenshtein()
        words = ["apple", "app", "appreciate", "book", "bad", "bear", "bat"]
        for word in words:
            self.spell_checker.trie.insert(word)

    def test_suggest_with_no_typo(self):
        self.assertEqual(self.spell_checker.suggest("apple"), "Ei kirjoitusvirheitä")

    def test_suggest_with_empty_input(self):
        self.assertEqual(self.spell_checker.suggest(""), "Anna sana")
    
    def test_suggest_with_numeric_input(self):
        self.assertFalse(self.spell_checker.suggest("123"))

    def test_suggest_single_typo(self):
        self.assertIn("appreciate", self.spell_checker.suggest("apreciate"))

    def test_suggest_with_word_not_in_trie(self):
        self.assertEqual(self.spell_checker.suggest("application"), [])

    def test_find_word_with_word_in_trie(self):
        self.assertTrue(self.spell_checker.find_word("app"))

    def test_find_word_with_word_not_in_trie(self):
        self.assertFalse(self.spell_checker.find_word("battery"))

    def test_find_word_with_numeric(self):
        self.assertFalse(self.spell_checker.find_word("123"))

    def test_fix_typos_no_typo(self):
        self.assertEqual(self.spell_checker.fix_typos(["apple", "book", "bat"]), ["apple", "book", "bat"])

    def test_fix_typos_with_typos(self):
        self.assertEqual(self.spell_checker.fix_typos(["applle", "boot", "apreciate"]), ["apple", "book", "appreciate"])

    def test_fix_typos_with_empty_list(self):
        self.assertEqual(self.spell_checker.fix_typos([]), [])
    
    def test_parse_text(self):
        self.assertEqual(self.spell_checker.parse_text("apple book appreciate"), ["apple", "book", "appreciate"])

    def test_parse_empty_string(self):
        self.assertEqual(self.spell_checker.parse_text(""), [])

    def test_return_into_text(self):
        self.assertEqual(self.spell_checker.return_into_text(["apple", "book", "appreciate"]), "apple book appreciate")

    def test_return_into_text_empty_list(self):
        self.assertEqual(self.spell_checker.return_into_text([]), "")

