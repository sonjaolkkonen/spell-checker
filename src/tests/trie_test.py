import unittest
from services.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.insert("kissa")
        self.trie.insert("koira")
        self.trie.insert("lehmä")
        self.trie.insert("apina")
        self.trie.insert("hevonen")
    
    def test_insert(self):
        self.assertTrue(self.trie.search("kissa"))
        self.assertTrue(self.trie.search("koira"))
        self.assertTrue(self.trie.search("lehmä"))
        self.assertTrue(self.trie.search("apina"))
        self.assertTrue(self.trie.search("hevonen"))
    
    def test_search_with_word_in_trie(self):
        self.assertTrue(self.trie.search("kissa"))

    def test_search_with_word_not_in_trie(self):
        self.assertFalse(self.trie.search("maito"))

    def test_get_words(self):
        words = self.trie.get_words()
        expected_words = ["kissa", "koira", "lehmä", "apina", "hevonen"]
        self.assertCountEqual(words, expected_words)