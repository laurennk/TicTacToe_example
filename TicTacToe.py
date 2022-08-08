import numpy as np
import random


def print_board(board_array):
    print("Printing board")

    extra_line = "     |     |"
    new_line = "\n-----|-----|-----\n"
    
    print(extra_line)
    print(" ", board_array[0][0], " | ", board_array[0][1], " | ", board_array[0][2])
    print(new_line)
    print(" ", board_array[1][0], " | ", board_array[1][1], " | ", board_array[1][2])
    print(new_line)
    print(" ", board_array[2][0], " | ", board_array[2][1], " | ", board_array[2][2])
    print(extra_line)

    return


def init_board():
    print("Initializing a new board")
    board = np.array([[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]])

    return board


def take_turn(current_character, board):
    print("Starting turn")

    # placeholder
    move = input(current_character + " what is your move?")

    # check if the move is valid
    while not valid_move(int(move), board):
        move = input("That is not a valid move. Try again:")

    # update board
    update_board(current_character, int(move), board)


def update_board(character, move, board):
    print("Updating the board")
    
    board[move//3][move%3] = character


def determine_start():
    print("Determining the start of the game")

    possible_start = ['X', 'O']
    choice = random.choice(possible_start)

    return choice


def valid_move(move, board):
    print("Checking if the move is valid")

    if move > 8:
        return False
        
    if board[move//3][move%3] == ' ':
        return True
    elif board[move//3][move%3] == 'X':
        print("There is an X there!")
        return False
    else:
        print("There is an O there!")
        return False


def check_win(character, board):
    print("Checking if the game has been won")

    win = check_rows(board)
    print("Rows", win)
    if win == False:
        win = check_columns(board)
        print("Columns", win)
    if win == False:
        win = check_diagonals(board)
        print("Diag", win)
    if ' ' not in board:
        print("It's a tie! No one has won!")
        return True

    print(win)
    return win


def check_rows(board):
    print("Checking rows")

    for i in range(3):
        if board[i][0] == " ":
            continue
        elif (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]):
            return True

    return False



def check_columns(board):
    print("Checking columns")
    for i in range(3):
        if board[0][i] == " ":
            continue
        elif (board[0][i] == board[1][i]) and (board[1][i] == board[2][i]):
            return True
    return False

def check_diagonals(board):
    print("Checking diagonals")
    if board[1][1] == " ":
        return False
    elif (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
        return True
    elif (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]):
        return True
    else:
        return False



def switch_player(character):
    print("Switching player")
    if character == 'X':
        character = 'O'
    else:
        character = 'X'

    return character


def play_game():
    print("Entering play game")

    # declare the board options
    board_options = np.array([['0', '1', '2'],
                              ['3', '4', '5'],
                              ['6', '7', '8']])

    # print the board options
    print_board(board_options)

    # initialize the board
    board = init_board()

    # keep track of if the game has been won
    win = False

    # determine how the game will be started
    player = determine_start()

    print("Player " + player + " will start the game")

    # while the game has not been won stay inside of a loop
    while not win:
        # take turns
        take_turn(player, board)

        # print the board after each turn
        print_board(board)

        # check if the  game has been won after each turn
        if check_win(player, board):
            # if the game has been won, ask if they would like to play again
            again = input("Would you like to play again? [Y/N]")

            # if they would like to play again...
            if (again == 'Y') or (again == 'y'):
                # reset the board
                print("Resetting board")
                board = init_board()

                # determine how the game will be started
                player = determine_start()

            # if they would not like to play again...
            elif (again == 'N') or (again == 'n'):
                # exit the program
                print("Thanks for playing!")
                exit(0)

        # swap which players turn it is at the end of each turn
        player = switch_player(player)
        
        


if __name__ == "__main__":
    play_game()


