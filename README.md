# basic-tetris 

## PROBLEM STATEMENT

There are 5 different pieces in this version of Tetris defined as follows and they fall down a 12x12 tetris board:

PIECES = [
    [[1, 1, 1, 1]],
    [[1, 0], [1, 0], [1, 1]],
    [[0, 1], [0, 1], [1, 1]],
    [[1, 0], [1, 1], [0, 1]],
    [[1, 1], [1, 1]]
]
The game starts with a random piece appearing at the top of the board (centered horizontally on the first row). The user is then prompted to make a move:
 <a> (+<return>): move piece left and move one row down
 <d> (+<return>): move piece right and move one row down
 <w> (+<return>): rotate piece counter clockwise and move one row down
 <s> (+<return>): rotate piece clockwise and move one row down
 <space>: no action and the piece moves one row down

If the move the user selects is valid, then it is executed and the grid is redrawn and printed again on the screen. If the action is not valid, then the user is again prompted to enter a valid move. Note that the game state only updates after the user has entered a valid action.

A valid move is defined thus: if the piece, drawn at its new location, is not outside the bounds of the board, and does not overlap any pieces that previously fell, then the move is valid. 

If a new piece’s position is such that it allows no valid move, then a new piece appears along the top of the board, randomly positioned along the x-axis (i.e. not in the center of the first row). 

If this new piece offers no valid move, then the game is over and the program exits.
