class A:
    a = 100
    b = 200

class B:
    def __init__(self, b):
        self.b = b
        print(self.b)
class C:
    c = 'hello'
    def __init__(self,a):
        self.a = a
        print(self.a)

class D(A,B,C):
    e = 50
    f = 60

print(D.a, D.b, D.c, D.e, D.f)
# ob = D('hellsdfjfdo', 'tow')

class upper:
    def __init__(self, upper):
        self.upper = upper

    def check_upper(self):
        upper_ch = True
        for i in self.upper:
            if('A'<= i <= 'Z'):
               upper_ch = True
            else:
                upper_ch = False
        return upper_ch
        
class lower:
    def __init__(self, lower):
        self.lower = lower

    def check_lower(self,):
        lower_ch = False
        for i in self.lower:
            if('a'<= i <= 'z'):
                lower_ch = True
            else:
                lower_ch = False
        return lower_ch
        
class number:
    def __init__(self, number):
        self.number = number

    def check_number(self):
        if(type(self.number)==int):
            return True
        else:
            return False
        

class spl(upper, lower, number):
    def __init__(self,upper, lower, number, splch):
        super().__init__(upper,lower,number)
        self.splch = splch

    def check_spl(self):
            num_ch = False
            for i in splch:
                if (i in '!@#$%$^&*()?><'):
                    num_ch = True
                else:
                    num_ch = False
            return num_ch
        
ob = spl('ANAND', 'lower', 3443, '@#')
print(ob.check_lower())