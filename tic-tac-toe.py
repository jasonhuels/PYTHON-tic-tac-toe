__author__ = 'Jason_Huels'

# Inputs: value, play, done
# Outputs: board, prompt

# import the random library
import random

# Function Integer input_num(String prompt, Integer[] used):

def input_num(prompt, used):
    done = False
    value = 0

    while not done:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid selection. Please try again.")
            continue
        if value < 1 or value > 9:
            print("That number is out of range, try again.")
            done = False
        elif value != 0 and used[value] == value:
            print("That space is full, try again.")
            done = False
        else:
            done = True

    return value


# Function input_comp(String[] board, Integer[] used):

def input_comp(board, used):
    done = False
    value = 0

# top row
    if board[1] == board[2] and used[3] == 0:
        value = 3
    elif board[1] == board[3] and used[2] == 0:
        value = 2
    elif board[2] == board[3] and used[1] == 0:
        value = 1
# middle row
    elif board[4] == board[5] and used[6] == 0:
        value = 6
    elif board[4] == board[6] and used[5] == 0:
        value = 5
    elif board[5] == board[6] and used[4] == 0:
        value = 4
# bottom row
    elif board[7] == board[8] and used[9] == 0:
        value = 9
    elif board[7] == board[9] and used[8] == 0:
        value = 8
    elif board[8] == board[9] and used[7] == 0:
        value = 7
# first column
    elif board[1] == board[4] and used[7] == 0:
        value = 7
    elif board[1] == board[7] and used[4] == 0:
        value = 4
    elif board[7] == board[4] and used[1] == 0:
        value = 1
# second column
    elif board[2] == board[5] and used[8] == 0:
        value = 8
    elif board[2] == board[8] and used[5] == 0:
        value = 5
    elif board[5] == board[8] and used[2] == 0:
        value = 2
# third column
    elif board[3] == board[6] and used[9] == 0:
        value = 9
    elif board[3] == board[9] and used[6] == 0:
        value = 6
    elif board[9] == board[6] and used[3] == 0:
        value = 3
# diagonals
    elif board[1] == board[5] and used[9] == 0:
        value = 9
    elif board[1] == board[9] and used[5] == 0:
        value = 5
    elif board[9] == board[5] and used[1] == 0:
        value = 1
    elif board[3] == board[5] and used[7] == 0:
        value = 7
    elif board[3] == board[7] and used[5] == 0:
        value = 5
    elif board[7] == board[5] and used[3] == 0:
        value = 3
    else:
        while not done:
            value = random.randint(1, 9)
            if value != 0 and used[value] == value:
                done = False
            elif value < 1 or value > 9:
                done = False
            else:
                done = True
    return value


# Module draw_board(String Array board):

def draw_board(board):
    print(board[1], "|", board[2], "|", board[3])
    print(board[4], "|", board[5], "|", board[6])
    print(board[7], "|", board[8], "|", board[9])


# Module user_input(String[] board, Integer[] used):

def user_input(board, used):
    play = input_num("Choose a move: ", used)
    move = False
    count = 1
    while not move:
        if play == count:
            board[count] = "X"
            used[count] = count
            move = True
        count += 1


# Module comp_turn(String[] board, Integer[] used):

def comp_turn(board, used):
    play = input_comp(board, used)
    move = False
    count = 1
    delay = 0
    print("Computer's turn ...")
    while delay < 10000000:
        delay += 1

    while not move:
        if play == count:
            board[count] = "O"
            used[count] = count
            move = True
        count += 1


# Function Boolean game_over(String[] board, Integer[] left):

def game_over(board, left):
    over = False

    if board[1] == board[2] == board[3]:
        if board[1] == "X":
            print("You Win!")
            over = True
        elif board[1] == "O":
            print("You Lose!")
            over = True
    elif board[4] == board[5] == board[6]:
        if board[4] == "X":
            print("You Win!")
            over = True
        elif board[4] == "O":
            print("You Lose!")
            over = True
    elif board[7] == board[8] == board[9]:
        if board[7] == "X":
            print("You Win!")
            over = True
        elif board[7] == "O":
            print("You Lose!")
            over = True
    elif board[1] == board[4] == board[7]:
        if board[1] == "X":
            print("You Win!")
            over = True
        elif board[1] == "O":
            print("You Lose!")
            over = True
    elif board[2] == board[5] == board[8]:
        if board[2] == "X":
            print("You Win!")
            over = True
        elif board[2] == "O":
            print("You Lose!")
            over = True
    elif board[3] == board[6] == board[9]:
        if board[3] == "X":
            print("You Win!")
            over = True
        elif board[3] == "O":
            print("You Lose!")
            over = True
    elif board[1] == board[5] == board[9]:
        if board[1] == "X":
            print("You Win!")
            over = True
        elif board[1] == "O":
            print("You Lose!")
            over = True
    elif board[3] == board[5] == board[7]:
        if board[3] == "X":
            print("You Win!")
            over = True
        elif board[3] == "O":
            print("You Lose!")
            over = True
    elif left <= 0:
        print("Stalemate!")
        over = True
    return over


# Function Boolean y_or_n(String prompt):

def y_or_n(prompt):
    done = False
    return_value = False

    while not done:
        value = input(prompt)
        if value == "Y" or value == "y":
            done = True
            return_value = True
        elif value == "N" or value == "n":
            done = True
            return_value = False
        else:
            done = False
            print("Please enter Y or N!")
    return return_value


# Module main():

def main():
    over = False
    play = True

    print("Welcome to the tic-tac-toe program. You are 'X' and the computer is 'O'.")

    while play:
        board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        used = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        left = 9
        first = random.randint(0, 1)

        if first == 0:
            comp_turn(board, used)
            left -= 1
            over = game_over(board, left)
            if over:
                break

        while not over:
            draw_board(board)
            user_input(board, used)
            left -= 1
            over = game_over(board, left)
            if over:
                break
            comp_turn(board, used)
            left -= 1
            over = game_over(board, left)
            if over:
                break

        draw_board(board)
        play = y_or_n("Would you like to play again? (Y/N)")
        if play:
            over = False


# Call Function main()
main()
