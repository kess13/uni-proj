class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class TrieSpellChecker:
    def __init__(self):
        self.root = TrieNode()

    def build_dictionary(self, words):
        for word in words:
            self._insert(word)

    def _insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def check_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def check_text(self, text):
        return [self.check_word(word) for word in text]
