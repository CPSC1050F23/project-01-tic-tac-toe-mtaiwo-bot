"""
Author: Folu Taiwo
Psuedocode partner: Tori Fazio
Date: 10/4/2023
Assignment: tic tac toe
Course: CPSC1050

"""
def init_board():
    board = [['' for i in range(3)] for j in range(3)]
    return board

board = init_board()

def print_board(board):
    # create a string
    output_string = ""
    #iterate through outer list (rows)
    for row in board:
        output_string += "|"
        #iterate through inner list (cols)
        for col in row:
            #process and format board content and add to string
            if col == "":
                output_string += f" _ |"
            else:
                output_string += f" {col} |"
        
        output_string += "\n"
    #return the formatted 2d list as a string
    print(output_string)


def update_board(board, row, col, player):
    if board[row][col] == "":
        board[row][col] = player
    else:
        print("That spot is full!")
        print(f"Enter row and column for player {player}")
        get_move(player)

def get_move(player):
    while True:
        move = input()
        move = move.split()
        
        if not all(char.isdigit() or char.isspace() for char in move):
            print("Please enter valid row and col numbers from 1 to 3:")
            continue

        if len(move) != 2:
            print("Please enter valid row and col numbers from 1 to 3:")
            continue
        
        row, col = int(move[0]) - 1, int(move[1]) - 1
        if 0 <= row <= 2 and 0 <= col <= 2:
            return row, col
        else:
            print("Please enter valid row and col numbers from 1 to 3:")
        
def player_move(board, player):
    while True:
        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == "":
            board[row][col] = player
            break

def start_game():
    print("Let's play Tic-Tac-Toe!")
    print("When prompted, enter desired row and column numbers")
    print("Example: 1 3")
    print()
    update_board(board,0,2,'X')
    print_board(board)
    print()
    print("Let's play!")
    print("Player X starts!")

def check_tie(board):
    for row in board:
        if "" in row:
            return False
    return True

def check_win(board, player):
    #Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    #Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    
    #Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_complete(board):
    for row in board:
        if "" in row:
            return False
    return True

def play_again():
    while True:
        print("Do you want to play again? Y or N")
        response = input().lower().strip()
        if response in 'y':
            print("Let's play Tic-Tac-Toe!")
            print("When prompted, enter desired row and column numbers")
            print("Example: 1 3")
            print()
            update_board(board,0,2,'X')
            print_board(board)
            print()
            print("Let's play!")
            print("Player X starts!")
            print()
            play()
        elif response in 'n':
            exit(0)
        else:
            print("Please enter valid input: Y or N")

def play():
    board = init_board()
    print_board(board)
    while True:
        player = 'X'

        for i in range(9):
            print(f"Enter row and column for player {player}")
            row, col = get_move(player)
            update_board(board, row, col, player)
            print()
            print_board(board)

            if check_tie(board):
                print("It's a TIE!")
                print("Do you want to play again? Y or N")
                play_again()
                
            if check_win(board, 'X'):
                print("Player X WINS!")
                break
            elif check_win(board, 'O'):
                print("Player O WINS!")
                break
            
            if check_complete(board):
                break

            player = 'O' if player == 'X' else 'X'
        
        if play_again():
            return

start_game()
print()
play()