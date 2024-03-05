import tkinter as tk
from tkinter import messagebox

# Function to check if the game is over
def game_over(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return True

    # Check for tie
    if all([cell != '' for row in board for cell in row]):
        return True

    return False

# Function to check for winner
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]

    return None

# Function to handle player's move
def handle_click(row, col):
    global player_turn

    if board[row][col] == '' and not game_over(board):
        if player_turn:
            board[row][col] = 'X'
            player_turn = False
        else:
            board[row][col] = 'O'
            player_turn = True

        update_board()
        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Game Over", f"{winner} wins!")
        elif game_over(board):
            messagebox.showinfo("Game Over", "It's a tie!")

# Function to update the GUI board
def update_board():
    for i in range(3):
        for j in range(3):
            button_grid[i][j].config(text=board[i][j])

# Initialize the GUI window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize the game board
board = [['' for _ in range(3)] for _ in range(3)]

# Initialize player's turn
player_turn = True

# Create buttons for the game board
button_grid = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        button_grid[i][j] = tk.Button(root, text='', font=('Arial', 20), width=6, height=3,
                                       command=lambda row=i, col=j: handle_click(row, col))
        button_grid[i][j].grid(row=i, column=j, padx=5, pady=5)

# Run the GUI main loop
root.mainloop()
