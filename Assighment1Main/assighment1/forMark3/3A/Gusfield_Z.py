def z_function(s):
    # Initialize the Z array with zeros. This array will hold the lengths of the longest substrings
    # starting from each position that match the prefix of the string.
    Z = [0] * len(s)
    
    # Initialize the left and right boundaries of the current Z-box, and an index variable.
    L, R, K = 0, 0, 0

    # Start iterating from the second character to the end of the string
    for i in range(1, len(s)):
        if i > R:
            # If i is outside the current Z-box, set new boundaries
            L, R = i, i
            # Expand the new Z-box as far as possible
            while R < len(s) and s[R] == s[R - L]:
                R += 1
            # Set the Z value for position i
            Z[i] = R - L
            # Adjust the right boundary to the last matching position
            R -= 1
        else:
            # If i is inside the current Z-box, calculate the corresponding position in the Z-array
            K = i - L
            if Z[K] < R - i + 1:
                # If the Z value at K is less than the remaining length of the Z-box, copy it
                Z[i] = Z[K]
            else:
                # Otherwise, start a new Z-box from position i
                L = i
                while R < len(s) and s[R] == s[R - L]:
                    R += 1
                # Set the Z value for position i
                Z[i] = R - L
                # Adjust the right boundary to the last matching position
                R -= 1
    # Return the completed Z array
    return Z


def gusfield_z_search(text, pattern):
    concatenated = pattern + "$" + text
    Z = z_function(concatenated)
    for i in range(len(pattern) + 1, len(concatenated)):
        if Z[i] == len(pattern):
            return i - len(pattern) - 1
    return -1


assert gusfield_z_search("hello world", "world") == 6
assert gusfield_z_search("hello world", "hello") == 0
assert gusfield_z_search("hello world", "o w") == 4
assert gusfield_z_search("hello world", "planet") == -1
print("Gusfield Z algorithm tests passed.")
