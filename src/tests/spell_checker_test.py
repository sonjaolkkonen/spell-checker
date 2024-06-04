import unittest
from services.spell_checker import SpellChecker
from services.trie import Trie
from services.damerau_levenshtein import DamerauLevenshtein

class TestSpellChecker(unittest.TestCase):
    def setUp(self):
        self.spell_checker = SpellChecker()
        self.spell_checker.trie = Trie()
        self.spell_checker.dl = DamerauLevenshtein()
        words = ["omena", "banaani", "appelsiini"]
        for word in words:
            self.spell_checker.trie.insert(word)

    def test_no_typo(self):
        self.assertEqual(self.spell_checker.suggest("omena"), "Ei kirjoitusvirheitä")

    def test_empty_input(self):
        self.assertEqual(self.spell_checker.suggest(""), "Anna sana")

    def test_single_typo(self):
        self.assertIn("omena", self.spell_checker.suggest("omen"))

    def test_insertion(self):
        self.assertIn("appelsiini", self.spell_checker.suggest("apelsiini"))

    def test_deletion(self):
        self.assertIn("banaani", self.spell_checker.suggest("baanaani"))

    def test_transposition(self):
        self.assertIn("omena", self.spell_checker.suggest("omean"))

    def test_no_suggestions(self):
        self.assertEqual(self.spell_checker.suggest("kakku"), [])

    def test_no_typo_in_sentence(self):
        self.assertEqual(self.spell_checker.suggest_text("omena appelsiini banaani"), "Ei kirjoitusvirheitä")

    def test_typo_in_one_word(self):
        self.assertEqual(self.spell_checker.suggest_text("omen appelsiini banaani"), {"omen": ["omena"]})

    def test_typo_in_two_words(self):
        self.assertEqual(self.spell_checker.suggest_text("banani apelsiini omena"), {"banani":["banaani"], "apelsiini":["appelsiini"]})
