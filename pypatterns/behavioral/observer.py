from abc import ABCMeta, abstractmethod
from re import X



class Oberver(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):
        pass

class Notice():
    def __init__(self, company_info):
        self.__observer = []
        self.__company_info__ = company_info

    def attach(self, oberver):
        self.__observer.append(oberver)

    def detach(self, oberver):
        self.__observer.remove(oberver)

    def notify(self):
        for obs in self.__observer:
           obs.update(self)

    @property
    def company_info(self):
        return self.__company_info__
    
    @company_info.setter
    def company_info(self, company_info):
        self.__company_info__ = company_info   
        self.notify()

class Stuff(Oberver):
    def __init__(self):
        self.__company_info__ = None

    def update(self, notice):
        self.__company_info__ = notice.company_info

    @property
    def company_info(self):
        return self.__company_info__



n = Notice("明天放假")
stuff1 = Stuff()
stuff2 = Stuff()
n.attach(stuff1)
n.attach(stuff2)
n.company_info = "明天是冬至，全体放假半天"
print(stuff1.company_info)
print(stuff2.company_info)

    


