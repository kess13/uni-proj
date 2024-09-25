def brute_force_pattern_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    i = 0

    while i < (n - m + 1):
        j = 0
        match = True
        while j < m:
            if text[i + j] != pattern[j]:
                match = False
                break
            j += 1
        if match:
            return True
        i += 1

    return False


def test_brute_force_pattern_matching():
    
    text = "ABCDABCD"
    pattern = "ABCD"
    assert brute_force_pattern_matching(text, pattern) == True, "Test Case 1 Failed"

    
    text = "AABAACAADAABAABA"
    pattern = "AABA"
    assert brute_force_pattern_matching(text, pattern) == True, "Test Case 2 Failed"

    
    text = "ABCDABCD"
    pattern = "XYZ"
    assert brute_force_pattern_matching(text, pattern) == False, "Test Case 3 Failed"

    
    text = ""
    pattern = "A"
    assert brute_force_pattern_matching(text, pattern) == False, "Test Case 4 Failed"

    text = "ABC"
    pattern = ""
    assert brute_force_pattern_matching(text, pattern) == True, "Test Case 5 Failed"


    text = ""
    pattern = ""
    assert brute_force_pattern_matching(text, pattern) == True, "Test Case 6 Failed"

    text = "ABC"
    pattern = "ABCD"
    assert brute_force_pattern_matching(text, pattern) == False, "Test Case 7 Failed"

    text = "ABCDEF"
    pattern = "DEF"
    assert brute_force_pattern_matching(text, pattern) == True, "Test Case 8 Failed"

    print("All test cases passed!")


test_brute_force_pattern_matching()

