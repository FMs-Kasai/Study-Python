def print_board(board):
    print(board["3-1"] + "|" + board["2-1"] + "|" + board["1-1"])
    print("-+-+-")
    print(board["3-2"] + "|" + board["2-2"] + "|" + board["1-2"])
    print("-+-+-")
    print(board["3-3"] + "|" + board["2-3"] + "|" + board["1-3"])

the_board = {"3-1": " ", "2-1": " ", "1-1": " ",
             "3-2": " ", "2-2": " ", "1-2": " ",
             "3-3": " ", "2-3": " ", "1-3": " "}

turn = "〇"
for i in range(9):
    print_board(the_board)
    print(turn + "の手番です。どこに打ちますか？")
    move = input()
    the_board[move] = turn

    if turn == "〇":
        turn = "★"
    else:
        turn = "〇"