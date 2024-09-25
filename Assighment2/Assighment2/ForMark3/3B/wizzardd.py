from collections import deque  # Import deque for efficient queue operations

def reverse_bfs(labyrinth, exit):
    rows, cols = len(labyrinth), len(labyrinth[0])  # Get dimensions of the labyrinth
    queue = deque([(exit[0], exit[1], 0)])  # Initialize queue with exit position and distance 0
    distances = [[float('inf')] * cols for _ in range(rows)]  # Initialize distances with infinity
    distances[exit[0]][exit[1]] = 0  # Distance to the exit from itself is 0

    while queue:  # While there are positions to process in the queue
        r, c, dist = queue.popleft()  # Dequeue the next position and its distance
        # Explore all possible moves (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc  # Calculate the new position
            if 0 <= nr < rows and 0 <= nc < cols and labyrinth[nr][nc] != '#' and distances[nr][nc] == float('inf'):
                # Check if the new position is within bounds, not a wall, and not visited
                distances[nr][nc] = dist + 1  # Update the distance for the new position
                queue.append((nr, nc, dist + 1))  # Enqueue the new position with incremented distance

    return distances  # Return the distances grid

def predict_winner(labyrinth, wizard_start_positions, wizard_speeds, exit_symbol='E'):
    # Find the exit position in the labyrinth
    exit_position = None
    for r in range(len(labyrinth)):
        for c in range(len(labyrinth[0])):
            if labyrinth[r][c] == exit_symbol:
                exit_position = (r, c)
                break
        if exit_position:
            break

    if not exit_position:
        raise ValueError("Exit not found in labyrinth")

    distances = reverse_bfs(labyrinth, exit_position)  # Perform reverse BFS from the exit

    times = []  # List to store the times each wizard takes to reach the exit
    for i, (start, speed) in enumerate(zip(wizard_start_positions, wizard_speeds)):
        distance_to_exit = distances[start[0]][start[1]]  # Get the precomputed distance to the exit
        time_to_exit = distance_to_exit / speed  # Calculate time to exit based on wizard's speed
        times.append((time_to_exit, i))  # Append the time and wizard index to the list

    times.sort()  # Sort the wizards based on their time to exit
    return times[0][1], times  # Return the index of the fastest wizard and all times

# Example labyrinth and inputs
labyrinth = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '#', '.', '#'],
    ['#', '.', '#', '.', '#', '.', '#'],
    ['#', 'E', '#', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '#', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#'],
]

wizard_start_positions = [(1, 1), (1, 5), (5, 5)]  # Starting positions of wizards
wizard_speeds = [2, 3, 1]  # Speeds of wizards in corridors per minute

try:
    # Determine the winner and all arrival times
    winner_index, all_times = predict_winner(labyrinth, wizard_start_positions, wizard_speeds)

    # Output the results
    print(f"Winner: Wizard {winner_index + 1}")  # Print the index of the winning wizard
    for time, i in all_times:
        print(f"Wizard {i + 1}: Time = {time:.2f} minutes")  # Print the times for each wizard

except ValueError as e:
    print(e)  # Print error message if exit is not found