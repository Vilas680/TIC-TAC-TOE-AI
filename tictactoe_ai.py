
import math

# Game board
board = [' ' for _ in range(9)]

# Display board
def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print("---------")
    print()

# Check winner
def check_winner(player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check draw
def is_draw():
    return ' ' not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    best_move = 0

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = 'O'

# Main game loop
print("TIC-TAC-TOE GAME")
print("You are X | AI is O")
print("Positions: 0 1 2 | 3 4 5 | 6 7 8")

while True:
    print_board()
    move = int(input("Enter your move (0-8): "))

    if board[move] != ' ':
        print("Invalid move! Try again.")
        continue

    board[move] = 'X'

    if check_winner('X'):
        print_board()
        print("🎉 You Win!")
        break

    if is_draw():
        print_board()
        print("🤝 Draw!")
        break

    ai_move()

    if check_winner('O'):
        print_board()
        print("🤖 AI Wins!")
        break
