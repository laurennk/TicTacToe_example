import numpy as np
import random


def print_board(board_array):
    print("Printing board")

    # if len(board_array.flatten()) != 9:
    #     print("Incorrect board array length!")
    #     exit()

    # extra_line = "     |     |"
    # new_line = "\n-----|-----|-----\n"
    # 
    # print(extra_line)
    # print(" ", board_array[0][0], " | ", board_array[0][1], " | ", board_array[0][2])
    # print(new_line)
    # print(" ", board_array[1][0], " | ", board_array[1][1], " | ", board_array[1][2])
    # print(new_line)
    # print(" ", board_array[2][0], " | ", board_array[2][1], " | ", board_array[2][2])
    # print(extra_line)


def init_board():
    print("Initializing a new board")


def take_turn(current_character, board):
    print("Starting turn")

    # placeholder
    move = 0

    # check if the move is valid
    while not valid_move(int(move), board):
        break

    # update board
    update_board(current_character, int(move), board)


def update_board(character, move, board):
    print("Updating the board")


def determine_start():
    print("Determining the start of the game")


def valid_move(move, board):
    print("Checking if the move is valid")


def check_win(character, board):
    print("Checking if the game has been won") 


def check_rows(board):
    print("Checking rows") 


def check_columns(board):
    print("Checking columns")

def check_diagonals(board):
    print("Checking diagonals")



def switch_player(character):
    print("Switching player")


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
        
        exit(0)


if __name__ == "__main__":
    play_game()


