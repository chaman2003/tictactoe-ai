def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == '_']

def check_winner(board):
    for line in get_all_lines(board):
        if line[0] == line[1] == line[2] and line[0] != '_':
            return line[0]
    return None

def get_all_lines(board):
    lines = []
    lines.extend(board)
    for j in range(3):
        lines.append([board[i][j] for i in range(3)])
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])
    return lines

def player_move(board, name):
    move_row = input("Enter your move (row): ")
    move_col = input("Enter your move (column): ")
    try:
        row, col = int(move_row) - 1, int(move_col) - 1
        if not (0 <= row <= 2 and 0 <= col <= 2):
            raise ValueError("Row and column indices must be between 1 and 3.")
        if board[row][col] != '_':
            raise ValueError("That cell is already taken. Try again.")
        board[row][col] = 'O'
        print_board(board)
        return row, col
    except ValueError as e:
        print(e)
        return player_move(board, name)

def ai_move(board):
    best_score = float('-inf')
    best_move = None
    for move in get_empty_cells(board):
        board[move[0]][move[1]] = 'X'
        score = minimax(board, False)
        board[move[0]][move[1]] = '_'
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move[0]][best_move[1]] = 'X'
    print("AI's move:")
    print_board(board)

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif '_' not in [cell for row in board for cell in row]:
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for move in get_empty_cells(board):
            board[move[0]][move[1]] = 'X'
            score = minimax(board, False)
            board[move[0]][move[1]] = '_'
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_empty_cells(board):
            board[move[0]][move[1]] = 'O'
            score = minimax(board, True)
            board[move[0]][move[1]] = '_'
            best_score = min(score, best_score)
        return best_score
