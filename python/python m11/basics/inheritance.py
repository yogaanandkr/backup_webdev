class A:
    a = 100
    b = 200

class B:
    c = 'hello'
    d = 7

class bank:
    bname = 'TMB'
    bloc = 'Madurai'
    bIFSC = 'TMBL0000458'
    def __init__(self, name, accno, phno):
        self.name = name
        self.accno = accno
        self.phno = phno
    
    def disp_obj(self):
        print(self.name, self.accno, self.phno, end=' ')

    def disp_cls(self):
        print(self.bname, self.bloc, self.bIFSC)

    def ch_phno(self, new):
        self.phno = new

class bank1(bank):
    def __init__(self,name, accno, phno, age, pan):
        super().__init__(name, accno, phno)
        self.age = age
        self.pan = pan

    def disp_obj1(self):
        super().disp_obj()
        print(self.age, self.pan)


# obj1 = bank1('Anand', 66565626, 7397576683, 22, 'PCSKJKJ5656' )
# obj1.disp_obj1()
# print(obj1.__dict__)
# print(obj1.__getattribute__)

# =================================================================
                                                                        # RESUME 



# def pack(**a):
#     print(a)
# pack(a = 10, b = 20)

# a, b = 'pq'
# print(a)
# print(b)

