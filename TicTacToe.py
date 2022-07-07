import numpy as np
import random


def print_board(board_array):
    if len(board_array.flatten()) != 9:
        print("Incorrect board array length!")
        exit()

    extra_line = "     |     |"
    new_line = "\n-----|-----|-----\n"

    print(extra_line)
    print(" ", board_array[0][0], " | ", board_array[0][1], " | ", board_array[0][2])
    print(new_line)
    print(" ", board_array[1][0], " | ", board_array[1][1], " | ", board_array[1][2])
    print(new_line)
    print(" ", board_array[2][0], " | ", board_array[2][1], " | ", board_array[2][2])
    print(extra_line)


def init_board():
    new_board = np.array([[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']])

    return new_board


def take_turn(current_character, board):

    move = input(current_character + ", where would you like to go? ")

    while not valid_move(int(move), board):
        move = input(current_character + ", where would you like to go? ")

    update_board(current_character, int(move), board)

    return board


def update_board(character, move, board):

    board[move//3][move%3] = character

    return board


def determine_start():

    possible_starts = ['X', 'O']
    choice = random.choice(possible_starts)
    print(choice, "will go first!")

    return choice


def valid_move(move, board):
    if board[move//3][move%3] == ' ':
        return True
    elif board[move//3][move%3] == 'X':
        print("There is already and X there!")
        return False
    elif board[move//3][move%3] == 'O':
        print("There is already an O there!")
        return False
    else:
        print("That is an invalid move!")
        return False


def check_win(character, board):
    if check_rows(board):
        print(character, " has won!")
        return True
    elif check_columns(board):
        print(character, " has won!")
        return True
    elif check_diagonals(board):
        print(character, " has won!")
        return True
    elif ' ' not in board:
        print("It's a tie! No one has won!")
        return True
    else:
        return False


def check_rows(board):

    for i in range(3):
        if board[i][0] == ' ':
            continue
        elif (board[i][0] == board[i][1]) and (board[i][0] == board[i][2]):
            return True

    return False


def check_columns(board):
    for i in range(3):
        if board[0][i] == ' ':
            continue
        elif (board[0][i] == board[1][i]) and (board[0][i] == board[2][i]):
            return True
    return False


def check_diagonals(board):
    if board[1][1] == ' ':
        return False
    elif (board[0][0] == board[1][1]) and (board[0][0] == board[2][2]):
        return True
    elif (board[0][2] == board[1][1]) and (board[0][2] == board[2][0]):
        return True
    else:
        return False


def switch_character(character):
    if character == 'O':
        return 'X'
    elif character == 'X':
        return 'O'
    else:
        "Uhhhh that's not valid..."
        exit(0)


def play_game():
    print("Starting")

    board_options = np.array([['0', '1', '2'],
                              ['3', '4', '5'],
                              ['6', '7', '8']])

    print_board(board_options)

    board = init_board()

    win = False

    character = determine_start()

    while not win:
        take_turn(character, board)
        print_board(board)

        if check_win(character, board):
            again = input("Would you like to play again? [Y/N]")

            if (again == 'Y') or (again == 'y'):
                print("Resetting board")
                board = init_board()
                character = determine_start()

            elif (again == 'N') or (again == 'n'):
                print("Thanks for playing!")
                exit(0)

        character = switch_character(character)


if __name__ == "__main__":
    play_game()


