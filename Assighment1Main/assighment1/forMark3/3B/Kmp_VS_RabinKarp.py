import time

def kmp_search(pattern, text):
    lps = [0] * len(pattern)
    j = 0
    compute_lps_array(pattern, lps)
    
    i = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            j = lps[j-1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

def compute_lps_array(pattern, lps):
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

def rabin_karp_search(pattern, text, q=101):
#d: The number of characters in the input alphabet (256 for ASCII).
#m: The length of the pattern.
#n: The length of the text.
#p: The hash value for the pattern.
#t: The hash value for the current window of text.
#h: constant multiplier
#This loop calculates h = d^(m-1) % q using modular exponentiation. This value of h is used to remove the influence of the leading character in the current window of the text when computing the hash for the next window.
    d = 256
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    
    for i in range(m-1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            else:
                pass
        
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

# Assume text is read from a file
file_path = 'text_and_pattern.txt'
with open(file_path, 'r') as file:
    text_content = file.read()

pattern_content = "abababab"

# Measure KMP
start_time = time.time()
kmp_search(pattern_content, text_content)
kmp_duration = (time.time() - start_time) * 1e6

# Measure Rabin-Karp
start_time = time.time()
rabin_karp_search(pattern_content, text_content)
rabin_karp_duration = (time.time() - start_time) * 1e6

print(f"KMP: {kmp_duration} microseconds")
print(f"Rabin Karp: {rabin_karp_duration} microseconds")
