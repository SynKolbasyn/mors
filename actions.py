from saveLoad import *
from character import *

playerID = ""
playerLogin = ""
playerPassword = ""
ingress = 0
loginStatus = 0
passwordStatus = 0

moneyConst = "500"
damageConst = "5"
helthPointsConst = "100"


def register():
    loginStatus = 0
    passwordStatus = 0
    playerName = input("Введите своё настоящее имя: ")
    ok = 0
    while ok != 1:
        playerLogin = input("Придумайте логин: ")
        ta = []
        count = 0
        file = open(dataPath.getDataPath(), 'r')
        for line in file:
            ta = line.split("\t")
            if playerLogin == ta[1]:
                count = count + 1
        file.close()
        if count == 0:
            ok = 1
        else:
            print("Введённый логин уже занят, придумайте другой")
            print("\n" + 100 * "#" + "\n")
    playerPassword = input("Придумайте пароль: ")
    ok = 0
    while ok != 1:
        playerNickName = input("Введите игровой ник нейм: ")
        ta = []
        count = 0
        file = open(dataPath.getDataPath(), 'r')
        for line in file:
            ta = line.split("\t")
            if playerLogin == ta[3]:
                count = count + 1
        file.close()
        if count == 0:
            ok = 1
        else:
            print("Введённый ник нейм уже занят, придумайте другой")
            print("\n" + 100 * "#" + "\n")
    ok = 0
    while ok != 1:
        playerRass = input(
            "Выберите одну из следующих расс:\n\t1.Эльф\n\t2.Орк\n\t3.Человек\nВведите цифру выбранной рассы: ")
        if playerRass == "1" or playerRass.lower() == "эльф":
            players.append(
                Elf(playerName, playerLogin, playerPassword, playerNickName, helthPointsConst,
                    damageConst,
                    moneyConst))
            ok = 1
        elif playerRass == "2" or playerRass.lower() == "орк":
            players.append(
                Orc(playerName, playerLogin, playerPassword, playerNickName, helthPointsConst,
                    damageConst,
                    moneyConst))
            ok = 1
        elif playerRass == "3" or playerRass.lower() == "человек":
            players.append(
                Human(playerName, playerLogin, playerPassword, playerNickName, helthPointsConst,
                      damageConst,
                      moneyConst))
            ok = 1
        else:
            print("Расса выбрана неправильно, попробуйте ещё раз")
            print("\n" + 100 * "#" + "\n")
    dataPath.saveA(players[-1].encode())
    players[-1].getAccInfo()
    players[-1].getCharInfo()
    print("\n" + 100 * "#" + "\n")


def login():
    loginStatus = 0
    passwordStatus = 0
    ok = 0
    while ok != 1:
        playerLogin = input("Введите логин: ")
        file = open(dataPath.getDataPath(), 'r')
        ta = []
        loginStatus = 0
        for line in file:
            ta = line.split("\t")
            if playerLogin == ta[1]:
                loginStatus = 1
                break
        file.close()
        if loginStatus == 1:
            ok = 1
        else:
            print("Неверный логин, попробуйте ещё раз")
            print("\n" + 100 * "#" + "\n")
    ok = 0
    while ok != 1:
        playerPassword = input("Введите пароль: ")
        file = open(dataPath.getDataPath(), 'r')
        ta = []
        passwordStatus = 0
        for line in file:
            ta = line.split("\t")
            if playerPassword == ta[2]:
                passwordStatus = 1
                break
        file.close()
        if passwordStatus == 1:
            ok = 1
            print("Вы успешно вошли в аккаунт")
        else:
            print("Неверный пароль, попробуйте ещё раз")
            print("\n" + 100 * "#" + "\n")
    print("\n" + 100 * "#" + "\n")


def unknown():
    print("Неизвестное действие")
    print("\n" + 100 * "#" + "\n")
