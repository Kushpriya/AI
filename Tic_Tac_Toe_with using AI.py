import tkinter as tk
from tkinter import messagebox
import random

def game_over(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return True

    if all([cell != '' for row in board for cell in row]):
        return True

    return False

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]

    return None

def handle_click(row, col):
    global player_turn

    if board[row][col] == '' and not game_over(board) and player_turn:
        board[row][col] = 'X'
        update_board()
        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Game Over", f"{winner} wins!")
            return
        if game_over(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            return

        player_turn = False
        ai_move()

def update_board():
    for i in range(3):
        for j in range(3):
            button_grid[i][j].config(text=board[i][j])

def empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']

def minimax(board, depth, is_maximizing):
    if game_over(board):
        score = 0
        winner = check_winner(board)
        if winner == 'X':
            score = -1
        elif winner == 'O':
            score = 1
        return score

    if is_maximizing:
        best_score = -float('inf')
        for move in empty_cells(board):
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ''
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in empty_cells(board):
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ''
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    best_move = None
    for move in empty_cells(board):
        board[move[0]][move[1]] = 'O'
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = ''
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def ai_move():
    global player_turn

    if not game_over(board) and not player_turn:
        row, col = best_move(board)
        board[row][col] = 'O'
        update_board()
        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Game Over", f"{winner} wins!")
        elif game_over(board):
            messagebox.showinfo("Game Over", "It's a tie!")
        player_turn = True

root = tk.Tk()
root.title("Tic Tac Toe")

board = [['' for _ in range(3)] for _ in range(3)]

player_turn = True

button_grid = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        button_grid[i][j] = tk.Button(root, text='', font=('Arial', 20), width=6, height=3,
                                       command=lambda row=i, col=j: handle_click(row, col))
        button_grid[i][j].grid(row=i, column=j, padx=5, pady=5)

root.mainloop()
