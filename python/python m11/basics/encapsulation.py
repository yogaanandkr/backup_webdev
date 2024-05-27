class enc:
    __login = 123456
    def __init__(self, name, age, pasw):
        self.name = name
        self.age = age
        self.__pasw = pasw

    def disp(self):
        print(self.name, self.age, self.__pasw,self.__login)

class new(enc):
    def __init__(self):
        print(self.__login)


obj = enc('anand', 22, '12345')
obj2 = new()
    