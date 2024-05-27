# out = []
# ans = lambda x: out.append(x**2)

# for i in range(1,11):
#     ans(i)
# print(out)

sqr = lambda x: x**2
ans = map(sqr, [1,2,3,4,5,6,7,8,9,10])
# print(list(ans))
# print(list(map(lambda x: x**2,[1,2,3,4,5,6,7,8,9,10])))

a = "good morning"
fun = lambda x: (x, len(x))
ans = map(fun, a.split(" "))
print(dict(ans))


# print(dict(map(lambda a: len(a), a.split(" "))))

out = {}
fun = lambda x: out.update(x=len(x))
ans = map(fun, a.split(" "))
# print(out)

def facto(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)

fact = lambda x: 1 if x == 1 else x*fact(x-1)
ans = map(fact, range(1,11))
ans2= map(facto, range(1,11))
# print('ans',list( ans))
# print('ans2',list( ans2))

fun = lambda x: x%2==0
fil = filter(fun, range(1,101))
# print(list(fil))

import functools
fun1 = lambda x,y: x+y
red = functools.reduce(fun1, range(1,6))
print(red)