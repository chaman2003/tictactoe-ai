def print_board(board):
    for row in range(0, 9, 3):
        print(" | ".join(board[row:row+3]))
        print("-" * 9)

def get_empty_cells(board):
    return [i for i in range(len(board)) if board[i] == '_']

def check_winner(board):
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)]
    
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != '_':
            return board[a]
    return None

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'X': return 1
    if winner == 'O': return -1
    if '_' not in board: return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in get_empty_cells(board):
            board[i] = 'X'
            score = minimax(board, False)
            board[i] = '_'
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in get_empty_cells(board):
            board[i] = 'O'
            score = minimax(board, True)
            board[i] = '_'
            best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score, move = -float('inf'), None
    for i in get_empty_cells(board):
        board[i] = 'X'
        score = minimax(board, False)
        board[i] = '_'
        if score > best_score:
            best_score, move = score, i
    board[move] = 'X'

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != '_': raise ValueError("Cell taken.")
            board[move] = 'O'
            print_board(board)
            return
        except (ValueError, IndexError):
            print("Invalid move. Try again.")

def main():
    board = ['_'] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player_move(board)
        if (winner := check_winner(board)):
            print(f"{winner} wins!" if winner == 'X' else "You win!")
            break
        if '_' not in board:
            print("It's a draw!")
            break
        ai_move(board)
        print("AI's move:")
        print_board(board)
        if (winner := check_winner(board)):
            print(f"{winner} wins!" if winner == 'X' else "You win!")
            break

if __name__ == "__main__":
    main()
