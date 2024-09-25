from sortedcontainers import SortedSet

class BBSTSpellChecker:
    def __init__(self):
        self.dictionary = SortedSet()

    def build_dictionary(self, words):
        self.dictionary.update(words)

    def check_word(self, word):
        return word in self.dictionary

    def check_text(self, text):
        return [self.check_word(word) for word in text]
