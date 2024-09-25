def fsm_search(text, pattern):
    # Function to build the finite state machine for the given pattern
    def build_fsm(pattern):
        # Create a set of all unique characters in the pattern (the alphabet)
        alphabet = set(pattern)
        # Initialize the FSM table, which is a list of dictionaries.
        # Each dictionary maps characters to states. There are len(pattern) + 1 states.
        fsm = [{c: 0 for c in alphabet} for _ in range(len(pattern) + 1)]
        
        # Build the FSM table
        for i in range(len(pattern)):
            # Get the previous state for the current character in the pattern
            prev_state = fsm[i][pattern[i]]
            # Set the state for the current character to the next state
            fsm[i][pattern[i]] = i + 1
            # Update the next state's transitions to match the previous state's transitions
            for c in alphabet:
                fsm[i + 1][c] = fsm[prev_state][c]
        
        # Return the completed FSM table
        return fsm

    # Build the FSM for the given pattern
    fsm = build_fsm(pattern)
    # Initialize the current state to 0
    state = 0
    
    # Iterate over each character in the text
    for i in range(len(text)):
        # If the current character is in the FSM's current state transitions, update the state
        if text[i] in fsm[state]:
            state = fsm[state][text[i]]
        else:
            # If the current character is not in the FSM's current state transitions, reset the state to 0
            state = 0
        
        # If the state equals the length of the pattern, a match is found
        if state == len(pattern):
            # Return the starting index of the match in the text
            return i - len(pattern) + 1
    
    # If no match is found, return -1
    return -1

# Test cases to verify the implementation
assert fsm_search("hello world", "world") == 6
assert fsm_search("hello world", "hello") == 0
assert fsm_search("hello world", "o w") == 4
assert fsm_search("hello world", "planet") == -1
print("FSM algorithm tests passed.")
