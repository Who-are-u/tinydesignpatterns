from abc import ABCMeta, abstractmethod
from re import X



class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handler_leave(self, day):
        pass

class GeneralManager(Handler):
    def __init__(self):
        self.next = None

    def handler_leave(self, day):
        if day < 7:
            print("GeneralManager 批准 %s" % day)
        else:
            print("滚蛋")


class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    
    def handler_leave(self, day):
        if day < 3:
            print("DepartmentManager 批准 %s" % day)
        else:
            print("DepartmentManager 权限不足 %s" % day)
            self.next.handler_leave(day)


class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handler_leave(self, day):
        if day < 2:
            print("ProjectDirector 批准 %s" % day)
        else:
            print("ProjectDirector 权限不足 %s" % day)
            self.next.handler_leave(day)
    


day = 1
h = ProjectDirector()
h.handler_leave(day)
