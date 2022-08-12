import numpy as np
import random


def print_board(board_array):
    if len(board_array.flatten()) != 9:
        print("Incorrect board array length!")
        exit()

    extra_line = "     |     |"
    new_line = "-----|-----|-----\n"

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


def take_turn(player, current_character, board):

    move = None

    if player == 'r':
        move = computer_random(board)

    elif player == 'f':
        move = computer_rules(board, current_character)

    elif player == 'h':
        move = input(current_character + ", where would you like to go? ")

        while not valid_move(move, board):
            move = input(current_character + ", where would you like to go? ")

    else:
        print("Idk how you got an invalid player type...weird...")
        exit(0)

    update_board(current_character, int(move), board)

    return board, move


def update_board(character, move, board):

    board[move//3][move%3] = character

    return board


def determine_start():

    possible_starts = ['X', 'O']
    choice = random.choice(possible_starts)
    print(choice, "will go first!")

    return choice


def valid_move(move, board):
    try:
        move = int(move)
    except:
        print("That is an invalid move!")
        return False
    if move > 8 or move < 0:
        print("That is an invalid move!")
        return False
    elif board[move//3][move%3] == ' ':
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
    if character == "X":
        ch = 0
    else:
        ch = 1

    if check_rows(board):
        print(character, " has won!")
        return ch
    elif check_columns(board):
        print(character, " has won!")
        return ch
    elif check_diagonals(board):
        print(character, " has won!")
        return ch
    elif ' ' not in board:
        print("It's a tie! No one has won!")
        return 0
    else:
        return -1


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


def computer_random(board):
    empties = np.where(board == ' ')

    possible_moves = 3*empties[0] + empties[1]

    move = random.choice(possible_moves)

    print("Computer has chosen ", move)

    return move


def computer_rules(board, character):
    if character == "O":
        opponent = "X"
    else:
        opponent = "O"

    empties = np.where(board == ' ')

    possible_moves = 3 * empties[0] + empties[1]

    if len(possible_moves) == 9:
        move = random.choice([0, 2, 6, 8])

    elif 4 in possible_moves:
        move = 4

    elif only_diag(possible_moves):
        move = random.choice([1, 3, 5, 7])

    elif two_same(board, character, possible_moves) >= 0:
        move = two_same(board, character, possible_moves)

    elif two_same(board, opponent, possible_moves) >= 0:
        move = two_same(board, opponent, possible_moves)

    elif two_diff(board, possible_moves) >= 0:
        move = two_diff(board, possible_moves)

    else:
        print("Random")
        move = random.choice(possible_moves)

    print("Computer has chosen ", move)

    return move


def only_diag(empties):
    if (set(empties) == {1, 2, 3, 5, 6, 7}) or (set(empties) == {0, 1, 3, 5, 7, 8}):
        return True
    else:
        return False


def two_diff(board, empties):
    move = -1

    d0 = np.array([board[0][0], board[1][1], board[2][2]])
    d1 = np.array([board[0][2], board[1][1], board[2][0]])

    counts = {'r0': (np.count_nonzero(board[0][:] == " "), {0, 1, 2}),
              'r1': (np.count_nonzero(board[1][:] == " "), {3, 4, 5}),
              'r2': (np.count_nonzero(board[2][:] == " "), {6, 7, 8}),
              'c0': (np.count_nonzero(board.transpose()[0][:] == " "), {0, 3, 6}),
              'c1': (np.count_nonzero(board.transpose()[1][:] == " "), {1, 4, 7}),
              'c2': (np.count_nonzero(board.transpose()[2][:] == " "), {2, 5, 8}),
              'd0': (np.count_nonzero(d0 == " "), {0, 4, 8}),
              'd1': (np.count_nonzero(d1 == " "), {2, 4, 6})}

    #print("empties: ", empties)

    for k, v in counts.items():
        if v[0] == 1:
            #print("v1: ", v[1])
            #print("ea: ", empties)
            move = (v[1] & set(empties)).pop()
            print(move)
            break

    return move


def two_same(board, char, empties):
    move = -1

    d0 = np.array([board[0][0], board[1][1], board[2][2]])
    d1 = np.array([board[0][2], board[1][1], board[2][0]])

    counts = {'r0': (np.count_nonzero(board[0][:] == char), {0, 1, 2}),
              'r1': (np.count_nonzero(board[1][:] == char), {3, 4, 5}),
              'r2': (np.count_nonzero(board[2][:] == char), {6, 7, 8}),
              'c0': (np.count_nonzero(board.transpose()[0][:] == char), {0, 3, 6}),
              'c1': (np.count_nonzero(board.transpose()[1][:] == char), {1, 4, 7}),
              'c2': (np.count_nonzero(board.transpose()[2][:] == char), {2, 5, 8}),
              'd0': (np.count_nonzero(d0 == char), {0, 4, 8}),
              'd1': (np.count_nonzero(d1 == char), {2, 4, 6})}

    #print("empties: ", empties)

    #print("counts: ", counts)

    for k, v in counts.items():
        if v[0] == 2:
            #print("key: ", k)
            #print("v1: ", v[1])
            #print("ea: ", empties)
            possible = v[1] & set(empties)
            if len(possible) != 0:
                move = possible.pop()
            #print(move)
            break

    # print(r0, r1, r2)
    # print(c0, c1, c2)

    return move


def gameStats(games, player=1):
    if player == 1:
        character = "X"
    else:
        character = "O"
    stats = {"win": 0, "loss": 0, "draw": 0}
    for game in games:
        result = check_win(character, game)
        if result == -1:
            continue
        elif result == player:
            stats["win"] += 1
        elif result == 0:
            stats["draw"] += 1
        else:
            stats["loss"] += 1

    winPct = stats["win"] / len(games) * 100
    lossPct = stats["loss"] / len(games) * 100
    drawPct = stats["draw"] / len(games) * 100

    print("Results for player %d:" % (player))
    print("Wins: %d (%.1f%%)" % (stats["win"], winPct))
    print("Loss: %d (%.1f%%)" % (stats["loss"], lossPct))
    print("Draw: %d (%.1f%%)" % (stats["draw"], drawPct))

def play_game():
    history = []

    print("The board spaces are numbered as follows: ")

    board_options = np.array([['0', '1', '2'],
                              ['3', '4', '5'],
                              ['6', '7', '8']])

    print_board(board_options)

    print("\nThe game options are as follows: ")
    print("\t[1]\t Human vs Human")
    print("\t[2]\t Human vs Random Computer")
    print("\t[3]\t Human vs First Move Computer")
    print("\t[4]\t Random Computer vs First Move Computer")

    while True:
        game_option = int(input("Which game option would you like to play? "))

        if game_option == 1:
            player_type = ['h', 'h']
            break
        elif game_option == 2:
            player_type = ['h', 'r']
            break
        elif game_option == 3:
            player_type = ['h', 'f']
            break
        elif game_option == 4:
            player_type = ['r', 'f']
            break
        else:
            print("Invalid option selected.")
            continue

    board = init_board()

    character = determine_start()

    og_pt = player_type

    if character == 'O':
        player_type = player_type[::-1]

    play = True

    while play:
        take_turn(player_type[0], character, board)

        print_board(board)

        history.append((character, board))

        if check_win(character, board) >= 0:
            again = input("Would you like to play again? [Y/N]")

            if (again == 'Y') or (again == 'y'):
                print("Resetting board")
                board = init_board()
                character = determine_start()
                if character == 'O':
                    player_type = og_pt[::-1]
                else:
                    player_type = og_pt
                continue

            elif (again == 'N') or (again == 'n'):
                print("Thanks for playing!")
                play = False

            else:
                print("Thanks for playing!")
                play = False

        character = switch_character(character)

        player_type = player_type[::-1]


if __name__ == "__main__":
    play_game()


