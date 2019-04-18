# -*-coding:utf-8-*-

class shape:
    def __init__(self):
        pass

    def area(self):
        self.area = 0
        return self.area

class square(shape):
    def __init__(self, l):
        shape.__init__(self)
        self.l = l

    def area(self):
        return self.l*self.l

