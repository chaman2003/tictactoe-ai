from flask import Flask, render_template, jsonify, request
from minimax import ai_move

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-ai-move', methods=['POST'])
def get_ai_move():
    data = request.json
    board_state = data.get('board')
    difficulty = data.get('difficulty')
    
    ai_move_result = calculate_ai_move(board_state, difficulty)
    
    return jsonify({'move': ai_move_result})

def calculate_ai_move(board, difficulty):
    board_2d = [list(board[i:i + 3]) for i in range(0, 9, 3)]
    
    if difficulty == 'easy':
        available_moves = [i for i, cell in enumerate(board) if cell == '_']
        return available_moves[0]
    elif difficulty == 'medium':
        available_moves = [i for i, cell in enumerate(board) if cell == '_']
        if available_moves:
            return available_moves[len(available_moves) // 2]
    elif difficulty == 'hard':
        move = ai_move(board_2d)
        return move[0] * 3 + move[1]
    
    return None

if __name__ == '__main__':
    app.run(debug=True)
