list1 = [1,2,3,[4,5,6,9],8,10]
# list1.remove(0)
list1[3].insert(3, 7)
list1.insert(5,9)
# print(list1)

set1 = {5,4,3,2,1,'a'}
set1.add(100)
# print(set1)

a = {}
# print(type(a))
tup = (1,2,3,[4,5])
# print(tup[2])

# dictionary

d1 = {'firstName': 'Yoga', 'LastName': ' Anand', 'age': 22, 'marks': 100 }
# print(d1)
d1['degree'] ='B.E'
d1['age'] = 23
del d1['age']
# print(d1)


d2= {}
d2['Name'] = 'Omen'
# print(d2)


# slicing

a = 'python'
# print(a[0:5:2])
# print(a[5:1:-1])
# print(a[:1:-1])

# print(a[-5:-1])
# print(a[-1:-])


# a = (('a',1), ('b', 2))
a= [4,3,5,3,9,1,2,'a','b','c','d']
b = tuple(a)
a = set(a)
# print(a)

# a = 10.5
# print(type(a))
# print(float(a))
# print(complex(a))
# print(bool(a))
# print(str(a))
# print(list(a)) # error
# print(tuple(a)) # error
# print(set(a)) # error
# print(dict(a)) # error

comp = 4 + 6j
# print(bool(comp))

a  = True
b = float(a)
# print(b)
# print(type(b))

li = [3,4,5]


string = '34'
b = int(string)
# print(type(b))

listt = {'neme': 'Omen', 'age':22}
a = list(listt.items())
b = list(listt.values())
# print(a)
# print(b)
# print(type(a))

print(3**4)
print(4/3)
print(4%3)
print([1,2,3,4,5] + [1,2,3,4,5])
# print('a' + 1)
z = 'z'
b = 5
print(5%3)

print([1,2] * 2)