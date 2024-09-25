def original_sunday_algorithm(text, pattern):
    m = len(pattern)
    n = len(text)

    # Construct skip table
    skip_table = {}
    for i in range(m):
        if pattern[i] not in skip_table:
            skip_table[pattern[i]] = m - i

    i = 0
    while i <= n - m:
        j = 0
        while j < m and (text[i + j] == pattern[j]):
            j += 1
        if j == m:
            return True
        if i + m >= n:
            break
        if text[i + m] in skip_table:
            i += skip_table[text[i + m]]
        else:
            i += m + 1
    return False

def test_original_sunday_algorithm():
    assert original_sunday_algorithm("hello world", "hello") == True
    assert original_sunday_algorithm("hello world", "python") == False
    assert original_sunday_algorithm("hello hello hello", "hello") == True
    assert original_sunday_algorithm("", "hello") == False
    assert original_sunday_algorithm("hello world", "") == True
    assert original_sunday_algorithm("hello", "hello world") == False
    assert original_sunday_algorithm("", "") == True
    assert original_sunday_algorithm("hello world", "hello") == True
    assert original_sunday_algorithm("hello world", "world") == True
    assert original_sunday_algorithm("Hello, world!", ",") == True
    assert original_sunday_algorithm("Hello, world!", "!") == True
    assert original_sunday_algorithm("Hello, world!", " ") == True
    assert original_sunday_algorithm("Hello, 12345!", "12345") == True
    assert original_sunday_algorithm("apple orange banana", "orange") == True
    assert original_sunday_algorithm("abcdefg", "abc") == True
    assert original_sunday_algorithm("1234567890", "345") == True
    assert original_sunday_algorithm("aaabbbccc", "bb") == True
    assert original_sunday_algorithm("xyz", "x") == True
    assert original_sunday_algorithm("xyz", "z") == True

    print("All assert tests passed successfully.")

test_original_sunday_algorithm()
