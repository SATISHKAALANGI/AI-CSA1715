CODE:
from collections import deque

# Goal state
GOAL = "123456780"

# Possible positions for the blank (0)
MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}


def solve_puzzle(start):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == GOAL:
            return path + [state]

        blank = state.index("0")

        for position in MOVES[blank]:
            state_list = list(state)

            # Move blank
            state_list[blank], state_list[position] = \
                state_list[position], state_list[blank]

            new_state = "".join(state_list)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))

    return None


def display(state):
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()


# Main program
print("8-Puzzle Problem using BFS")
print("Use 0 for the blank space.")

start = input("Enter initial state: ")

if len(start) != 9 or not start.isdigit() or set(start) != set("012345678"):
    print("Invalid input!")
else:
    solution = solve_puzzle(start)

    if solution:
        print("\nSolution found!")
        print("Number of moves:", len(solution) - 1)
        print("\nSteps:\n")

        for i, state in enumerate(solution):
            print("Step", i)
            display(state)
    else:
        print("No solution exists.")

  OUTPUT:
8-Puzzle Problem using BFS
Use 0 for the blank space.
Enter initial state: 123456708

Solution found!
Number of moves: 1

Steps:

Step 0
1 2 3
4 5 6
7 0 8

Step 1
1 2 3
4 5 6
7 8 0
