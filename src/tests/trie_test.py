import unittest
from services.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.insert("aalto")
        self.trie.insert("aaltoallas")
        self.trie.insert("aamu")
        self.trie.insert("ahven")
        self.trie.insert("aikakone")
        self.trie.insert("lihas")
        self.trie.insert("lihota")

    def test_insert(self):
        self.assertTrue(self.trie.search("aalto"))
        self.assertTrue(self.trie.search("aaltoallas"))
        self.assertTrue(self.trie.search("aamu"))
        self.assertTrue(self.trie.search("ahven"))
        self.assertTrue(self.trie.search("aikakone"))
        self.assertTrue(self.trie.search("lihas"))
        self.assertTrue(self.trie.search("lihota"))

    def test_insert_with_none(self):
        self.trie.insert(None)
        self.assertFalse(self.trie.search(None))
    
    def test_search_with_word_in_trie(self):
        self.assertTrue(self.trie.search("aalto"))

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

    def test_get_trie_content(self):
        content = self.trie.get_trie_content()
        self.assertEqual(content, ["aalto", "aaltoallas", "aamu", "ahven", "aikakone", "lihas", "lihota"])

    def test_get_trie_content_with_empty_trie(self):
        trie = Trie()
        content = trie.get_trie_content()
        self.assertEqual(content, [])
