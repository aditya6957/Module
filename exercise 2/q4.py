'''
A Tic-Tac-Toe game using Python
'''
import os

from q4 import C_WIN

def print_board(game_input):
    '''
    Function to create board
    '''
    # Printing Board By using gameValues 's List
    print([game_input[0], game_input[1], game_input[2]])
    print([game_input[3], game_input[4], game_input[5]])
    print([game_input[6], game_input[7], game_input[8]])

def check_winner(game_input):
    '''
    Function to check winner or draw
    '''
    # All Winning Patterns
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        # if gameValues matches with the pattern and has X then X won the Match
        if game_input[win[0]] == game_input[win[1]] == game_input[win[2]] == 'X':
            print_board(game_input)
            print("X Won the match")
            return 1

        # if gameValues matches with the pattern and has X then O won the Match
        if game_input[win[0]] == game_input[win[1]] == game_input[win[2]] == 'O':
            print_board(game_input)
            print("O Won the match")
            return 0

        # if all places are filled and no one is the winner
        if all(isinstance(item, str) for item in game_input):
            print_board(game_input)
            return -2
    # return -1 if no one wons
    return -1

if __name__ == '__main__':
    print("Welcome to the Game")
    game_values=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    CHANCE = 1

    while True:
        try:
            if CHANCE == 1:
                print_board(game_values)
                print("\nX's turn")
                value = int(input("\nPlease enter a value: "))
                value = value - 1

                # check if already filled with O
                if game_values[value]!= 'O':
                    game_values[value] = 'X'
                else:
                    os.system('CLS')
                    print("\nPlease Enter Different Location for X")
                    continue
                os.system('CLS')

            if CHANCE == 0:
                print_board(game_values)
                print("\nO's turn")
                value = int(input("\nPlease enter a value: "))
                value = value - 1

                # check if already filled with X
                if game_values[value]!= 'X':
                    game_values[value] = 'O'
                else:
                    os.system('CLS')
                    print("\nPlease Enter Different Location for O")
                    continue
                os.system('CLS')

        except IndexError:
            # exception if Value is not between 1 to 9
            os.system('CLS')
            print("\nOops!! Please Enter value from 1 - 9\n")
            continue

        # for giving CHANCE to other player
        CHANCE = 1 - CHANCE
        C_WIN = check_winner(game_values)
        # Game Draw
        if C_WIN == -2:
            print("Game Draw")
            break
        # Match Over
        if C_WIN != -1:
            print("Match over")
            break
