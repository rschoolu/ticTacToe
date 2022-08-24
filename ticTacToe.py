import os, platform, threading, json
from typing import Dict, List
try:
    import playsound
except:
    print("This requires playsound 1.2.2. Install it now by entering a pip install command. (pip install playsound==1.2.2)")
    os.system(input('pip command > '))
    import playsound
def victory():
    playsound.playsound("./game/sounds/victory.mp3")
def blipSound():
    playsound.playsound("./game/sounds/blip.mp3")
board = []
sec_allowAcc = True
clearCommand = ""
if platform.system() == "Windows":
    clearCommand = "cls"
elif platform.system() == "Darwin" or platform.system() == "Linux":
    clearCommand = "clear"
def iterMath(it):
    return ((it-1)*3)
def getBoardrcd(rcd, iter):
    if rcd == "row":
        return [board[0+iterMath(iter)],board[1+iterMath(iter)],board[2+iterMath(iter)]]
    if rcd == "col":
        return [board[0+(iter-1)],board[3+(iter-1)],board[6+(iter-1)]]
    if rcd == "dia":
        if iter == 1:
            return [board[0],board[4],board[8]]
        if iter == 2:
            return [board[2], board[4], board[6]]
def createEmptyBoard():
    for x in range(9):
        board.append(" ")
def parseBoard(game):
    returnThis = f"_____________\n|_{game[0]}_|_{game[1]}_|_{game[2]}_|\n|_{game[3]}_|_{game[4]}_|_{game[5]}_|\n|_{game[6]}_|_{game[7]}_|_{game[8]}_|"
    return returnThis
def checkWin(space):
    for i in range(3):
        if getBoardrcd('row', i+1) == [space, space, space]:
            return True
        if getBoardrcd('col', i+1) == [space,space,space]:
            return True
    if getBoardrcd('dia', 1) == [space,space,space]:
        return True
    if getBoardrcd('dia', 2) == [space,space,space]:
        return True
    thingy = ""
    for e in board:
        if e != " ":
            thingy += "0"
        else:
            thingy += "1"
    if thingy == "000000000":
        return "draw"
    return False
inProgram = True
game = False
while inProgram:
    print("-- Tic Tac Toe -- ")
    print("1) Start a game")
    #print("2) Local Leaderboard")
    print("2) Help")
    print("3) Exit")
    cmd = input('Tic Tac Toe > ')
    if cmd == "1":
        curPlayer = 0
        os.system(clearCommand)
        board=[]
        createEmptyBoard()
        game = True
    elif cmd == "0":
        print(os.listdir("./game/scoreboard"))
    elif cmd == "2":
        os.system(clearCommand)
        print("How to Play")
        print("The board numbers are ordered like this:")
        print(parseBoard(["1","2","3","4","5","6","7","8","9"]))
        print("Use the input to select a box and place your mark.")
        input('\n')
        os.system(clearCommand)
        print("How to Play")
        print("When any player has a diagonal arrangment with their marks,\nThey can win the game.")
        print("Diagonal Arrangments:")
        print(parseBoard(["X"," ","O",
                        " ", "X", "O",
                        "O"," ","X"]))
        print(parseBoard(["X", " ", "O",
                        "X", "O", "X",
                        "O"," ", " "]))
        input('\n')
        os.system(clearCommand)
        print("How to Play")
        print("It can happen with horizontal also!")
        print("Horizontal Arrangments:")
        print(parseBoard(["X","X","X"," ","O","O","O"," ", "O"]))
        print(parseBoard([" ","X","X","O","O","O"," ", "X"," "]))
        print(parseBoard([" ", "O", "O", "X", " ", "X", "X", "X","X"]))
        input('\n')
        os.system(clearCommand)
        print("How to Play")
        print("Vertical arrangments are no exception!")
        print(parseBoard(["X"," ","O","X","O","O","X"," ", " "]))
        print(parseBoard(["O","X", "X"," ","X"," ","O","X","O"]))
        print(parseBoard([" ", "O", "O","X"," ","O","X","X","O"]))
        input('\n')
        os.system(clearCommand)
        print("How to Play")
        print("Now that you know how to play, and if you've played before, refreshed.\nLet's get to playing!")
        input('\n')
    elif cmd == "3":
        inProgram = False
    while game:
        y = threading.Thread(target=blipSound)
        y.start()
        print(parseBoard(board))
        safe = True
        while safe:
            print(f"Player {curPlayer+1}, Where do you put your mark?")
            markPlace = 9012
            markPlace = input(f'Player {curPlayer+1} > ')
            if markPlace.isdigit() and int(markPlace) < 10 and int(markPlace) != 0:
                markPlace = int(markPlace)
                if board[markPlace-1] == " ":
                    if curPlayer == 0:
                        board[markPlace-1] = "X"
                        if checkWin("X") == True:
                            x = threading.Thread(target=victory)
                            x.start()
                            os.system(clearCommand)
                            print(parseBoard(board))
                            print(f"Player {curPlayer+1} has won the game!")
                            input('\n')
                            game = False
                        elif checkWin("X") == "draw":
                            os.system(clearCommand)
                            print(parseBoard(board))
                            print(f"The game was a draw. Nobody won.")
                            input('\n')
                            game = False
                        curPlayer = 1
                    elif curPlayer == 1:
                        board[markPlace-1] = "O"
                        if checkWin("O") == True:
                            x = threading.Thread(target=victory)
                            x.start()
                            os.system(clearCommand)
                            print(parseBoard(board))
                            print(f"Player {curPlayer+1} has won the game!")
                            input('\n')
                            game = False
                        elif checkWin("X") == "draw":
                            os.system(clearCommand)
                            print(parseBoard(board))
                            print(f"The game was a draw. Nobody won.")
                            input('\n')
                            game = False
                        curPlayer = 0
                    safe = False
                    break
        os.system(clearCommand)
    os.system(clearCommand)