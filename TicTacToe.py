import numpy as np
import random


def play_game():
    print("Let's play TicTacToe!")

    board_options = np.array([['a', 'b', 'c'],
                              ['f', 'e', 'd'],
                              ['g', 'h', 'i']])

    print_board(board_options)

    board = init_board()

    win = False

    character = determine_start()

    while not win:

        take_turn(character, board)

        print_board(board)

        if check_win(character, board):
            again = input("Would you like to play again? [Y/N]")

            if again == 'Y' or again == 'y':
                print("Resetting board")
                board = init_board()
                character = determine_start()
            else:
                print("Thanks for playing!")
                exit(0)
        else:
            character = switch_character(character)


def switch_character(current_character):
    if current_character == "X":
        return "O"
    else:
        return "X"


def take_turn(current_character, board):

    move = input(current_character + ", where would you like to go? ")

    while not valid_move(int(move), board):
        move = input(current_character + ", where would you like to go? ")

    new_board = update_board(current_character, board, int(move))

    return new_board


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
    elif " " not in board:
        print("It's a tie! No one has won!")
        return True
    else:
        return False


def check_rows(board):

    for i in range(3):
        if board[i][0] == " ":
            continue
        elif (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]):
            return True

    return False


def check_columns(board):
    for i in range(3):
        if board[0][i] == " ":
            continue
        elif (board[0][i] == board[1][i]) and (board[1][i] == board[2][i]):
            return True

    return False


def check_diagonals(board):
    if board[1][1] == " ":
        return False
    elif (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
        return True
    elif (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]):
        return True
    else:
        return False


def update_board(character, board, move):
    board[move//3][move%3] = character
    return board


def valid_move(move, current_board):
    if move > 8:
        print("That is an invalid move!")
        return False
    elif current_board[move//3][move%3] == " ":
        return True
    elif current_board[move//3][move%3] == "X":
        print("There is already an X there!")
        return False
    elif current_board[move//3][move%3] == "O":
        print("There is already an O there!")
        return False
    else:
        print("That is an invalid move!")
        return False


def determine_start():
    possible_starts = ['X', 'O']
    choice = random.choice(possible_starts)
    print(choice, "will go first!")

    return choice

def init_board():
    new_board = np.array([[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']])

    return new_board

def print_board(board):

    new_line = "-----------------"

    print("\n ", board[0][0], " | ", board[0][1], " | ", board[0][2])
    print(new_line)
    print(" ", board[1][0], " | ", board[1][1], " | ", board[1][2])
    print(new_line)
    print(" ", board[2][0], " | ", board[2][1], " | ", board[2][2], "\n")



if __name__ == "__main__":
    play_game()