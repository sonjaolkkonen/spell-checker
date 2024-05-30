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
    
    def test_search_with_empty_string(self):
        self.assertEqual(self.trie.search(""), False)

    def test_search_with_none(self):
        self.assertEqual(self.trie.search(None), False)

    def test_search_with_empty_trie(self):
        trie = Trie()
        self.assertFalse(trie.search("omena"))
        self.assertFalse(trie.search("banaani"))
        self.assertFalse(trie.search(""))

    def test_get_words_with_empty_trie(self):
        trie = Trie()
        result = trie.get_words_with_prefix("")
        self.assertEqual(result, [])

    def test_get_words_with_prefix(self):
        self.assertEqual(self.trie.get_words_with_prefix("kis"), ["kissa"])
        self.assertEqual(self.trie.get_words_with_prefix("k"), ["kissa", "koira"])
        self.assertEqual(self.trie.get_words_with_prefix("lehm"), ["lehmä"])
        self.assertEqual(self.trie.get_words_with_prefix("ap"), ["apina"])
        self.assertEqual(self.trie.get_words_with_prefix("hevo"), ["hevonen"])
    
    def test_get_words_with_empty_prefix(self):
        self.assertEqual(self.trie.get_words_with_prefix(""), ["kissa", "koira", "lehmä", "apina", "hevonen"])

    def test_get_words_with_prefix_does_not_exist(self):
        self.assertEqual(self.trie.get_words_with_prefix("karhu"), [])

        