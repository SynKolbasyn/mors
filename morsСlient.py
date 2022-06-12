from saveLoad import *
import actions

command = ""

ingress = 0
playerID = ""

dataPath = SaveLoad("data/gameData.txt")
players = dataPath.load()

while command != "exit":
    command = input("Ваши действия: ")
    print(">>>\n")

    if command.lower() == "register":
        actions.register()
        ingress = 0

    elif command.lower() == "login":
        playerID = actions.login(0)
        ingress = 1

    elif command.lower() == "info":
        actions.info(playerID)

    elif command.lower() == "logout":
        ingress = actions.logout(ingress)

    elif command.lower() == "exit":
        actions.exit()

    else:
        actions.unknown()
