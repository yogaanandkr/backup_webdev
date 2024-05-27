# for i in range(1, 11):
#     print(i)
    

# for i in 'python':
#     print(i)

# for i in [1, 2, 3, 4, 'python']:
#     print(i)

# for i in {'a': 1, 'b': 2, 'c': 3}:
#     print(i)

# a = 'python is easy to solve'.split()
# out = {}
# for i in range(len(a)):
#     if i % 2 == 0:
#         out[a[i]] = int(len(a[i])/2)
#     else:
#         out[a[i]] = a[i][::-1]
# print(out)

# =================================================================
# a = 'nitin loves ava so much than aba'.split()
# out = ''

# for i in range(len(a)):
#     if a[i] == a[i][::-1]:
#         out += a[i] + ' '
# print(out)

# for i in a:
#     if i == i[::-1]:
#         out += i + ' '
# print(out)


# username = 'omen07'

# while True:
#     id = input('enter the username: ')
#     if username == id:
#         print('welcome')
#         break
#     else:
#         print('enter valid username ')

# =================================================================

# create a casino

# crt_no = 7
# won = 0
# while True:
#     guess = int(input('enter your guess:'))
#     if guess == crt_no:
#         won += 100
#         print('you won 100 rs and your balance is ', won)
#     elif guess > crt_no:
#         print('your guess was beyond the crt number, have another chance')
#     else:
#         won -= 100
#         print('you lost 100 rs, better luck next time and you won ', won)
#         break
# print(won)

# =================================================================
# prime or not
# while True:
#     check = int(input('enter a number: '))
#     if check == 2:
#         print('prime')
#         break
#     for i in range(2, check):
        
#         if check % i == 0:
#             print('not prime')
#             break
#         else:
#             print('prime')
#             break

# check = int(input())
# for i in range (2, check):
#     if check % i == 0:
#         print('not prime')
        
# else:
#     print('prime')

# =================================================================
# str has lower case or not
# str = input('Enter a string: ')
# for i in range(len(str)):
#     if 'a'<= str[i] <= 'z':
#         print('has lower case')
#         break
# else:
#     print('has no lower case')


# =================================================================
# check a collection is hetero or homogeneous
# a = [1,2,3,4,5,6]
# dtype = type(a[0])
# for i in a:
#     if type(i) != dtype:
#         print('heterogenous')
#         break
# else:
#         print('homogenous')
    

# =================================================================
# check a collection is homogeneous (int ) or not
# a = [1,2,3,4,5]
# a = [1,2,3,'a',4,5]
# for i in a:
#     if type(i) != int:
#         print('not int')
#         break
# else:
#     print('they are all integger')

# ================================================================
# extract all the even numbers from 1 to 100
# for i in range(1,101):
#     if i % 2 != 0:
#         continue
#     print(i, end = ' ')

# ================================================================
# extract all the integers from the list
# a = ['hello', 2, 'world', 33, 45, 'anand']
# ans = []
# for i in a:
#     if type(i) != int:
#         continue
#     ans.append(i)
# print(ans)

# ================================================================
# extract all the integers from the list and store square of it
# a = ['hello', 2, 'world', 33, 45, 'anand']
# ans = []
# for i in a:
#     if type(i) != int:
#         continue
#     ans.append(i**2)
# print(ans)

# ================================================================
# a = [10, 20, 30]
# b = 'python'
# for i in a:
#     for j in b:
#         print(i, str(i)+j, end = ' ')


# ================================================================
# a = 'HiE How are you'.split()
# ans = []

# for i in a:
#     count = 0
#     if 'a' in i or 'A' in i:
#         count += 1
#     if 'e' in i or 'E' in i:
#         count += 1
#     if 'i' in i or 'I' in i:
#         count += 1
#     if 'o' in i or 'O' in i:
#         count += 1
#     if 'u' in i or 'U' in i:
#         count += 1
    
#     ans += [count]
# print(ans)

# for i in a:
#     count = 0
#     for j in i:
#         if j in 'aeiouAEIOU':
#             count += 1
#     ans += [count]
    
# print(ans)

# =================================================================
# print factorial of number range 1 to 10
# ans = []
# for i in range(1, 11):
#     fact = 1
#     for j in range(1,i+1):
#         fact *= j
#     ans += [fact]
# print(ans)

# =================================================================
# perfect number using nested for
# out = []
# for i in range(1,101):
#     count = 0
#     for j in range(1, i):
#         if i % j == 0:
#             count += j
#     if count == i:
#         out += [count]
# print(out)

# =================================================================
# a = [10, 'hiee', 'apple', 321] out = [1, 6]

# a = [10, 'hiee', 'apple', 321]
# out = []
# for i in a:
#     sum = 0
#     if type(i) == int:
#         for j in str(i):
#             sum += int(j)
#         out += [sum]
# print(out)

# method 2 (without nested for loop)
# a = [10, 'hiee', 'apple', 321]
# out = []
# for i in a:
#     sum = 0
#     if type(i) == int:
#         while i > 0:
#                 ld = i % 10
#                 sum += ld
#                 i = i // 10
#         out += [sum]
# print(out)

# =============================================================================
a = input()
b = ''
for i in a:
    if i in 'aeiouAEIOU' and i not in b:
        b += i
print(b)