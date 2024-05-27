class check:
    def __init__(self, a):
        self.a = a

    
class calculate(check):
    def __init__(self, a):
        super().__init__(a)

    def __add__(self, other):
        return self.a + other.a
    
    def __sub__(self, other):
        return self.a - other.a
    
    def __mul__(self, other):
        return self.a * other.a
    

class add(calculate):
    pass

class sub(calculate):
    pass
class mul(calculate):
    pass

obj1 = sub(5)
obj2 = mul(5)
print(obj1 - obj2)

obj3 = calculate(4)
obj4 = calculate(5)