# def sum(a,b):
#     print(a+b)
# out = sum

# def sum(a,b,c):
#     print(a+b+c)

# sum(1,1,1)
# out(5,5)

def gen(a):
    i=0
    while i<a:
        yield i
        i+=1
        
# print(dict(gen(10)))

class operator:
    def __init__(self, a):
        self.a = a

    def __add__(self, any):
        return self.a - any.a

    def __sub__(self, any):
        return self.a - any.a
    
    def __mul__(self, any):
        return self.a * any.a
    
    def __truediv__(self, any):
        return self.a / any.a
    
    def __mod__(self, any):
        return self.a % any.a
    
    def __floordiv__(self, any):
        return self.a // any.a
    
    def __pow__(self, any):
        return self.a ** any.a
    
obj1 = operator(5)
obj2 = operator(4)
inp = input('choose a operation to perform')
# while inp != 'exit':
#     # print(f'{obj1} {inp} {obj2}')
#     exec(obj1 , eval(inp) , obj2)
#     inp = input('choose a operation to perform')

# print(obj1*obj2)
# print(obj1-obj2)
# print(obj1%obj2)
# print(obj1/obj2)
# print(obj1//obj2, 'floor')

