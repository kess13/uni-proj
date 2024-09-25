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
                continue
            else:
                new_pattern += "\\"
                escaped.append(False)
        else:
            new_pattern += pattern[i]
            escaped.append(False)
        i += 1
    return new_pattern, escaped


def is_match(text, pattern):
    pattern, escaped = preprocess(pattern)
    text_index = 0
    pattern_index = 0
    last_wildcard_index = -1
    text_backtrack_index = -1
    next_to_wildcard_index = -1

    if len(pattern) == 0 and len(text) > 0:
        return False



    while text_index < len(text):
        if pattern_index < len(pattern) and (pattern[pattern_index] == '?' and not escaped[pattern_index] or
                                             pattern[pattern_index] == text[text_index]):
            text_index += 1
            pattern_index += 1
        elif pattern_index < len(pattern) and pattern[pattern_index] == '*' and not escaped[pattern_index]:
            last_wildcard_index = pattern_index
            next_to_wildcard_index = pattern_index + 1
            text_backtrack_index = text_index
            pattern_index += 1
        elif last_wildcard_index == -1:
            return False
        else:
            pattern_index = next_to_wildcard_index
            text_backtrack_index += 1
            text_index = text_backtrack_index

    while pattern_index < len(pattern) and pattern[pattern_index] == '*' and not escaped[pattern_index]:
        pattern_index += 1

    return pattern_index == len(pattern)


def test_is_match():
    assert is_match("b", "a") == False
    assert is_match("a", "a") == True

    # Exact match
    assert is_match("abc", "abc") == True
    assert is_match("abd", "abc") == False

    # '?' wildcard
    assert is_match("abc", "a?c") == True
    assert is_match("axc", "a?c") == True
    assert is_match("axx", "a?c") == False

    # '*' wildcard
    assert is_match("a", "a*") == True
    assert is_match("a", "*a") == True
    assert is_match("aa", "a*") == True
    assert is_match("ab", "a*") == True
    assert is_match("ab", "a*b") == True
    assert is_match("acb", "a*b") == True
    assert is_match("ab", "*b") == True
    assert is_match("acbd", "a***b*") == True
    assert is_match("ac", "a*b*c") == False
    assert is_match("abbbc", "a*c") == True
    assert is_match("aaa", "aa\\*") == False

    # Escaped characters
    assert is_match("a*b", "a\\*b") == True
    assert is_match("a?c", "a\\?c") == True
    assert is_match("a\\b", "a\\\\b") == True
    assert is_match("?", "\\?") == True
    assert is_match("aa", "\\??") == False #text, pattern
    assert is_match("aaa", "aa\\*") == False
    assert is_match("aa\\a", "aa\\*") == False
    assert is_match("aa*", "aa\\*") == True
    assert is_match("*", "\\*") == True
    assert is_match("a", "\\*") == False
    assert is_match("a", "\\?") == False 
    assert is_match("aaa", "\\*") == False
    assert is_match("aa*", "aa\\*") == True

    # Mix of wildcards and escaped characters
    assert is_match("a*c?", "a\\*c?") == True
    assert is_match("*?*", "***") == True
    assert is_match("ar*?*qr", "*") == True
    assert is_match("ar*?*qr", "*???") == True
    assert is_match("*?*", "\\*\\?\\*") == True
    assert is_match("*?\\*", "*\\?\\\\\\*") == True
    assert is_match("*?\\*", "\\*???") == True
    assert is_match("\\ab", "\\*b") == False
    assert is_match("*b", "\\*b") == True

    # Empty patterns and texts
    assert is_match("", "") == True
    assert is_match("a", "") == False
    assert is_match("", "a") == False

    print("All tests passed!")


test_is_match()
