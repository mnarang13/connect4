print("Let's play Connect Four! Try to get four pieces in a row.")
player1Name = input("Enter the name of Player One: ")
player2Name = input("Enter the name of Player Two: ")

counter = 1

x = [[" 0", 1, 2, 3, 4, 5, 6, '\n'], [".", ".", ".", ".", ".", ".", ".",'\n'], [".", ".", ".", ".", ".", ".", ".",'\n'], [".", ".", ".", ".", ".", ".", ".",'\n'], [".", ".", ".", ".", ".", ".", ".",'\n'], [".", ".", ".", ".", ".", ".", ".",'\n'], [".", ".", ".", ".", ".", ".", ".",'\n']]

def gameBoard(x):
    for m in range(7):
        for n in range(8):
            print(x[m][n], end=" ")

gameBoard(x)

def findSpot(col, x):
    for i in(6, 5, 4, 3, 2, 1):
        if x[i][col] == ".":
            return i
            break

def checkFourH(x, m, n, symb):
    if x[m][n] == symb:
        if x[m][n+1] == symb:
            if x[m][n+2] == symb:
                if x[m][n+3] == symb:
                    return True
        return False

def checkHorizontal(x):
    for m in(1, 2, 3, 4, 5, 6):
        for n in(0, 1, 2, 3):
            if checkFourH(x, m, n, "x") == True:
                return True
            elif checkFourH(x, m, n, "o") == True:
                return True
    return False

def checkFourV(x, m, n, symb):
    if x[m][n] == symb:
        if x[m+1][n] == symb:
            if x[m+2][n] == symb:
                if x[m+3][n] == symb:
                    return True
        return False

def checkVertical(x):
    for m in(1, 2, 3):
        for n in (0, 1, 2, 3, 4, 5, 6):
            if checkFourV(x, m, n, "x") == True:
                return True
            elif checkFourV(x, m, n, "o") == True:
                return True
    return False

def checkFourD1(x, m, n, symb):
    if x[m][n] == symb:
        if x[m-1][n+1] == symb:
            if x[m-2][n+2] == symb:
                if x[m-3][n+3] == symb:
                    return True
        return False

def checkDiagonal1(x):
    for m in(4, 5, 6):
        for n in (0, 1, 2, 3):
            if checkFourD1(x, m, n, "x") == True:
                return True
            elif checkFourD1(x, m, n, "o") == True:
                return True
    return False

def checkFourD2(x, m, n, symb):
    if x[m][n] == symb:
        if x[m+1][n+1] == symb:
            if x[m+2][n+2] == symb:
                if x[m+3][n+3] == symb:
                    return True
        return False

def checkDiagonal2(x):
    for m in(1, 2, 3):
        for n in (0, 1, 2, 3):
            if checkFourD2(x, m, n, "x") == True:
                return True
            elif checkFourD2(x, m, n, "o") == True:
                return True
    return False               

while True:
    if counter == 1:
        #player1goes
        col = int(input("Hello " + player1Name + "! What column do you want to choose?"))
        x[findSpot(col, x)][col] = "x"
        gameBoard(x)
        counter = 2
    elif counter == 2:
        #player2goes
        col = int(input("Hello " + player2Name + "! What column do you want to choose?"))
        x[findSpot(col, x)][col] = "o"
        gameBoard(x)
        counter = 1
    if checkHorizontal(x) == True:
        if counter == 1:
            print("Congrats! " + player2Name + " won! Game over.")
        else:
            print("Congrats! " + player1Name + " won! Game over.")
        break
    if checkVertical(x) == True:
        if counter == 1:
            print("Congrats! " + player2Name + " won! Game over.")
        else:
            print("Congrats! " + player1Name + " won! Game over.")
        break
    if checkDiagonal1(x) == True:
        if counter == 1:
            print("Congrats! " + player2Name + " won! Game over.")
        else:
            print("Congrats! " + player1Name + " won! Game over.")
        break
    if checkDiagonal2(x) == True:
        if counter == 1:
            print("Congrats! " + player2Name + " won! Game over.")
        else:
            print("Congrats! " + player1Name + " won! Game over.")
        break
