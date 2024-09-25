import json
import random
from random_text_generator import generate_random_text

# Define small and large patterns
small_pattern = "pattern and the text"
large_pattern = "This is a very large pattern meant to test the efficiency of the pattern matching algorithms over a large pattern embedded within the text.n number interface recursive ponens number conquer tokenization perceptron theorem simile random lexical hyperparameter bagging dependency bert tagging networks support models audio affirmation tu simile brute Warshall force consonance search placebo recognition matching developer hasty affirmation video heap bias graph selection bagging dropout machines informal proof modal onomatopoeia bandwagon generation self biconditional document epizeuxis memoization matrix map vertex hash grid causation zeugma optimization tautology glove LSTM GloVe algorithms random ensemble coding testing array conjunction summarization image enthymeme"

# Seed for reproducibility
seed = 42  

# Define text lengths
text_lengths = [100, 200, 500, 750, 1000, 2000, 5000, 10000, 20000, 50000, 100000]

# Generate texts with small pattern
texts_with_small_pattern = {}
for length in text_lengths:
    random.seed(seed)  
    texts_with_small_pattern[length] = generate_random_text(length, seed, small_pattern)

# Generate texts with large pattern
texts_with_large_pattern = {}
for length in text_lengths:
    random.seed(seed)  
    texts_with_large_pattern[length] = generate_random_text(length, seed, large_pattern)

# Save the generated texts to JSON files
with open('generated_texts_with_small_pattern.json', 'w') as f:
    json.dump(texts_with_small_pattern, f)

with open('generated_texts_with_large_pattern.json', 'w') as f:
    json.dump(texts_with_large_pattern, f)
