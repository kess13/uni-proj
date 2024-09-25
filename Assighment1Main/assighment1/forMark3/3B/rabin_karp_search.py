def rabin_karp_search(text, pattern):
    text_length, pattern_length = len(text), len(pattern)
    pattern_hash = hash(pattern)
    for i in range(text_length - pattern_length + 1):
        current_hash = hash(text[i:i + pattern_length])
        if current_hash == pattern_hash and text[i:i + pattern_length] == pattern:
            return i
    return -1



