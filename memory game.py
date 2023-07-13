import random

# Create the board
def create_board(size):
    symbols = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    num_pairs = size * size // 2
    pairs = random.sample(symbols, num_pairs)
    board = random.sample(pairs * 2, num_pairs * 2)
    random.shuffle(board)
    return [board[i:i+size] for i in range(0, size*size, size)]

# Display the board
def display_board(board):
    for row in board:
        print(" ".join(row))

# Get user input for the row and column
def get_input(size):
    while True:
        try:
            row = int(input("Enter the row (0 to N-1): "))
            col = int(input("Enter the column (0 to N-1): "))
            if row >= 0 and row < size and col >= 0 and col < size:
                return row, col
            else:
                print("Invalid input! Row and column values must be within the valid range.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Main game loop
def play_game(size):
    board = create_board(size)
    display_board(board)

    while True:
        print("\n")
        row1, col1 = get_input(size)
        print("\n")
        row2, col2 = get_input(size)

        if board[row1][col1] == board[row2][col2]:
            board[row1][col1] = "-"
            board[row2][col2] = "-"
            display_board(board)
            print("Match found!")
        else:
            print("No match.")

        if all(all(val == "-" for val in row) for row in board):
            print("Congratulations! You won!")
            break

# Start the game
size = int(input("Enter the size of the board: "))
play_game(size)
