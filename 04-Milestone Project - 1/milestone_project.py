""" OLD TEST CODE
#find positions corresponding to X and O placement
for token in ['X','O']:
    first = []
    second = []
    third = []
    for position,row in positions.items():
        if row[0] == token:
            first.append(position)
        if row[2] == token:
            second.append(position)
        if row[4] == token:
            third.append(position)
    if token == 'X':
        X_pos = [first,second,third]
    elif token == 'O':
        O_pos = [first,second,third]





def is_impossible(win):
    tokens = ''
    for position in win:
        tokens += positions[position]
    count = Counter(tokens)
    return count['X']-count['O'] > 1 

#create wins list
player1_wins = []
player2_wins = []


#diagonal left to right wins
def diagonal_left(rows):
    diagonal_left_wins = []
    for position in rows[0]:
        for position_2 in rows[1]:
            for position_3 in rows[2]:
                win = [position,position_2,position_3]
                #remove impossible boards
                if is_impossible(win) == False:
                    diagonal_left_wins.append(win)

#diagonal right to left wins
def diagonal_right(rows):
    diagonal_right_wins = []
    for position in rows[2]:
        for position_2 in rows[1]:
            for position_3 in rows[0]:
                win = [position,position_2,position_3]
                #remove impossible boards
                if is_impossible(win) == False:
                    diagonal_right_wins.append(win)

#vertical wins
def vertical(rows):
    vertical_wins = []
    for row in range(0,3):
        for position in rows[row]:
            for position_2 in rows[row]:
                for position_3 in rows[row]:
                    win = [position,position_2,position_3]
                    #remove impossible boards
                    if is_impossible(win) == False:
                        vertical_wins.append(win)

#horizontal
def horizontal(rows):
    horizontal_wins = []
    for row, position in positions.items():
        if position[0] == position[2] == position[4]:
            winning_row = row
    
            if is_impossible(win) == False:
                horizontal_wins.append(win)

#vertical wins"""

"""
#wins where X last on top row
for position in O_pos[2]:
    for position_2 in O_pos[1]:
        for position_3 in O_pos[0]:
            win = [position,position_2,position_3]
            #remove impossible boards
            if is_impossible(win) == False:
                player2_wins.append(win)
#vertical wins
for row in range(0,3):
    for position in O_pos[row]:
        for position_2 in O_pos[row]:
            for position_3 in O_pos[row]:
                win = [position,position_2,position_3]
                #remove impossible boards
                if is_impossible(win) == False:
                    player2_wins.append(win)




#remove duplicates
player1_wins = list(set(map(tuple,player1_wins)))
player2_wins = list(set(map(tuple,player2_wins)))

#remove boards where both players win
both_win = list(set(player1_wins).intersection(player2_wins))
player1_wins = [win for win in player1_wins if win not in both_win]
player2_wins = [win for win in player2_wins if win not in both_win]



"""



#Game set-up: possible playing positions, empty game board

def game_board():
    print('\n')
    print('1|2|3')
    print('_ _ _')
    print('4|5|6')
    print('_ _ _')
    print('7|8|9')
    print('\n')


def board(row1,row2,row3):
    print('\n')
    print(row1)
    print('_ _ _')
    print(row2)
    print('_ _ _')
    print(row3)
    print('\n')




def player(row1,row2,row3):
    """ Ask for player's posiiton choice """
    choice = 'init'
    acceptable_range = range(1,10)
    within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input('Choose a place to play: ')
        if choice.isdigit() == False:
            print('Not on board')
        else:
            if int(choice) in acceptable_range:
                if acceptable_move(choice,row1,row2,row3):
                    within_range = True
                else:
                    print('Space already taken')
            else:
                print('Not on board')
    return int(choice)

def acceptable_move(choice, row1, row2, row3):
    """ check that chosen position is free to play """
    rows = row1+row2+row3
    game_board_dict = {1: 0, 2: 2, 3: 4, 
                   4: 5, 5: 7, 6: 9,
                   7: 10, 8: 12, 9: 14}
    if rows[game_board_dict[int(choice)]] == ' ':
        return True
    else:
        return False



def update_board(choice,row1,row2,row3,player):
    """ Update the board with the players choice """
    row1 = list(row1)
    row2 = list(row2)
    row3 = list(row3)
    game_board_dict = {1: 0, 2: 2, 3: 4, 
                   4: 0, 5: 2, 6: 4,
                   7: 0, 8: 2, 9: 4}
    if choice in range(1,4):
        row1[game_board_dict[choice]] = player
    elif choice in range(4,7):
        row2[game_board_dict[choice]] = player
    elif choice in range(7,10):
        row3[game_board_dict[choice]] = player
    return ''.join(row1),''.join(row2),''.join(row3)


""" Set up possible winning boards """

from collections import Counter
from itertools import combinations, permutations

#possible row configurations
positions = {1: ' | | ', 2: ' | |X', 3: ' | |O',
             4: ' |X| ', 5: ' |X|X', 6: ' |X|O',
             7: ' |O| ', 8: ' |O|X', 9: ' |O|O',
             10: 'X| | ', 11: 'X| |X', 12: 'X| |O',
             13: 'O| | ', 14: 'O| |X', 15: 'O| |O',
             16: 'X|X| ', 17: 'X|X|X', 18: 'X|X|O',
             19: 'X|O| ', 20: 'X|O|X', 21: 'X|O|O',
             22: 'O|X| ', 23: 'O|X|X', 24: 'O|X|O',
             25: 'O|O| ', 26: 'O|O|X', 27: 'O|O|O'}


def is_impossible(board):
    """ define impossible boards: players should
    have played an equal number of times or X one more as X plays first"""
    tokens = ''
    for position in board:
        tokens += positions[position]
    count = Counter(tokens)
    return count['X']-count['O'] > 1

assert is_impossible((14,9,17)) == False


# set up list of possible boards
boards = permutations(positions.keys(),3)
possible_boards = [board for board in boards if is_impossible(board) == False]


def possible_win(board):
    """ check if a win is possible at this point in the game, 
    i.e. X has played at least 3 times"""
    tokens = ''
    for position in board:
        tokens += positions[position]
    count = Counter(tokens)
    return count['X'] >= 3

assert possible_win((19,6,2)) == True

# set up list of boards where a win could be possible (i.e. sufficient number of moves played)
possible_to_win = [board for board in possible_boards if possible_win(board) == True]


# functions to define different types of win. All functions return the winning token if a win has occured.
def diagonal_win(rows):
    if rows[0][0] == rows[1][2] == rows[2][4] and rows[0][0] != ' ':
        return rows[1][2]
    elif rows[0][4] == rows[1][2] == rows[2][0] and rows[0][4] != ' ':
        return rows[1][2]
    else:
        return False
    
def vertical_win(rows):
    for i in range(0,5,2):
        if rows[0][i] == rows[1][i] == rows[2][i] and rows[0][i] != ' ': 
            return rows[0][i]
    return False 

def horizontal_win(rows):
    for row in rows:
        if row[0] == row[2] == row[4] and row[0] != ' ':
            return row[0]
    return False


def is_win(board):
    """ check if a board contains any wins. If more than one 'win' reject as impossible """
    rows = [positions[board[i]] for i in range(0,3)]
    diagonal = diagonal_win(rows)
    vertical= vertical_win(rows)
    horizontal = horizontal_win(rows)
    wins = [diagonal, vertical, horizontal]
    win_count = Counter(wins)
    if win_count[False] == 1 or win_count[False] == 0:
        return False 
    elif diagonal != False:
        return diagonal
    elif vertical != False:
        return vertical
    elif horizontal != False:
        return horizontal
    else:
        return False

  
assert is_win((8,1,1)) == False
assert is_win((19,22,2)) == 'X'
assert is_win((24,23,8)) == False
assert is_win((19,6,2)) == 'X'
    
#set up dictionary of winning boards with correspoding win token
winning_boards = {board: is_win(board) for board in possible_to_win if is_win(board) != False}

test_board = (19,6,2)
test_win = {test_board: is_win(test_board)}
#print(test_win)
       
assert (19,6,2) in winning_boards

     
            
      
#convert set of rows into positional tuple
def rows_to_positions(row1,row2,row3):
    positions_inverted = {value: key for key,value in positions.items()}
    return (positions_inverted[row1],positions_inverted[row2],positions_inverted[row3])
        

def turn(row1,row2,row3,player_num):
    """ enacts the players turn """
    if player_num == 1:
        token = 'X'
    elif player_num == 2:
        token = 'O'
    choice = player(row1, row2, row3)
    row1, row2, row3 = update_board(choice, row1, row2, row3, token)
    board(row1,row2,row3)
    
    return row1,row2,row3


def check_win(board):
    """ checks if the current board is a win. 
    Stops the game if this is the case and returns the winning player """
    if board in winning_boards:
        if winning_boards[board] == 'X':
            print('Player 1 wins!')
        elif winning_boards[board] == 'O':
            print('Player 2 wins!')
        playing = False
    else:
        playing = True
    return playing


def replay():
    answer = False
    while answer == False:
        replay = input('Play again? (yes/no): ').lower()
        if replay == 'yes' or replay == 'no':
            answer = True
        else:
            print('Answer not understood')  
    return replay
        

def tictactoe_game():

    """ A game of tic tac toe for 2 players working at the same computer """

    # show players board set-up
    game_board()
    # set up game and display empty game board
    row1 = ' | | '
    row2 = ' | | '
    row3 = ' | | '
    board(row1, row2, row3)
    playing = True
    turn_number = 0
    while playing:
        #player1
        print("Player 1's Turn")
        row1, row2, row3 = turn(row1, row2, row3, 1)
        turn_number += 1
        #check if win
        board_status = rows_to_positions(row1,row2,row3)
        playing = check_win(board_status)
        # if board full or win, end game
        if turn_number == 9 and playing == True:
            print('Game Over: draw')
            break
        elif playing == False:
            break
        #player2
        print("Player 2's Turn")
        row1, row2, row3 = turn(row1, row2, row3, 2)
        turn_number += 1
        #check if win
        board_status = rows_to_positions(row1,row2,row3)
        playing = check_win(board_status)

    print('\nFinal board is: ')
    board(row1, row2, row3)

    
    
#Run game

again = 'yes'
while again == 'yes':
    tictactoe_game()
    again = replay()
    




""" Alternative coding
def tictactoe2():
           
    # show players board set-up
    game_board()
    # set up game and display empty game board
    row1 = ' | | '
    row2 = ' | | '
    row3 = ' | | '
    board(row1, row2, row3)
    playing = True
    turn_number = 0
    while playing:
        for i in range(1,3):
            print(f"Player {i}'s Turn")
            row1, row2, row3 = turn(row1, row2, row3, i)
            turn_number += 1
            #check if win
            board_status = rows_to_positions(row1,row2,row3)
            playing = check_win(board_status)
            if turn_number == 9 and playing == True:
                print('Game Over: draw')
                break
            elif playing == False:
                break
        
        
    print('Final board is: ')
    board(row1, row2, row3)


#tictactoe2() """

