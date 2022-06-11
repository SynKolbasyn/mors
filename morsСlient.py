from saveLoad import *
import actions

command = ""

playerID = ""
playerLogin = ""
playerPassword = ""
ingress = 0
loginStatus = 0
passwordStatus = 0

moneyConst = "500"
damageConst = "5"
helthPointsConst = "100"

dataPath = SaveLoad("data/gameData.txt")

players = dataPath.load()

while command != "exit":
    command = input("Ваши действия: ")
    print(">>>\n")

    if command == "register":
        actions.register()

    elif command == "login":
        actions.login()

    else:
        actions.unknown()
