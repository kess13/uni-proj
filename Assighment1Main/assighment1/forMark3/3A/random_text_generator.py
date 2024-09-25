import random

def generate_random_text(length, seed=None, include_pattern=None):
    if seed is not None:
        random.seed(seed)

    words = [
        "example", "text", "random", "words", "generated", "for", "testing", "pattern", "matching", "algorithms",
        "learning", "classification", "clustering", "regression", "dimensionality",
        "reduction", "overfitting", "underfitting", "bias", "variance", "ensemble", "methods", "boosting", "bagging",
        "random", "forest", "gradient", "boosting", "support", "vector", "machines", "k-nearest", "neighbors",
        "logistic", "regression", "cross-validation", "training", "testing", "validation", "hyperparameter", "grid",
        "search", "dropout", "regularization", "convolutional", "recurrent", "architectures", "sequence", "models",
        "attention", "mechanism", "transformers", "embeddings", "word2vec", "glove", "bert", "fasttext","programming", 
        "developer", "coding", "software", "engineering", "algorithm", "logic", "iteration",
        "recursive", "iterative", "loop", "conditional", "branching", "variable", "function", "module", "library",
        "framework", "API", "interface", "object", "class", "method", "attribute", "inheritance", "polymorphism",
        "encapsulation", "abstraction", "data", "structure", "array", "list", "stack", "queue", "heap", "tree",
        "graph", "hash", "map", "dictionary", "set", "tuple", "linked", "list", "doubly", "singly", "circular",
        "pointer", "node", "leaf", "edge", "vertex", "algorithm", "sort", "search", "insertion", "merge", "quick",
        "bubble", "selection", "linear", "binary", "depth", "breadth", "first", "DFS", "BFS", "dynamic", "greedy",
        "divide", "conquer", "backtracking", "brute", "force", "heuristic", "optimization", "dynamic", "programming",
        "memoization", "tabulation", "recursion", "iteration", "mathematics", "calculus", "geometry", "algebra",
        "statistics", "probability", "matrix", "vector", "tensor", "trigonometry", "discrete", "continuous",
        "theorem", "proof", "number", "theory", "set", "theory", "logic", "propositional", "predicate", "modal",
        "quantum", "combinatorics", "permutation", "combination", "graph", "theory", "graphical", "representation",
        "adjacency", "matrix", "adjacency", "list", "incidence", "matrix", "graph", "traversal", "DFS", "BFS",
        "Dijkstra", "Floyd", "Warshall", "Prim", "Kruskal", "Bellman", "Ford", "A*", "machine", "learning",
        "supervised", "unsupervised", "semi-supervised", "reinforcement", "learning", "classification",
        "regression", "clustering", "dimensionality", "reduction", "feature", "extraction", "selection", "ensemble",
        "learning", "bagging", "boosting", "random", "forest", "gradient", "boosted", "machines", "support", "vector",
        "machines", "kernel", "methods", "neural", "networks", "perceptron", "multilayer", "convolutional", "recurrent",
        "LSTM", "GRU", "attention", "mechanism", "transformer", "embeddings", "word", "sentence", "document", "sequence",
        "generation", "translation", "summarization", "image", "video", "audio", "processing", "natural", "language",
        "understanding", "generation", "translation", "summarization", "speech", "recognition", "text", "synthesis",
        "sentiment", "analysis", "emotion", "detection", "topic", "modeling", "named", "entity", "recognition",
        "part", "of", "speech", "tagging", "dependency", "parsing", "chunking", "stemming", "lemmatization",
        "tokenization", "stopword", "removal", "vectorization", "tf-idf", "word2vec", "GloVe", "fastText",
        "BERT", "ELMo", "GPT", "semantic", "syntactic", "morphological", "phonological", "lexical", "pragmatic",
        "discourse", "sentiment", "stance", "style", "irony", "sarcasm", "metaphor", "simile", "hyperbole",
        "litotes", "rhetorical", "question", "repetition", "alliteration", "assonance", "consonance", "onomatopoeia",
        "euphemism", "oxymoron", "hyperbaton", "ellipsis", "anaphora", "epistrophe", "antithesis", "chiasmus",
        "zeugma", "catachresis", "malapropism", "pun", "adynaton", "syllepsis", "tmesis", "paraprosdokian", "aporia",
        "isocolon", "epizeuxis", "antanaclasis", "synecdoche", "metonymy", "cliché", "climax", "anticlimax", "homoioteleuton",
        "chiasmus", "anadiplosis", "epanalepsis", "epistrophe", "asyndeton", "polysyndeton", "tricolon", "antimetabole",
        "conjunction", "disjunction", "negation", "affirmation", "implication", "converse", "contrapositive",
        "inverse", "biconditional", "tautology", "contradiction", "contingency", "validity", "soundness", "modus", "ponens",
        "modus", "tollens", "syllogism", "enthymeme", "valid", "argument", "inductive", "deductive", "abductive",
        "informal", "fallacy", "straw", "man", "slippery", "slope", "ad", "hominem", "tu", "quoque", "bandwagon",
        "confirmation", "bias", "falsifiability", "post", "hoc", "ergo", "propter", "hoc", "hasty", "generalization",
        "correlation", "causation", "sampling", "selection", "survivorship", "regression", "self", "selection",
        "observer", "effect", "hawthorne", "effect", "placebo", "effect", "response", "bias", "non-response", "bias",
        "volunteer", "bias", "confirmation", "bias", "response", "bias", "demand", "characteristic"
    ]

    if include_pattern is not None:
        pattern_length = len(include_pattern)
    else:
        pattern_length = 0

    max_length = length - pattern_length

    text = []
    current_length = 0
    max_word_length = max(len(word) for word in words)

    while current_length + max_word_length + 1 < max_length:
        word = random.choice(words)
        if current_length + len(word) + 1 <= max_length:
            text.append(word)
            current_length += len(word) + 1
        else:
            break

    generated_text = ' '.join(text)

    if include_pattern is not None:
        insertion_point = random.randint(0, len(generated_text))
        generated_text = generated_text[:insertion_point] + include_pattern + generated_text[insertion_point:]

    return generated_text[:length]
