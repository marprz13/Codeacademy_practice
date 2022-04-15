# Simple Tic Tac Toe terminal game - programming project
from Player_class import Player

# global variables
winner = None
game_on = True

#
player_one = input('What is the name of Player 1?: \n')
player_two = input('What is the name of Player 2?: \n')

player1 = Player(player_one, 'X')
player2 = Player(player_two, 'O')

current_player = player1.sign

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


def view_board():
    print(board[0], '|', board[1], '|', board[2])
    print(board[3], '|', board[4], '|', board[5])
    print(board[6], '|', board[7], '|', board[8])


def play_game():
    view_board()
    while game_on:
        move()
        check_if_game_over()
        flip_player()
    winner_prompt()


def move():
    global current_player
    choice = input('Choose position of your sign: ')
    choice = int(choice) - 1
    board[choice] = current_player
    view_board()


def check_row_win():
    global game_on

    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    if row1 or row2 or row3:
        game_on = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None


def check_column_win():
    global game_on

    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'

    if column1 or column2 or column3:
        game_on = False

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    else:
        return None


def check_diagonal_win():
    global game_on

    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'

    if diagonal1 or diagonal2:
        game_on = False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[1]
    else:
        return None


def check_winner():
    global winner

    row_winner = check_row_win()
    column_winner = check_column_win()
    diagonal_winner = check_diagonal_win()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        return None



def check_if_tied():
    global game_on

    if '-' not in board:
        game_on = False
        return True
    else:
        return False


def check_if_game_over():
    check_winner()
    if check_if_tied():
        print("It's a tie")


def flip_player():
    global current_player
    if current_player == player1.sign:
        current_player = player2.sign
    elif current_player == player2.sign:
        current_player = player1.sign

def winner_prompt():
    if winner == 'X':
        print('Winner of the game is: ' + player1.name)
    elif winner == 'O':
        print('Winner of the game is: ' + player2.name)


play_game()
