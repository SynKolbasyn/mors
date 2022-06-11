from character import *


class SaveLoad():
    def __init__(self, dataPath):
        self.dataPath = dataPath

    def saveA(self, data):
        file = open(self.dataPath, 'a')
        file.write(data)
        file.close()

    def saveW(self, data):
        file = open(self.dataPath, 'w')
        file.write(data)
        file.close()

    def load(self):
        a = []
        file = open(self.dataPath, 'r')
        for line in file:
            ta = []
            ta = line.split("\t")
            a.append(Character(ta[0].strip(),
                               ta[1].strip(),
                               ta[2].strip(),
                               ta[3].strip(),
                               ta[4].strip(),
                               ta[5].strip(),
                               ta[6].strip()))
        file.close()
        return a

    def getDataPath(self):
        return self.dataPath
