class Character():
    def __init__(self, name, login, password, nickName, helthPoints, damage, money):
        self.name = name
        self.login = login
        self.password = password
        self.nickName = nickName
        self.helthPoints = helthPoints
        self.damage = damage
        self.money = money

    def encode(self):
        data = self.name + "\t" + \
               self.login + "\t" + \
               self.password + "\t" + \
               self.nickName + "\t" + \
               self.helthPoints + "\t" + \
               self.damage + "\t" + \
               self.money + "\t" + \
               self.rassInfo() + "\n"
        return data

    # def decode(self, line):
    #     ta = []
    #     ta = line.split("\t")
    #     self.name = ta[0].strip()
    #     self.login = ta[1].strip()
    #     self.password = ta[2].strip()
    #     self.nickName = ta[3].strip()
    #     self.helthPoints = ta[4].strip()
    #     self.damage = ta[5].strip()
    #     self.money = ta[6].strip()
    #     return Character(self.name, self.login, self.password, self.nickName, self.helthPoints, self.damage, self.money)

    def getAccInfo(self):
        print("Данные аккаунта:\n\tЛогин:", self.login + "\n\tПароль:",
              self.password + "\nОбязательно запомните их, иначе вы можете потеряете доступ к своему аккаунту")

    def getCharInfo(self):
        print("\nИгровые данные:\n\tНик:", self.nickName + "\n\tРасса:",
              self.rassInfo + "\n\tЗдоровье:", self.helthPoints + "\n\tУрон:", self.damage + "\n\tБаланс кошелька:",
              self.money)

    def rassInfo(self):
        return self.rassInfo


class Elf(Character):
    def __init__(self, name, login, password, nickName, helthPoints, damage, money):
        super().__init__(name, login, password, nickName, helthPoints, damage, money)
        self.rassInfo = "Elf"



class Orc(Character):
    def __init__(self, name, login, password, nickName, helthPoints, damage, money):
        super().__init__(name, login, password, nickName, helthPoints, damage, money)
        self.rassInfo = "Orc"

class Human(Character):
    def __init__(self, name, login, password, nickName, helthPoints, damage, money):
        super().__init__(name, login, password, nickName, helthPoints, damage, money)
        self.rassInfo = "Human"

