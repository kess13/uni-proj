def preprocess(pattern):
    new_pattern = ""
    escaped = []
    i = 0
    while i < len(pattern):
        if pattern[i] == "\\":
            if i + 1 < len(pattern) and pattern[i + 1] in ["*", "?", "\\"]:
                new_pattern += pattern[i + 1]
                escaped.append(True)
                i += 2
            else:
                new_pattern += "\\"
                escaped.append(False)
                i += 1
        else:
            new_pattern += pattern[i]
            escaped.append(False)
            i += 1
    return new_pattern, escaped

def build_skip_table(pattern):
    m = len(pattern)
    skip_table = {}
    for i in range(m - 1, -1, -1):
        if pattern[i] not in skip_table:
            skip_table[pattern[i]] = m - i
    return skip_table

def find_subpattern(text, subpattern, start, escaped):
    m = len(subpattern)
    n = len(text)
    if m == 0:
        return start

    skip_table = build_skip_table(subpattern)

    i = start
    while i <= n - m:
        j = 0
        while j < m and (text[i + j] == subpattern[j] or (subpattern[j] == '?' and not escaped[j])):
            j += 1
        if j == m:
            return i + m
        if i + m < n and text[i + m] in skip_table:
            i += skip_table[text[i + m]]
        else:
            i += m + 1
    return -1

def split_pattern(pattern, escaped):
    parts = []
    current_part = []
    current_escaped = []
    for i in range(len(pattern)):
        if pattern[i] == "*" and not escaped[i]:
            if current_part:
                parts.append(("".join(current_part), current_escaped))
                current_part = []
                current_escaped = []
        else:
            current_part.append(pattern[i])
            current_escaped.append(escaped[i])
    if current_part:
        parts.append(("".join(current_part), current_escaped))
    return parts

def sunday_algorithm_with_wildcard(text, pattern):
    if len(pattern) == 0 and len(text) == 0:
        return True
    elif len(pattern) == 0:
        return False

    pattern, escaped = preprocess(pattern)
    parts = split_pattern(pattern, escaped)
    start = 0
    for part, part_escaped in parts:
        if part == '':
            continue
        start = find_subpattern(text, part, start, part_escaped)
        if start == -1:
            return False
    return True

# Test function
def test_sunday_algorithm_with_wildcard():
    # Single character match
    assert sunday_algorithm_with_wildcard("a", "a") == True
    assert sunday_algorithm_with_wildcard("a", "b") == False

    # Exact match
    assert sunday_algorithm_with_wildcard("abc", "abc") == True
    assert sunday_algorithm_with_wildcard("abc", "abd") == False

    # '?' wildcard
    assert sunday_algorithm_with_wildcard("abc", "a?c") == True
    assert sunday_algorithm_with_wildcard("axc", "a?c") == True
    assert sunday_algorithm_with_wildcard("axx", "a?c") == False
    assert sunday_algorithm_with_wildcard("axx", "a??x") == False
    assert sunday_algorithm_with_wildcard("axxx", "a??x") == True

    # '*' wildcard
    assert sunday_algorithm_with_wildcard("a", "a*") == True
    assert sunday_algorithm_with_wildcard("aa", "a*") == True
    assert sunday_algorithm_with_wildcard("ab", "a*") == True
    assert sunday_algorithm_with_wildcard("ab", "a*b") == True
    assert sunday_algorithm_with_wildcard("acb", "a*b") == True
    assert sunday_algorithm_with_wildcard("acefbwqd", "a*b") == True
    assert sunday_algorithm_with_wildcard("ab", "*b") == True
    assert sunday_algorithm_with_wildcard("acbd", "a***b*") == True
    assert sunday_algorithm_with_wildcard("ac", "a*b*c") == False
    assert sunday_algorithm_with_wildcard("ac", "a***c") == True

    # Escaped characters
    assert sunday_algorithm_with_wildcard("a*b", "a\\*b") == True
    assert sunday_algorithm_with_wildcard("a?c", "a\\?c") == True
    assert sunday_algorithm_with_wildcard("a\\b", "a\\\\b") == True
    assert sunday_algorithm_with_wildcard("?", "\\?") == True
    assert sunday_algorithm_with_wildcard("a", "\\?") == False
    assert sunday_algorithm_with_wildcard("aa", "\\??") == False
    assert sunday_algorithm_with_wildcard("aaa", "aa\\*") == False # text, pattern
    assert sunday_algorithm_with_wildcard("aa\\a", "aa\\*") == False
    assert sunday_algorithm_with_wildcard("*", "\\*") == True
    assert sunday_algorithm_with_wildcard("aaa", "\\*") == False
    assert sunday_algorithm_with_wildcard("aa*", "aa\\*") == True

    # Mix of wildcards and escaped characters
    assert sunday_algorithm_with_wildcard("a\\*c?", "a\\*c?") == False
    assert sunday_algorithm_with_wildcard("*\\*?*", "*\\*?*") == True
    assert sunday_algorithm_with_wildcard("\\*\\?\\*", "*?*") == True
    assert sunday_algorithm_with_wildcard("*\\?\\\\\\*", "*?\\*") == True
    assert sunday_algorithm_with_wildcard("\\*???", "*?\\*") == True
    assert sunday_algorithm_with_wildcard("\\*b", "\\ab") == False
    assert sunday_algorithm_with_wildcard("\\*b", "*b") == True

    # Empty patterns and texts
    assert sunday_algorithm_with_wildcard("", "") == True
    assert sunday_algorithm_with_wildcard("", "a") == False
    assert sunday_algorithm_with_wildcard("a", "") == False

    print("All tests passed!")

test_sunday_algorithm_with_wildcard()
