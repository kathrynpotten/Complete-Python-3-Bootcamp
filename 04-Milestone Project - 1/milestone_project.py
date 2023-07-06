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





def game_board():
    print('1|2|3')
    print('_ _ _')
    print('4|5|6')
    print('_ _ _')
    print('7|8|9')


def board(row1,row2,row3):
    print(row1)
    print('_ _ _')
    print(row2)
    print('_ _ _')
    print(row3)


def player():
    choice = 'init'
    acceptable_range = range(1,10)
    within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input('Choose a place to play: ')
        if choice.isdigit() == False:
            print('Not on board')
        else:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Not on board')
    return int(choice)

def update_board(choice,row1,row2,row3,player):
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

#define impossible boards
def is_impossible(win):
    tokens = ''
    for position in win:
        tokens += positions[position]
    count = Counter(tokens)
    return count['X']-count['O'] > 1 or count['X'] < 3

assert is_impossible((14,9,17)) == False

#possible boards
boards = permutations(positions.keys(),3)
possible_boards = [board for board in boards if is_impossible(board) == False]

#wins
def is_win(board):
    win = False
    winning_token = ''
    if board not in possible_boards:
        return False
    rows = [positions[board[i]] for i in range(0,3)]
    #horizontal
    for row in rows:
        if row[0] == row[2] == row[4]:
            win = True
            winning_token =  row[0]
    #diagonal
    if rows[0][0] == rows[1][2] == rows[2][4]:
        win = True
        winning_token = row[0][0]
    if rows[0][4] == rows[1][2] == rows[2][0]:
        win = True
        winning_token = rows[0][4]
    #vertical
    for i in range(0,3):
        if rows[0][i] == rows[1][i] == rows[2][i]:
            win =  True
            winning_token = rows[0][i]

    return win, winning_token
        
#assert is_win((8,1,1))[0] == False

def rows_to_positions(row1,row2,row3):
    positions_inverted = {value: key for key,value in positions.items()}
    return (positions_inverted[row1],positions_inverted[row2],positions_inverted[row3])
        

def turn(row1,row2,row3,player_num):
    if player_num == 1:
        token = 'X'
    elif player_num == 2:
        token = 'O'
    choice = player()
    row1, row2, row3 = update_board(choice, row1, row2, row3, token)
    board(row1,row2,row3)
    
    return row1,row2,row3


def check_win(board_status,turn_number):
    win, winning_token = is_win(board_status)
    print(winning_token)
    if win == True:
        #check winner
        #if winning_token == 'X':
        #    winner = 1
        #elif winning_token == 'O':
        #    winner = 2
    #confirm win and break game if finished
       # print(f'Player {winner} wins!')
        playing = False
    elif win == False and turn_number <= 9:
        playing = True
    elif win == False:
        print('Game over: draw')
        playing = False
    return playing


def tictactoe():

    """ A game of tic tac toe for 2 players working at the same computer """

    # show players board set-up
    game_board()
    # set up game
    row1 = ' | | '
    row2 = ' | | '
    row3 = ' | | '
    print('\n\n')
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
        playing = check_win(board_status, turn_number)
        if playing == False:
            break
        #player2
        print("Player 2's Turn")
        row1, row2, row3 = turn(row1, row2, row3, 2)
        turn_number += 1
        #check if win
        board_status = rows_to_positions(row1,row2,row3)
        playing = check_win(board_status, turn_number)
        
    print('Final board is: ')
    board(row1, row2, row3)

    
    



tictactoe()
    

        




