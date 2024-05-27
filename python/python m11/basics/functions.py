# a = 'python' out = 'Python
def cap():
    a = 'python'
    b=''
    
    for i in range(len(a)):
        if i == 0 and 'a'<= i <= 'z':
            b += chr(ord(a[i])-32)
        else:
            b += a[i]
    print(b)
# cap()


# =================================================================
# a = '110$101#110' out = '    a = '110$101#110''
def convert():
    a = '110$101#110'
    out = ''
    for i in a:
        if i == '1':
            out+= '0'
        elif i == 0:
            out+= '1'
        elif i in '!@#$%^&*()<>?':
            out+= '*'
    print(out)

# convert()
    
# =================================================================
# sum of two numbers
def sum(a, b):
    print(a + b)

# sum(int(input('num 1: ')), int(input('num 2: ')))

# =================================================================
# extract all the numbers from a string and return their sum as output
def mailsum(email):
    sum = 0
    for i in email:
        if '0'<= i <='9':
            sum += int(i)
    print(sum)
# mailsum('yokeshanand762001@gmail.com')
    
# =================================================================
# a = [12, 'Hiee', (1,2,3), 3+5j, 9.8]
def check(col):
    out = []
    tup = ()
    for i in range(len(col)):
        if type(col[i]) in [int, float, complex, bool]:
            out += [(col[i], 1)]         
        else:
            out += [(col[i], len(col))]
    print(out)

# check([12, 'Hiee', (1,2,3), 3+5j, 9.8])

# =================================================================
# return the numbers which are palindrome in a list
    
def palindrome(list):
    out = []
    for i in list:
        if str(i) == str(i)[::-1]:
            out += [i]
    print(out)

# palindrome([111, 234, 414, 777])


# method 2 (without type casting)
def palindrome1(list):
    out = []
    for i in list:
        d = i
        num = 0
        while d > 0:
            ld = d % 10
            num = num * 10 + ld
            d = d // 10

        if num == i:
            out += [num]
    print(out)

# palindrome1([111, 234, 414, 777])


# =================================================================
    # join

# a = ['hiee', 'how', 'are', 'you']
# for i in range(len(a))
#     a[i] = a[i].capitalize()

# print(' '.join(a))
    
# =================================================================
# wap to count all the uppercase from given string and its ascci value is divisible by 3

def ascci():
    a = "Hello, Are YOU ThEre"
    count = 0
    ans = ''
    for i in a:
        if 'A' <= i <= 'Z' and ord(i) % 3 == 0:
            count += 1
            ans += i 
    return count, ans

# print(ascci())
                                                                                                          
# =================================================================
# in = 'Python is Programming Language'  
# op = {'P': ['Python', 'Programming'], 'i': ['is'], 'L': ['Language']}

def dictionary():
    a = 'Python is Programming Language'.split()
    out = {}

    for i in a:
        if i[0] in out:
            out[i[0]].append(i)
        else:
             out[i[0]] = [i]
    return out

# print(dictionary())

# =================================================================
# make a list act as a set

def convert():
    list = [10, 'Hiee', 3+5j, 'Hiee', 10, 39]
    out = []
    for i in list:
        if i not in out and list.count(i) == 2:
            out += [i]
            
    return out

# print(convert())

# =================================================================

#                                           WITH ARGUMENTS WITH RETURN VALUES

# =================================================================
# convert all the small letters into capital letters from a given string

def convert_alpha(a):
    ans = ''
    for i in a:
        if 'a'<= i <='z':
            print(i)
            ans += chr(ord(i)-32)
        else:
            ans += i
    return ans

# print(convert_alpha('hello How are you'))

# =================================================================
# greatest number in list 

a = [45244,1,2,1000000,3,4,5,458,6,7]

def greater(a):
    greater = 0
    for i in range(len(a)):
        for j in range(0, len(a)):
            if a[i] > a[j] and a[i] > greater:
                greater = a[i]
            
    return greater

# print(greater(a))

# =================================================================
a = [12, 'hello', 'star', 8 ,3+6j, 'ab', 9,4.5,'happy']

def string(a):
    out = []
    for i in range (0,len(a)):
        if type(a[i]) == str and i % 2 == 0:
            out += [len(a[i])]

        else:
            out += [a[i]]
    return out

# print(string(a))


# =================================================================
a = 'python is very easy'

def convert_d(a):
    out = {}
    for i in a.split():
        out[i] = i[::-1] + str( len(i))
    return out

# print(convert_d(a))


# =================================================================
a = 'mother in law'
b = 'hitler woman'
# print(sorted(a))
def anagram(a, b):
    a1 = ''
    b1 = ''
    
    for i in a:
        if i != ' ':
            a1+= i
    for i in b:
        if i != ' ':
            b1+=i
    print('a1', a1)
    print('b1', b1)
    print(sorted(a))
    print(sorted(b))
    if sorted(a1) == sorted(b1):
        return 'anagram'
    else:
        return 'not anagram'
    
# print(anagram(a,b))



# =================================================================
# CALCULATOR34
def addition(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a,b):
    return a / b
    
def calculator(a, b, input):
    if input == '1':
        return addition(a,b)
    if input == '2':
        return sub(a,b)
    if input == '3':
        return mul(a,b)
    if input == '4':
        return div(a,b)
    else:
        return 'invalid input'
# a = int(input('enter 1st operand: '))
# b = int(input('enter 2nd operand: '))
# input = input('''enter 1 for + 
#       enter 2 for -
#       enter 3 for *
#       enter 4 for / : ''')
# print(calculator(a,b, input))

# a = 10
# b = 20
# def fun():
#     global b
#     b = 30
# print(b)
# fun()
# print(b)