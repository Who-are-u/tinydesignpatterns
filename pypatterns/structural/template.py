from abc import ABCMeta, abstractmethod
from re import X



class Window(metaclass=ABCMeta):
    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def start(self):
        pass

    def run(self):
        self.start()
        while True:
            try:
                self.repaint()
            except KeyboardInterrupt:
                break
        self.stop()


class MyWindow(Window):
    def __init__(self, title):
        self.__title__ = title

    def repaint(self):
        print("repaint")

    def stop(self):
        print("stop")

    def start(self):
        print("start")


wnd = MyWindow("hello....")
wnd.run()



    


