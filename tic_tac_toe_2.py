import os

A1,A2,A3,A4,A5,A6,A7,A8,A9 = '_','_','_','_','_','_','_','_','_'
list_pl = []
round_num = 0

def image():
    figure = '''
{}|{}|{}    1|2|3
{}|{}|{}    4|5|6
{}|{}|{}    7|8|9
'''.format(A1,A2,A3,A4,A5,A6,A7,A8,A9)
    print(figure)
# Assigning position and defining the board after each turn

def move(choice, n):
    global A1,A2,A3,A4,A5,A6,A7,A8,A9
    if n%2 != 0:      # Checks the turn number and returns 'X' or 'O'
        symbol = 'X'
    else:
        symbol = 'O'
    position =  'A' + str(choice) # Converts the position to string
    globals()[position] = symbol  # Converts string to a variable and then assigns value EXAMPLE A2 = 'X'

# Changes the board after each turn

def win(player):
    list_win = [[A1,A2,A3], [A4,A5,A6], [A7,A8,A9], [A1,A4,A7], [A2,A5,A8], [A3,A6,A9], [A1,A5,A9], [A3,A5,A7]]
    for i in list_win:
        if i[0] == '_':
            result = False
        else:
            result = (i.count(i[0]) == len(i))
            if result == True:
                print(player, 'wins')
                break
            else:
                result == False
    return result
 # Checking whether the player has won or not by checking the board position

print('Player 1 = X')
print('Player 2 = O')
print('''
Please give the input between 1 to 9
''')
image()

while True:
    round_num += 1
    if round_num % 2 == 0:
        player = 'Player 2'
    else:
        player = 'Player 1'
    while True:
        player_choice = int(input('{} Where is your move: '.format(player)))
        result = (player_choice in list_pl) # Checks whether already played or not
        if result == True:
            print('Already Played')
        elif result == False and player_choice<10:
            move(player_choice, round_num)
            os.system('cls')
            image()   # Prints the board
            list_pl.append(player_choice) # Appends the already palyed position to a list
            break
        else:
            print('Something went wrong')
    a = win(player) # Checking whether the player has won or not
    if a == True:
        break
    if round_num == 9:
        print('Tie')
        break

