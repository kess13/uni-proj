import time
import json
import matplotlib.pyplot as plt
import pandas as pd
from brute_force import brute_force_pattern_matching
from sunday import original_sunday_algorithm
from KMP import kmp_search
from FSM import fsm_search
from RabinKarp import rabin_karp_search
from Gusfield_Z import gusfield_z_search

small_pattern = "pattern and the text"
large_pattern = "This is a very large pattern meant to test the efficiency of the pattern matching algorithms over a large pattern embedded within the text.n number interface recursive ponens number conquer tokenization perceptron theorem simile random lexical hyperparameter bagging dependency bert tagging networks support models audio affirmation tu simile brute Warshall force consonance search placebo recognition matching developer hasty affirmation video heap bias graph selection bagging dropout machines informal proof modal onomatopoeia bandwagon generation self biconditional document epizeuxis memoization matrix map vertex hash grid causation zeugma optimization tautology glove LSTM GloVe algorithms random ensemble coding testing array conjunction summarization image enthymeme"


def measure_time(search_func, text, pattern, iterations=100):
    total_time = 0.0
    for _ in range(iterations):
        start_time = time.time()
        result = search_func(text, pattern)
        end_time = time.time()

        elapsed_time = end_time - start_time
        total_time += elapsed_time

    average_time = total_time / iterations
    return average_time

# Text lengths to test
text_lengths = [100, 200, 500, 750, 1000, 2000, 5000, 10000, 20000, 50000, 100000]

# Collecting results
results = {'algorithm': [], 'pattern': [], 'length': [], 'time': []}

# Algorithms to test
algorithms = {
    'Brute Force': brute_force_pattern_matching,
    'Sunday': original_sunday_algorithm,
    'KMP': kmp_search,
    'FSM': fsm_search,
    'Rabin-Karp': rabin_karp_search,
    'Gusfield Z': gusfield_z_search
}

# Load generated texts from the JSON files
with open('generated_texts_with_small_pattern.json', 'r') as f:
    texts_with_small_pattern = json.load(f)

with open('generated_texts_with_large_pattern.json', 'r') as f:
    texts_with_large_pattern = json.load(f)

# Number of iterations for averaging
iterations = 100

# Testing with different text lengths and patterns
for length in text_lengths:
    text_small = texts_with_small_pattern[str(length)]  # Convert length to string as JSON keys are strings
    text_large = texts_with_large_pattern[str(length)]  # Convert length to string as JSON keys are strings

    for name, func in algorithms.items():
        # Test with small pattern
        elapsed_time = measure_time(func, text_small, small_pattern, iterations)
        results['algorithm'].append(name)
        results['pattern'].append('small')
        results['length'].append(length)
        results['time'].append(elapsed_time)

        # Test with large pattern
        elapsed_time = measure_time(func, text_large, large_pattern, iterations)
        results['algorithm'].append(name)
        results['pattern'].append('large')
        results['length'].append(length)
        results['time'].append(elapsed_time)

# Convert results to DataFrame for easier manipulation
df = pd.DataFrame(results)

# Plotting results
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 6), sharex=True)

for i, pattern_size in enumerate(['small', 'large']):
    for algorithm in algorithms.keys():
        lengths = df[(df['pattern'] == pattern_size) & (df['algorithm'] == algorithm)]['length']
        times = df[(df['pattern'] == pattern_size) & (df['algorithm'] == algorithm)]['time']
        axes[i].plot(lengths, times, marker='o', label=f'{algorithm}')

    axes[i].set_ylabel('Time (seconds)')
    axes[i].set_title(f'Pattern Matching Algorithms Performance ({pattern_size.capitalize()} Patterns)')
    axes[i].legend()
    axes[i].grid(True)

plt.xlabel('Text Length')
plt.tight_layout()
plt.show()
