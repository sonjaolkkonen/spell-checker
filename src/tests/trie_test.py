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
    