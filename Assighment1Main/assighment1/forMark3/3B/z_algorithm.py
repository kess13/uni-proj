def z_algorithm(input_string):
    Z = [0] * len(input_string)
    left, right, k = 0, 0, 0
    for i in range(1, len(input_string)):
        if i > right:
            left, right = i, i
            while right < len(input_string) and input_string[right] == input_string[right - left]:
                right += 1
            Z[i] = right - left
            right -= 1
        else:
            k = i - left
            if Z[k] < right - i + 1:
                Z[i] = Z[k]
            else:
                left = i
                while right < len(input_string) and input_string[right] == input_string[right - left]:
                    right += 1
                Z[i] = right - left
                right -= 1
    return Z


def gusfield_z_search(text, pattern):
    concatenated_string = pattern + "$" + text
    Z = z_algorithm(concatenated_string)
    pattern_length = len(pattern)
    for i in range(len(Z)):
        if Z[i] == pattern_length:
            return i - pattern_length - 1
    return -1

