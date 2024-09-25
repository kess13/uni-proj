class HashMapSpellChecker:
    def __init__(self):
        self.dictionary = {}

    def build_dictionary(self, words):
        self.dictionary = {word: True for word in words}

    def check_word(self, word):
        return self.dictionary.get(word, False)

    def check_text(self, text):
        return [self.check_word(word) for word in text]
