from abc import ABC, abstractmethod

class abs(ABC):
    @abstractmethod
    def work(self):
        print('abs can work')

class ch1(abs):
    def work1(self):
        print('ch1 can also work')
        abs.work(self)

ob = ch1()
ob.work()