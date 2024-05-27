# even = lambda a: a%2 ==0
# print(even(5))
add = lambda x,y: x + y
# print(add(5,5)) 

# =================================================================

def sq(a):
    return a**2
# print(sq)

square = lambda x: x**2
# print(square(2))

 
check = lambda x,y: 'python is easy' if len(x)>len(y) else "python is hard"
# print(check("hello world", "hello"))

even = lambda x: x**3 if x%2==0 else x**2
# print(even(4))

str_check = lambda x,y : True if x==y and (type(x)==str and type(y)==str) else False
print(str_check(100 , 100))