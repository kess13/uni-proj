class LinearListSpellChecker:
    def __init__(self):
        self.dictionary = []

    def build_dictionary(self, words):
        self.dictionary = words

    def check_word(self, word):
        return word in self.dictionary

    def check_text(self, text):
        return [self.check_word(word) for word in text]
