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

    if best_move is not None:
        board[best_move[0]][best_move[1]] = 'X'
        return best_move
    return None

def minimax(board, is_maximizing):
    winner = check_winner(board)

    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif not get_empty_cells(board):
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

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == '_']

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != '_':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '_':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return board[0][2]
    return None
