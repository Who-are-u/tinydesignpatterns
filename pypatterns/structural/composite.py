from abc import ABCMeta, abstractmethod
from re import X



class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "Point(%s, %s)" % (self.x, self.y)
    
    def draw(self):
        print(str(self))


class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "Point(%s, %s)" % (self.p1, self.p2)
    
    def draw(self):
        print(str(self))


class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self,graphic):
        self.children.append(graphic)
    
    def draw(self):
        print("------组合图形------")
        for g in self.children:
            g.draw()
        print("------组合图形------")


p1 = Point(1,2)
p2 = Point(1,2)
l1 = Line(Point(1,2),Point(2,3))

pic1 = Picture([p1, p2, l1])
pic1.draw()

pic2 = Picture([p1, p2, l1, pic1])
pic2.draw()
