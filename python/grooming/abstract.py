from abc import ABC, abstractmethod
class abs(ABC):
    @abstractmethod
    def hidden(self):
        print('hello')

    @staticmethod
    def static():
        print("i'm static")

class sol(abs):
    def hidden(self):
        print('this is not abs')
        super().hidden()
    def draw(self):
        print('this is draw')
        self.static()


ob = sol()
ob.draw()
# ob.hidden()