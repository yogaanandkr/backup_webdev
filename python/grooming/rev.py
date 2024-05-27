a = {'a': 1, 'b': 2, 'c': 3}
b = [['a', 1], ['b', 2], ['c',3]]
c = dict(b)
# print('****'.join(str(c.values())))
# for i in a.items():
#     print(i)

a = "popoye the sailor man"
# print(a.title())

a = 'mother in law'
b = 'hitler woma'
one = []
two = []
for i in a:
    if i != ' ':
        one += [i]

for i in b:
    if i != ' ':
        two += [i]
print(one)
print(two)

if len(one) == len(two):
    if one.sort() == two.sort():
        print('anagram')
# a = ''.join(a)
# a.sort()
# print(a)
        
import keyword
print(keyword.iskeyword('Truee'))

def gen():
    yield 1
    yield 2
    yield 3

x = gen()

print(next(x))
print(next(x))
print(next(x))
print(next(x))

a = 5 print(str(a))