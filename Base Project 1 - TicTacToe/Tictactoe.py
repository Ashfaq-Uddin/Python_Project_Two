def sum(a, b, c):
    return a + b + c


def printBoard(xState, oState):
    zero = "X" if xState[0] else ("O" if oState[0] else 0)
    one = "X" if xState[1] else ("O" if oState[1] else 1)
    second = "X" if xState[2] else ("O" if oState[2] else 2)
    third = "X" if xState[3] else ("O" if oState[3] else 3)
    four = "X" if xState[4] else ("O" if oState[4] else 4)
    five = "X" if xState[5] else ("O" if oState[5] else 5)
    six = "X" if xState[6] else ("O" if oState[6] else 6)
    seven = "X" if xState[7] else ("O" if oState[7] else 7)
    eight = "X" if xState[8] else ("O" if oState[8] else 8)
    print(f" {zero} | {one} | {second} ")
    print(f"___|___|___")
    print(f" {third} | {four} | {five} ")
    print(f"___|___|___")
    print(f" {six} | {seven} | {eight} ")


def checkWin(xState, oState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 6], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X Wins!!!")
            return 1
        if sum(oState[win[0]], oState[win[1]], oState[win[2]]) == 3:
            print("O Wins!!!")
            return 0
    return -1


if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    oState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    while True:
        printBoard(xState, oState)
        if turn == 1:
            print("It is X's turn \n")
            value = int(input("Please enter a value to position your move\n"))
            xState[value] = 1
        else:
            print("It is O's turn \n")
            value = int(input("Please enter a value to position your move\n"))
            oState[value] = 1
        winc = checkWin(xState, oState)
        if winc != -1:
            print("Game Over")
            break
        turn = 1 - turn
