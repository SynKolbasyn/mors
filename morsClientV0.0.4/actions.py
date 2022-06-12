from saveLoad import *
from character import *

playerName = ""
playerID = ""
playerLogin = ""
playerPassword = ""
playerNickName = ""
ingress = 0
loginStatus = 0
passwordStatus = 0

moneyConst = "500"
damageConst = "5"
helthPointsConst = "100"

dataPath = SaveLoad("data/gameData.txt")

players = []


def langTest(word):
    check  = 0
    for i in range(len(word)):
        if word[i].lower() == '\u0430' or \
           word[i].lower() == '\u0431' or \
           word[i].lower() == '\u0432' or \
           word[i].lower() == '\u0433' or \
           word[i].lower() == '\u0434' or \
           word[i].lower() == '\u0435' or \
           word[i].lower() == '\u0451' or \
           word[i].lower() == '\u0436' or \
           word[i].lower() == '\u0437' or \
           word[i].lower() == '\u0438' or \
           word[i].lower() == '\u0439' or \
           word[i].lower() == '\u043a' or \
           word[i].lower() == '\u043b' or \
           word[i].lower() == '\u043c' or \
           word[i].lower() == '\u043d' or \
           word[i].lower() == '\u043e' or \
           word[i].lower() == '\u043f' or \
           word[i].lower() == '\u0440' or \
           word[i].lower() == '\u0441' or \
           word[i].lower() == '\u0442' or \
           word[i].lower() == '\u0443' or \
           word[i].lower() == '\u0444' or \
           word[i].lower() == '\u0445' or \
           word[i].lower() == '\u0446' or \
           word[i].lower() == '\u0447' or \
           word[i].lower() == '\u0448' or \
           word[i].lower() == '\u0449' or \
           word[i].lower() == '\u044a' or \
           word[i].lower() == '\u044b' or \
           word[i].lower() == '\u044c' or \
           word[i].lower() == '\u044d' or \
           word[i].lower() == '\u044e' or \
           word[i].lower() == '\u044f' or \
           word[i] == " ":
            check = check + 1
    if check == 0 and word != "":
        return 1
    else:
        return 0


def register():
    loginStatus = 0
    passwordStatus = 0
    ingress = 0
    ok = 0
    while ok != 1:
        playerName = input("Введите своё настоящее имя: ")
        ok = langTest(playerName)
        if ok != 1:
            print("Ошибка, введите имя на Английском языке и без пробелов")
            print("\n" + 100 * "#" + "\n")
    ok = 0
    while ok != 1:
        T = 0
        while T != 1:
            playerLogin = input("Придумайте логин: ")
            T = langTest(playerLogin)
            if T != 1:
                print("Ошибка, введите логин на Английском языке и без пробелов")
                print("\n" + 100 * "#" + "\n")
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
    ok = 0
    while ok != 1:
        playerPassword = input("Придумайте пароль: ")
        ok = langTest(playerPassword)
        if ok != 1:
            print("Ошибка, введите пароль на Английском языке и без пробелов")
            print("\n" + 100 * "#" + "\n")
    ok = 0
    while ok != 1:
        T = 0
        while T != 1:
            playerNickName = input("Введите игровой ник нейм: ")
            T = langTest(playerNickName)
            if T != 1:
                print("Ошибка, введите ник на Английском языке и без пробелов")
                print("\n" + 100 * "#" + "\n")
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
        if playerRass == "1" or playerRass.lower() == "эльф" or playerRass.lower() == "elf":
            players.append(
                Elf(playerName, playerLogin, playerPassword, playerNickName, helthPointsConst,
                    damageConst,
                    moneyConst))
            ok = 1
        elif playerRass == "2" or playerRass.lower() == "орк" or playerRass.lower() == "orc":
            players.append(
                Orc(playerName, playerLogin, playerPassword, playerNickName, helthPointsConst,
                    damageConst,
                    moneyConst))
            ok = 1
        elif playerRass == "3" or playerRass.lower() == "человек" or playerRass.lower() == "human":
            players.append(
                Human(playerName, playerLogin, playerPassword, playerNickName, helthPointsConst,
                      damageConst,
                      moneyConst))
            ok = 1
        else:
            print("Расса выбрана неправильно, попробуйте ещё раз")
            print("\n" + 100 * "#" + "\n")
    print("\n" + 100 * "#" + "\n")
    dataPath.saveA(players[-1].encode())
    print("\nВы успешно создали аккаунт и персонажа:\n")
    players[-1].getAccInfo()
    players[-1].getCharInfo()
    print("\n" + 100 * "#" + "\n")


def login(ingress):
    loginStatus = 0
    passwordStatus = 0
    ingress = 0
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
        passwordStatus = 0
        if playerPassword == ta[2]:
            passwordStatus = 1
            ok = 1
            print("Вы успешно вошли в аккаунт")
        else:
            print("Неверный пароль, попробуйте ещё раз")
            print("\n" + 100 * "#" + "\n")
    print("\n" + 100 * "#" + "\n")
    if ta[7].lower().strip() == "elf":
        return Elf(ta[0].strip(),
                   ta[1].strip(),
                   ta[2].strip(),
                   ta[3].strip(),
                   ta[4].strip(),
                   ta[5].strip(),
                   ta[6].strip())

    elif ta[7].lower().strip() == "orc":
        return Orc(ta[0].strip(),
                   ta[1].strip(),
                   ta[2].strip(),
                   ta[3].strip(),
                   ta[4].strip(),
                   ta[5].strip(),
                   ta[6].strip())
    else:
        return Human(ta[0].strip(),
                     ta[1].strip(),
                     ta[2].strip(),
                     ta[3].strip(),
                     ta[4].strip(),
                     ta[5].strip(),
                     ta[6].strip())


def info(playerID):
    try:
        playerID.getAccInfo()
        playerID.getCharInfo()
    except AttributeError:
        print("Вы не вошли в аккаунт")
    print("\n" + 100 * "#" + "\n")


def logout(ingress):
    if ingress == 1:
        loginStatus = 0
        passwordStatus = 0
        ingress = 0
        print("Вы успешно вышли из аккаунта")
    else:
        print("Вы не можете выйти из аккаунта не войдя в него,\nдля начала следует в него войти")
    print("\n" + 100 * "#" + "\n")
    return ingress


def unknown():
    print("Неизвестное действие\nДоступны следующие действия:"
          "\n\tregister - чтобы зарегестрировать новый аккаунт и персонажа"
          "\n\tlogin    - чтобы войти в уже созданный аккаунт"
          "\n\tlogout   - чтобы выйти из аккаунта"
          "\n\tinfo     - чтобы узнать информацию об аккаунте и персонаже"
          "\n\texit     - чтобы завершить программу")
    print("\n" + 100 * "#" + "\n")


def exit():
    print("Программа завершена")
    print("\n" + 100 * "#")
