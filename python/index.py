# a = 'break'
# b  = type(a)
# c = 5
# print(type(c))
# d = b(c)
# print(type(d))


# # listing all the keywrds
# import keyword
# print(keyword.kwlist)
# print(keyword.softkwlist)

# # displaying the location of the values stored in a variable
# a = 10
# b = 10
# print(id(a), id(b))

# c = 10.1
# print(id(c))


# d = 5+7j
# print(d)
# print(type(d))
# # e = 4+5i
# # print(e)

# print(len(keyword.kwlist))

a = '''py
thon's'''
# print(a)
b = '"Python"'
# print(b)
c = "python's"
# print(c)

string = "Python"
# print('string[2] ', string[2])
# print('string[-2] ',string[-2])
# print('string[len(string)-1] ', string[len(string)-1])

list1 = [1,2,3,[5,6,9]]
# print('list1[2] ', list1[2])
# print('list1[3][1] ', list1[3][1])

ani = ['Lion', 'tiger', 'dog', 'cat']
ani[3] = 'elephant'
print(ani)

food = ['Briyani', 'Pizza', 'fried chicken', 'Fried rice',['idly', 'dosa', 'poori']]
# food[3] = 'Paneer'
# food[4][2]='sambar'
# food.insert(4, 'Parotta')
# food.append('Chutney')
# food.remove('Pizza')
print(food)

food[4].append('chutney')
print(food)
