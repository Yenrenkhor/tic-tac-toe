def print_board():
    # print( '  |   |  ')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    # print('  |   |  ')


def place_move(pos, letter):
    board[pos] = letter


def isEmpty(pos):
    return board[pos] == ' '


def isFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def win(board, letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or \
           (board[4] == letter and board[5] == letter and board[6] == letter) or \
           (board[7] == letter and board[8] == letter and board[9] == letter) or \
           (board[1] == letter and board[4] == letter and board[7] == letter) or \
           (board[2] == letter and board[5] == letter and board[8] == letter) or \
           (board[3] == letter and board[6] == letter and board[9] == letter) or \
           (board[1] == letter and board[5] == letter and board[9] == letter) or \
           (board[3] == letter and board[5] == letter and board[7] == letter)


def player_move():
    player_turn = True
    while player_turn:
        player_move = input("Input a number 1 ~ 9: ")
        try:
            player_move = int(player_move)
            if player_move > 0 and player_move < 10:
                if isEmpty(player_move):
                    player_turn = False
                    place_move(player_move, player_char)
                else:
                    print("Sorry, this space is full!")
            else:
                print("Please type a number within the range!")
        except:
            print("Print type a number")


def ai_move():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in [ai_char, player_char]:
        for i in possibleMoves:
            board_copy = board[:]
            board_copy[i] = let
            if win(board_copy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(list):
    import random
    length = len(list)
    rand = random.randrange(0, length)
    return list[rand]


def main():
    print("Welcome to tic tac toe!")
    # place_move(5, 'x')
    print_board()

    while not (isFull(board)):
        if not win(board, ai_char):
            player_move()
            print_board()
        else:
            print("Sorry, you lost!")
            break

        if not win(board, player_char):
            move = ai_move()
            if move == 0:
                print("Tie Game")
            else:
                place_move(ai_move(), ai_char)
                print_board()
                print("Computer placed an \ 'o' \ in position", move)
        else:
            print("You won!")
            break

    # while not (isFull(board)):
    #     if not win(board, player_char):
    #         ai_move()
    #         print_board()
    #     else:
    #         print("You won!")
    #         break

    if isFull(board):
        print("Tie Game")


if __name__ == "__main__":
    board = [' ' for x in range(10)]
    player_char = 'x'
    ai_char = 'o'
    main()
