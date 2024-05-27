# #  wap to print 'i'm best' for 5 times
# i = 0
# while i < 5:
#     # print("i'm best")
#     i += 1


# # =================================================================

# # wap to print first 10 natural numbers
# i = 1
# while i <= 10:
#     # print(i, end='  ')
#     i += 1

# # =================================================================
# # wap to print all the even nos less than 100
# i = 0
# while i < 100:
#     if i %2 == 0:
#         # print(i, end=' ')
#         i += 1

# =================================================================
# wap to find sq of num from 1 to 10
# i = 1
# while i <= 10:
#     # print(i**2)
#     i+=1

# =================================================================
# wap to find cube of no from 1 to 100 which is divisible by 3

# i = 1
# while i <= 100:
#     if i%3 == 0:
#         print(i**3)
#     i = i+1


# =================================================================
# wap to print nos which are divisible by 5 from range m to n
# m = int(input())
# n = int(input())
# while m < n:
#     if m % 5 == 0:
#         print(m)
#     m+=1
    
# =================================================================
# sum of first 10 natural numbers
# i = 1
# sum = 0
# while i<=10:
#     sum += i 
#     i = i+ 1
# print(sum)

# =================================================================
# prod of first 10 natural numbers
# i = 1
# prod = 1
# while i<=10:
#     prod *= i 
#     i = i+ 1
# print(prod)

# =================================================================
# write a program to return capital letters from a string
# string = 'PyTHon'
# i = 0
# while i < len(string):
#     if 'A'<= string[i] <= 'Z':
#         print(string[i], end = '')
#     i +=1



# =================================================================
# write a program to reverse a number
num = 123
# print(str(num)[::-1])

# strnum = str(num)
# i = len(strnum)
# ans = ''
# while i > 0:
#     ans += strnum[i-1]
#     i -= 1
# print(int(ans))

# or

# rev = 0
# while num!=0:
#     id = num % 10
#     rev = rev * 10 + id
#     num = num//10
# print(rev)

# =================================================================
# wap to return spl charecters from a string
# string = 'adsj!@jkj#nnk$4'
# i = 0
# spl = ''
# while i < len(string):
#     if string[i] in ['!','@','#','$','%','^','&','*',',','<','>']:
#         spl += string[i]
#     i += 1
# print(spl)

# =================================================================
# wap to extract all the integers from given list
# a = [1, 2, 3, 'a', 'b', 'c', 'd', 'e', 'f', 4]
# i = 0
# out =[]
# while i < len(a):
#     if type(a[i]) == int:
#         out.append(a[i])
#     i += 1
# print(out)


# =================================================================
# a = 'pythON'
# i = 0
# ans = ''
# while i < len(a):               
#     if 'a' <= a[i] <='z' and i % 2 == 0:
#         ans += a[i]
#     i += 2
# print(ans)

# =================================================================
# wap to extract all the vowel from given string
# a = 'yoga anand'
# i = 0
# b = ''
# count = 0
# while i < len(a):
#     if a[i] in 'aeiouAEIOU':
#         b += a[i]
#         count += 1
#     i += 1


# print(b)
# print(count)
# print(len(b))

# =================================================================

# a = 'DaTASciENcE'
# i = 0
# ans = ''
# while i < len(a):
#     if 'A'<= a[i] <='Z':
#         ans += a[i]
#     i += 1
# print(ans+str(len(ans)))

# =================================================================

# a = 'AeisOsU'
# out = ''
# i = 0
# while i < len(a):
#     if i%2==0 and a[i] in 'AEIOU':
#         out += a[i]
#     i += 1
# print(out)

# =================================================================

a = 'aabacbcdac'
# i = 0
# dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
# while i < len(a):
#     if a[i] == 'a':
#         dict['a'] += 1
#     elif a[i] == 'b':
#         dict['b'] += 1
#     elif a[i] == 'c':
#         dict['c'] += 1
#     elif a[i] == 'd':
#         dict['d'] += 1
#     i += 1
# print(dict)

# i = 0
# ans = {}
# while i < len(a):
#     ans[a[i]] = a.count(a[i])
#     i+= 1
# print(ans)

# i = 0
# ans = {}
# while i < len(a):
#     if a[i] in ans:
#         ans[a[i]] += 1
#     else:
#         ans[a[i]] = 1
#     i += 1
# print(ans)


# =================================================================
# a = 'Python is very easy'
# ans = {}
# i = 0
# f = ''
# while i < len(a):
#     if a[i] != ' ':
#         f+=a[i]
#     i+=1
#     ans[f] = f[::-1]
#     f = ''
#     i += 1
# print(ans)

# a = 'Python is very easy'
# ans = {}
# i = 0
# a = a.split()
# print(a)
# while i < len(a):
#     ans[a[i]] = a[i][::-1]
#     i += 1
# print(ans)


# table = int(input())
# i = 1
# while i <=10:
#     print(table, '*', i, '=' ,table*i)
#     i += 1


# =================================================================
# input = 721 op = 10

# n = 721
# sn = str(n)
# i = 0
# ans = 0
# while i < len(sn):
#     ans += int(sn[i])
#     i += 1
# print(ans)
 
# mn = 721
# ans = 0
# while mn > 0:
#     num = mn % 10
#     ans = ans + num
#     mn //= 10
# print(ans)

# =================================================================

# listt = ['hello', 'asef',5,['apple',5,'mango'],'lksdjkj','ab', '56565']
# i = 0
# ans = []
# while i < len(listt):
#     if not len(listt[i]):
#         if type(listt[i]) == str and len(listt[i]) > 3:
#             ans.append(listt[i])
#     if type(listt[i])==len(listt[i]):
#         while i < len(listt[i]):
#             if type(listt[i]) == str and len(listt[i]) > 3:
#                 ans.append(listt[i])
#             i += 1

#     i += 1
# print(ans)


# =================================================================
# string = 'YokeshAnand762001@gmail.com'
# i = 0
# upper = ''
# lower = ''
# spl = ''
# number = ''

# while i < len(string):
#     if 'A'<= string[i] <='Z':
#         upper += string[i]
#     elif 'a'<= string[i] <='z':
#         lower += string[i]
#     elif string[i] in '!@#$%^&*()<>.':
#         spl += string[i]
#     elif string[i] in '0123456789':
#         number += string[i]
#     else:
#         print('enter a valid string')
        
#     i += 1

# print(upper  , lower, spl  , number)

# print(ord('A'))
# print(ord('a'))

# =================================================================

# txt = 'hai hello'
# i = 0
# ans = ''
# while i < len(txt):
#     if 'a'<= txt[i] <= 'z':
#         ans += chr(ord(txt[i])-32)
#     elif txt[i] == ' ':
#         ans += txt[i]
#     else:
#         ans += txt[i]
#     i += 1
# print(ans)


# ===================================================================
# txt = 'Hai Hello'
# i = 0
# ans = ''
# while i < len(txt):
#     if 'A'<= txt[i] <= 'Z':
#         ans += chr(ord(txt[i])+32)
#     else:
#         ans += txt[i]
#     i += 1
# print(ans)


# ===================================================================
# in = 'How are you pythons' op = 'How_are_you_pythons'
# a = 'How are you pythons'
# i = 0
# ans = ''
# while i < len(a):
#     if a[i] == ' ':
#         ans += '_'
#     else:
#         ans += a[i]
#     i += 1
# print(ans)


# ===================================================================


# a ='abcaaaddaccbb'
# ans = ''
# i = 0
# while i < len(a):
#     if a[i] not in ans:
#         ans += a[i] + str(a.count(a[i]))
#     i += 1
# print(ans)

# ===================================================================
# a = 'malayalam'
# palindrome = ''
# i = len(a)-1
# while i >=0:
#     palindrome += a[i]
#     i-=1
# if a == palindrome:
#     print('palindrome')
# else:
#     print('not palindrome')

# ===================================================================
# a = ['Hai', 3+5j, 'hello', [1,2,3], 'python']
# i = 0
# ans = {}
# while i < len(a):
#     if type(a[i]) == str:
#         ans[a[i]] = len(a[i])
#     i +=1
# print(ans)

# ===================================================================
# check the value is palindrome or not and return a list with palindrome values
# a = [121, 684, 777, 919]
# i = 0
# ans = []
# while i < len(a):
#     if len(str(a[i]))>1 and str(a[i]) == str(a[i])[::-1]:
#         ans.append(a[i])
#     i += 1
# print(ans)


# ==================================================================
# without converting to string
# ans = []
# temp = 0
# i = 0
# while i < len(a):
#     if a[i]>9:
#         check = a[i]
#         while a[i] != 0:
#             ld = a[i] % 10
#             temp = temp * 10 + ld
#             a[i] = a[i]//10
#         if check == temp:
#             ans.append(temp)
#         temp = 0
#     i += 1
# print(ans)

# =================================================================
# a = [10, 'hiee', 3+5j, 10, 3, 'hiee']
# sett = []
# i = 0
# while i  < len(a):
#     if a[i] not in sett:
#         sett.append(a[i])
#     i += 1
# print(sett)

# =================================================================
# a = '((())())('
# open = 0
# close = 0
# i = 0
# while i < len(a):
#     if a[i] == '(':
#         open += 1
#     else:
#         close += 1
#     i += 1
# print(open - close)

# # method 2
# ans = a.count('(')- a.count(')')
# if ans < 0 :
#     print (ans * -1)
# else:
#     print (ans)

# # method 3
# print(abs(a.count('(')- a.count(')')))

# =================================================================
# check a number is perfect number or not
n = int(input())
i = 1
ans = 0
while i < n:
    if n % i == 0:
        ans += i
    i+= 1
if n == ans:
    print('perfect number')
else:
    print('not perfect number')


# =================================================================
# a = 'python programming on while loop'
# b = a.split(' ')
# i = 0
# ans = {}
# while i < len(b):
#     ans[b[i][::-1]] = 0
#     if 'h' in b[i]:
#         ans[b[i][::-1]] = 1
#     i += 1
# print(ans)

a = 'Hai Hello'
b = a.split(' ')
ans = {}
i = 0
while i < len(b):
    ans[b[i]]  = [b[i], len(b[i]) * 2, b[i][::-1]+ str(len(b[i]))]
    i += 1
print(ans)


