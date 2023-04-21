import random

BOARD_WIDTH = 12
BOARD_HEIGHT = 12

PIECES = [
    [[1, 1, 1, 1]],
    [[1, 0], [1, 0], [1, 1]],
    [[0, 1], [0, 1], [1, 1]],
    [[1, 0], [1, 1], [0, 1]],
    [[1, 1], [1, 1]]
]

def create_board():
    """ Create new board with empty cells"""
    board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
    return board

def get_random_piece(board):
    """Return random tetris piece"""
    return random.choice(PIECES)

def print_board(board):
    """print current board"""
    for row in board:
        print(" ".join(str(cell)) for cell in row)

def is_valid_move(board, piece, row, col):
    """ check if move is valid 
        1. check if it is inside the board
        2. check if it is not overlapping
    """
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if row + i < 0 or row + i >= BOARD_HEIGHT:
                return False
            if col + j < 0 or col + j >= BOARD_WIDTH:
                return False
            if board[row+i][col+j] != 0 and piece[i][j] != 0:
                return False
    return True
            

def add_piece_to_board(board, piece, row,col):
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] != 0:
                board[row+i][col+j] = piece[i][j]



def remove_completed_rows(board):
    completed_rows = []
    for i in range(BOARD_HEIGHT):
        if 0 not in board[i]:
            completed_rows.append(i)
    
    for row in completed_rows:
        del board[row]
        board.insert(0,[0]* BOARD_WIDTH)

def add_piece_to_fallen_piece(piece, position, fallen_pieces):
    """TODO"""
    return 0

def is_game_over(piece, cuurent_row,current_col, fallen_pieces):
    for i in range(len(piece)):
        for j in range(len(piece)):
            if piece[i][j] == 1:
                row = cuurent_row + i
                col = current_col + j
            if row < 0 or row >= BOARD_HEIGHT or col < 0 or col >= BOARD_WIDTH:
                return True
        return False 
   
def main():
    """Play the game    
    """

    board = create_board()
    current_piece = get_random_piece(board)
    current_row = 0
    current_col = BOARD_WIDTH //2 - len(current_piece[0]) // 2
    game_over = False
    while not game_over:
        print(board)
        move = input("Enter a move (a, d, w, s or space)")
        new_piece = current_piece.copy()
        new_row = current_row
        new_col = current_col

        if move == "a":
            new_col -=1
        if move == "d":
            new_col +=1
        elif move == "s":
            new_piece = list(zip(*reversed(new_piece)))
        elif move == "d":
            new_piece = list(reversed(list(zip(*new_piece))))
        elif move == " ":
            new_row +=1
        else:
            print("Invalid Move")
            continue
        

        if is_valid_move(board, new_piece, new_row, new_col):
            current_piece = new_piece
            current_piece = new_row
            current_col = new_col
            add_piece_to_board(board, new_piece, new_row, new_col)
            remove_completed_rows(board)
            current_piece = get_random_piece(board)
            fallen_piece = add_piece_to_fallen_piece(current_piece, 0, 0)
        else:
            print("Invalid move")
            break

        if is_game_over(current_piece,current_row,current_col, 0):
            game_over = True
            print("Thank You! Game is Over!!")
        else:
            current_piece = get_random_piece(board)
            current_row = 0  
            max_left = BOARD_WIDTH - len(current_piece[0])
            max_right = 0
            current_col = random.randint(max_right, max_left)
main()