import unittest
from unittest.mock import Mock
from services.spell_checker import SpellChecker
from services.trie import Trie
from services.damerau_levenshtein import DamerauLevenshtein

class TestSpellChecker(unittest.TestCase):
    def setUp(self):
        self.create_test_file()
        self.trie_mock = Mock(wraps=Trie())
        self.dl_mock = Mock(wraps=DamerauLevenshtein())
        self.spell_checker = SpellChecker("src/data/test_words.txt", self.trie_mock, self.dl_mock)

    def create_test_file(self):
        with open("src/data/test_words.txt", "w") as file:
            file.write("aalto\naaltoallas\naamu\nahven\naikakone\nlihas\nlihota\n")

    def test_suggest_with_no_typo(self):
        suggestions = self.spell_checker.suggest("aamu")
        self.dl_mock.damerau_levenshtein_distance.assert_not_called()
        self.assertEqual(suggestions, "Ei kirjoitusvirheitä")

    def test_suggest_with_empty_input(self):
        suggestions = self.spell_checker.suggest("")
        self.dl_mock.damerau_levenshtein_distance.assert_not_called()
        self.assertEqual(suggestions, "Anna sana")
    
    # def test_suggest_with_numeric_input(self):
    #     self.spell_checker.suggest("123")
    #     self.dl_mock.damerau_levenshtein_distance.assert_not_called()

    def test_suggest(self):
        self.spell_checker.suggest("ajkakone")
        self.dl_mock.damerau_levenshtein_distance.assert_called()
        
    def test_find_word_with_word_in_trie(self):
        self.spell_checker.find_word("ahven")
        self.trie_mock.search.assert_called()

    def test_find_word_with_numeric(self):
        self.spell_checker.find_word("123")
        self.trie_mock.assert_not_called()

    def test_fix_typos(self):
        self.assertEqual(self.spell_checker.fix_typos(["amu", "lihass"])[0], ["aamu", "lihas"])
        self.assertEqual(self.spell_checker.fix_typos(["alto", "aaltoalkas", "lihoota"])[0], ["aalto", "aaltoallas", "lihota"])
        self.assertEqual(self.spell_checker.fix_typos(["ahven", "ja", "kuha"])[0], ["ahven", "ja", "kuha"])

    def test_fix_typos_with_empty_list(self):
        self.assertEqual(self.spell_checker.fix_typos([])[0], [])
    
    def test_parse_text(self):
        self.assertEqual(self.spell_checker.parse_text("aalto meri"), ["aalto", "meri"])
        self.assertEqual(self.spell_checker.parse_text("aalto laiva meri"), ["aalto", "laiva", "meri"])

    def test_parse_empty_string(self):
        self.assertEqual(self.spell_checker.parse_text(""), [])

    def test_return_into_text(self):
        self.assertEqual(self.spell_checker.return_into_text(["aalto", "laiva", "meri"]), "aalto laiva meri")

    def test_return_into_text_empty_list(self):
        self.assertEqual(self.spell_checker.return_into_text([]), "")

    def test_add_word_with_none(self):
        self.assertFalse(self.spell_checker.add_word(None))

    def test_add_word(self):
        self.assertTrue(self.spell_checker.add_word("lahja"))
        self.trie_mock.insert.assert_called_with("lahja")

    def test_add_existing_word(self):
        self.assertFalse(self.spell_checker.add_word("ahven"))


