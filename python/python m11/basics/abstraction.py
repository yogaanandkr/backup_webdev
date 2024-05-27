from abc import ABC, abstractmethod


class pluto(ABC):
    @abstractmethod
    def msg(self):
        print('msg1 pluto')

class earth(pluto):
    # @staticmethod
    def msg(self):
        print('hello')



# obj = earth()
# # obj.msg1()
# earth.msg(obj)
# obj2 = pluto()
# obj2.msg()

class rem:
    def __init__(self, str):
        self.str = str

    def __sub__(self, other):
        out = ''
        for i in (self.str):
            if i != other.str:
                out += i
        return out
        # return self.str - other.str
    
# print('hai'-'a')

ob1 = rem('hai')
ob2 = rem('a')
print(ob1 - ob2)