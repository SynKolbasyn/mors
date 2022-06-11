from saveLoad import *
import actions

command = ""

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
