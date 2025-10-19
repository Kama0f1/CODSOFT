import math
player, ai = 'X', 'O'

def print_board(board):
    print("\n")
    for row in board:
        print(' | '.join(row))
        print('-' * 9)
    print("\n")
        
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[1][1]
    return None

def empty_cells(board):
    cells = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == ' ':
                cells.append((x, y))
    return cells

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == ai:
        return 1
    if winner == player:
        return -1
    if not empty_cells(board):
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for (x,y) in empty_cells(board):
            board[x][y] = ai
            score = minimax(board, depth +1,  False)
            board[x][y] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for (x,y) in empty_cells(board):
            board[x][y] = player
            score = minimax(board , depth +1, True)
            board[x][y] = ' '
            best_score = min(score,best_score)
        return best_score
    
def ai_move(board):
    best_score = -math.inf
    move = None
    for (x,y) in empty_cells(board):
        board[x][y] = ai
        score = minimax(board, 0, False)
        board[x][y] = ' '
        if score > best_score: 
            best_score = score
            move = (x,y)
    if move:
        board[move[0]][move[1]] = ai

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("\n=== Tic Tac Toe AI Using Minimax ===")
    print("You = X, AI = O\n")
    current_player = player
    print_board(board)
    
    while True:
        if not empty_cells(board):
            print("\nIt's a draw!\n")
            break
        if current_player == player:
            try:
                x, y = map(int, input("\nEnter your move (row[0-2] and column[0-2]): ").split())
                if 0 <= x <= 2 and 0 <= y <= 2 and board[x][y] == ' ':
                    board[x][y] = player
                    if check_winner(board) == player:
                        print_board(board)
                        print("\nYou win!\n")
                        break
                    current_player = ai
                else:
                    print("\nInvalid move! Try again.\n")
                    continue
            except (ValueError, IndexError):
                print("\nInvalid input! Please enter two numbers between 0 and 2.\n")
                continue
        else:
            print("\nAI is making a move...\n")
            ai_move(board)
            if check_winner(board) == ai:
                print_board(board)
                print("\nAI wins!\n")
                break
            current_player = player
        print_board(board)

if __name__ == "__main__":
    main()