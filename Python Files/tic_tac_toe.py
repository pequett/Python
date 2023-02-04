'''
Tic Tac Toe by Malachi Campomizzi
Started: 10/19/2022 Finished: 10/22/2022
Python Institute (PCEP) 4.7.2.1 PROJECT: Tic-Tac-Toe
'''
from random import randint
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(' +-------+-------+-------+\n',
    '|       |       |       |\n',
    '|   {}   |   {}   |   {}   |\n'.format(board[0][0], board[0][1], board[0][2]),
    '|       |       |       |\n',
    '+-------+-------+-------+\n',
    '|       |       |       |\n',
    '|   {}   |   {}   |   {}   |\n'.format(board[1][0], board[1][1], board[1][2]),
    '|       |       |       |\n',
    '+-------+-------+-------+\n',
    '|       |       |       |\n',
    '|   {}   |   {}   |   {}   |\n'.format(board[2][0], board[2][1], board[2][2]),
    '|       |       |       |\n',
    '+-------+-------+-------+')     

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            user = 0
            user = int(input('Enter the number of where you would like to play\n--> '))
            if user <= 9 and user >= 0:
                if user in board[0]:
                    if board[0][0] == user:
                        board[0][0] = 'O'
                        break
                    elif board[0][1] == user:
                        board[0][1] = 'O'
                        break
                    elif board[0][2] == user:
                        board[0][2] = 'O'
                        break
                elif user in board[1]:
                    if board[1][0] == user:
                        board[1][0] = 'O'
                        break
                    elif board[1][1] == user:
                        board[1][1] = 'O'
                        break
                    elif board[1][2] == user:
                        board[1][2] = 'O'
                        break
                else:
                    if board[2][0] == user:
                        board[2][0] = 'O'
                        break
                    elif board[2][1] == user:
                        board[2][1] = 'O'
                        break
                    elif board[2][2] == user:
                        board[2][2] = 'O'
                        break
            else:
                print('Spot not available')
        except:
            print('Enter a valid number of one of the listed numbers in the display')
    return board

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = []
    for i, o, p in board[0], board[1], board[2]:
        if isinstance(i, int):
            free_squares.append((0, i))
        if isinstance(o, int):
            free_squares.append((1, o))
        if isinstance(p, int):
            free_squares.append((2, p))
    return(free_squares)
    #  This function was not used, I solved this with the isisntance() function instead

def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    #  Rows X & O
    for i in range(0, 3):
        if board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X':
            print('You Lost! :(')
            return False
        elif board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O':
            print('You Win! :)')
            return False
    #  Columns X & O
    for i in range(0, 3):
        if board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X':
            print('You Lost! :(')
            return False
        elif board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O':
            print('You Win! :)')
            return False
    #  Diagonals X
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        print('You Lost! :(')
        return False
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        print('You Lost! :(')
        return False
    #  Diagonals O
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        print('You Win! :)')
        return False
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        print('You Win! :)')
        return False
    #  Tie we iterate through every element in board and check if they are all strings
    #  if they are through each row our it variable will reach 3 when that happens: game is a Tie
    it = 0
    for i, o, p in board[0], board[1], board[2]:
        if (type(i) == str) and (type(o) == str) and (type(p) == str):
            it += 1
    if it == 3:
        print('Tie! :/')
        return False
    return True

def draw_move(board):
    # The function draws the computer's move and updates the board.
    #  isinstance(x, y) checks if its first argument is of the same type as its second argument
    valid = True
    while valid:
        computer = [randint(0, 2),randint(0, 2)]
        if isinstance(board[computer[0]][computer[1]], int):
            board[computer[0]][computer[1]] = 'X'
            valid = False
    return board

display_board(board)
while victory_for(board):
    enter_move(board)
    display_board(board)
    #  This makes sure the computer doesn't play once you win
    if not victory_for(board):
        break
    draw_move(board)
    display_board(board)
