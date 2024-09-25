import time
import matplotlib.pyplot as plt
from linear_list_spell_checker import LinearListSpellChecker
from bbst_spell_checker import BBSTSpellChecker
from trie_spell_checker import TrieSpellChecker
from hash_map_spell_checker import HashMapSpellChecker

def load_words(file_path):
    with open(file_path, 'r') as file:
        return file.read().split()

def benchmark(spell_checker, dictionary, text):
    start_time = time.time()
    spell_checker.build_dictionary(dictionary)
    build_time = time.time() - start_time

    start_time = time.time()
    spell_checker.check_text(text)
    check_time = time.time() - start_time

    return build_time, check_time

def main():
    dictionary_file = 'english_words.txt'
    text_file = 'large_text.txt'

    dictionary = load_words(dictionary_file)
    text = load_words(text_file)

    spell_checkers = [
        ('Linear List', LinearListSpellChecker()),
        ('BBST', BBSTSpellChecker()),
        ('Trie', TrieSpellChecker()),
        ('Hash Map', HashMapSpellChecker())
    ]

    build_times = []
    check_times = []
    labels = []

    for name, checker in spell_checkers:
        build_time, check_time = benchmark(checker, dictionary, text)
        build_times.append(build_time)
        check_times.append(check_time)
        labels.append(name)
        print(f"{name} - Build time: {build_time:.4f}s, Check time: {check_time:.4f}s")

    x = range(len(labels))

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.bar(x, build_times, tick_label=labels)
    plt.ylabel('Time (s)')
    plt.title('Dictionary Build Time')

    plt.subplot(1, 2, 2)
    plt.bar(x, check_times, tick_label=labels)
    plt.ylabel('Time (s)')
    plt.title('Text Check Time')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
