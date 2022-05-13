def printBoard(x, z):
    zero = "X" if x[0] else ("O" if z[0] else 0)
    one = "X" if x[1] else ("O" if z[1] else 1)
    two = "X" if x[2] else ("O" if z[2] else 2)
    three = "X" if x[3] else ("O" if z[3] else 3)
    four = "X" if x[4] else ("O" if z[4] else 4)
    five = "X" if x[5] else ("O" if z[5] else 5)
    six = "X" if x[6] else ("O" if z[6] else 6)
    seven = "X" if x[7] else ("O" if z[7] else 7)
    eight = "X" if x[8] else ("O" if z[8] else 8)
    print()
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")
    print()


def checkWin(x, z):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in wins:
        if sum((x[i[0]], x[i[1]], x[i[2]])) == 3:
            print("X has won.")
            return 1
        if sum((z[i[0]], z[i[1]], z[i[2]])) == 3:
            print("O has won.")
            return 0
    return -1


def TicTacToe():
    print("Welcome to Tic Tac Toe")
    turn = 1
    xState = [0 for i in range(9)]
    zState = [0 for i in range(9)]
    printBoard(xState, zState)
    i = 0
    while i < 9:
        if turn == 1:
            print("X's Turn")
            x1 = int(input("Enter X's Value: "))
            while zState[x1] == 1 or xState[x1] == 1:
                print("Please enter another value.")
                x1 = int(input("Enter X's Value: "))
            xState[x1] = 1
            printBoard(xState, zState)
        if turn == 0:
            print("O's Turn")
            o1 = int(input("Enter O's Value: "))
            while xState[o1] == 1 or zState[o1] == 1:
                print("Please enter another value.")
                o1 = int(input("Enter O's Value: "))
            zState[o1] = 1
            printBoard(xState, zState)
        c = checkWin(xState, zState)
        if c != -1:
            print("Game over.")
            break
        turn = 1 - turn
        i += 1
    if i > 8:
        print("Tie.")
        print("Game over.")
    return 0


if __name__ == "__main__":
    TicTacToe()
    n = input("Do you want to start over? (y/n) ")
    while n == "y":
        TicTacToe()
        n = input("Do you want to start over? (y/n) ")
    print("Thanks for playing.")
