def binary_sunday_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0

    # Step 1: Preprocess - Create a shift table
    shift_table = {char: m + 1 for char in set(text)}
    for i in range(m):
        shift_table[pattern[i]] = m - i

    # Step 2: Searching using binary steps
    i = 0
    while i <= n - m:
        # Check for match
        j = 0
        while j < m and pattern[j] == text[i + j]:
            j += 1

        if j == m:
            return i

        # Use binary search optimization
        if i + m < n:
            skip = shift_table.get(text[i + m], m + 1)
        else:
            skip = m + 1

        i += skip

    return -1  # Pattern not found



