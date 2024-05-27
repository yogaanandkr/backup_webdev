def sam():
    print('hello')
    yield 1
    print('hai')
    yield 2
    print('bye')
    yield 3

# print(list(sam()))


a = [1,2,3,4.5, 7.7, 8,8.0]
def yieldd(a):
    for i in a:
        if type(i) == float:
            yield i
# print(list(yieldd(a)))
            

def coun(li):
    count = 0
    while li != 0:
        count += 1
        li = li //10
    return count

def rev(li):
    ans = 0
    while li != 0:
        ld = li % 10
        ans = ans *10 + ld
        li = li //10
    return ans



a = [10, 212, 'hiee', 3+5j, 9999]
def palin(a):
    for i in a:
        out  = []
        if type(i) == int:
            if i == rev(i):
                out += [i, coun(i)]
                yield out

print(list(palin(a)))
                
# =================================================================
# store the factorial of the range of number given and store them in the tuple
def fact(num):
    if num == 0 or num == 1:
        return 1
    return num * fact(num-1)

def facto(a,b):
    for i in range(a, b+1):
        yield fact(i)

# print(tuple(facto(1, 10)))

# ==================================================================
# multiples of number 1 to 10
def mul(a):
    for i in range(1, 11):
        yield a * i

print(list(mul(2)))