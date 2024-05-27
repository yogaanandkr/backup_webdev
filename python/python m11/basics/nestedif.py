
# wap to check a number is divisible by 5 but it should be even. if it's even print even or false or print not divisible by 5.

# num = int(input())
# if num % 5 ==0:
#     if num % 2 == 0:
#         print('even')
#     else:
#         print('odd')

# else:
#     print('not divisible by 5') 

# print(len(45))

# num = eval(input())

# =================================================================
# wap to check the data is multivalued or not if multivalued its length should be more than 3.

# if (type(num) in [str, list, tuple, set, dict]):
#     if len(num) > 3:
#         print('length greater than 3')

#     else:
#         print('length not greater than 3')
# else:
#     print('not multivalued')

# =================================================================

# wap to check the charecter is vowel or consonant
# a = input()
# if 'A' <= a <= 'Z' or 'a' <= a <= 'z':
    # if a in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:   #or if a in 'aeiouAEIOU'
#         print('vowel')
#     else:
#         print('consonant')
# else:
#     print('not a string')

# =================================================================

# a = 10
# b = 50
# c = 30
# if a>b:
#     if a>c:
#         print('a', a)
#     else:
#         print('c', c)
# else:
#     if b > c:
#         print('b', b)
#     else:
#         print('c', c)

a = 90
b = 50
c = 100
d = 91
e = 87


# 4 nos
if a > b:
    if a > c:
        if a > d:
            print('a', a)
        else:
            print('d', d)
    else:
        if c > d:
            print('c', c)
        else:
            print('d', d)
else:
    if b > c:
        if b > d:
            print('b', b)
        else:
            print('d', d)
    else:
        if c > d:
            print('c', c)
        else:
            print('d', d)

#  5 nos

a = 90
b = 92
c = 10
d = 91
e = 87

if a > b:
    if a > c:
        if a > d:
            if a > e:
                print('a', a)
            else:
                print('e', e)
        else:
            if d > e:
                print('d', d)
            else:
                print('e', e)
    else:
        if c > d:
            if c > e:
                print('c', c)
            else:
                print('e', e)
        else:
            if d > e:
                print('d', d)
            else:
                print('e', e)

else:
    if b > c:
        if b > d:
            if b > e:
                print('b', b)
            else:
                print('e', e)
        else:
            if d > e:
                print('d', d)
            else:
                print('e', e)
    else:
        if c > d:
            if c > e:
                print('c', c)
            else:
                print('e', e)
        else:
            if d > e:
                print('d', d)
            else:
                print('e', e)


# wap to create a login page where username should be equal to the user input if both are same print welcome to website or enter valid password
            
# crt_username = 'yoga anand'
# crt_password = 'yokesh123'

# username = input('Enter username: ')
# password = input('Enter password: ')

# if username == crt_username:
#     if password == crt_password:
#         print('welcome to instagram')
#     else:
#         print('incorrect password')
# else:
#     print('invalid username or password')


# print("im best \n" *5)

# i = 0
        
# while i != 10:
#     print(i)
#     i += 1



i = 1
while i <= 100:
    if 1%3 == 0:
        print(i**3)
    i+=1