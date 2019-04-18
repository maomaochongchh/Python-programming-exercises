# -*-coding:utf-8-*-

class InputOutString():

    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = raw_input()
        return(self.s)

    def printString(self):
        print(self.s.upper())


a = InputOutString()
a.getString()
a.printString()

