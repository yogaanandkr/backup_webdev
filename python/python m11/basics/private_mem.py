class company:
    cname = "Valorant"
    cloc = "Icebox"
    cCEO = 'Omen'
    __cprofit = 95

    def __init__(self, name, phno, addr, email, sal):
        self.name = name
        self.phno = phno
        self.addr = addr
        self.email = email
        self.sal = sal

    def __disp_obj(self):
        print(self.name, self.phno, self.addr, self.email, self.sal)

    @classmethod
    def __disp_cls(cls):
        print(cls.cname, cls.cloc, cls.cCEO, cls.cprofit)
        cls.msg()

    @staticmethod
    def msg():
        print('welcome to amazon')


obj1 = company('Cypher', 737576683, 'Ascent', 'cyper@gmail.com', 10000000)
# company._company__disp_obj()
# print(company._company__cprofit)
company._company__cprofit += 5
# print(company._company__cprofit) 


class python:
    def __init__(self, tm = 0, ts = 0):
        self._tm = tm
        self._ts = ts

    # getter method 
    def get_tm(self):
        return self._tm
    
    # setter method
    def set_tm(self, m):
        self._tm = m

    # getter method 
    def get_ts(self):
        return self._ts
    
    # setter method
    def set_ts(self, s):
        self._ts = s

    def __str__(self) -> str:
        return str(self._tm)

stu = python()
print(stu)
stu.set_tm(474)
stu.set_ts(5)
print(stu)
print(stu.get_tm()/stu.get_ts())
