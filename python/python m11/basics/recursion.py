# sum of n numbers
def sum(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
    
# print(sum(3))
    
# =================================================================
a = 'PyThon IS EASY'
i = 0
out = ''
while i < len(a):
    if 'A'<= a[i] <='Z':
        out += a[i]
    i += 1
# print(out)

def upper(a, i = 0, out = ''):
    if i == len(a):
        return out
    if 'A'<= a[i] <='Z':
        out += a[i]
    return upper(a, i+1, out)

# print(upper('PyThon IS EASY'))


# =================================================================
# extract all the integers from the list

a = [1,'A', 3, 'Z', 4, 'g', 5]

# with while loop
# i = 0
# out = []
# while i < len(a):
#     if type(a[i]) == int:
#         out += [a[i]]
#     i += 1
# print(out)

# with recursion
def integer(a, i = 0, out = []):
    if i == len(a):
        return out
    if type(a[i]) == int:
        out += [a[i]]
    return integer(a, i+1, out)
# print(integer(a)) 

# ==================================================================

# if the number is even print square of number

a = [2, 4, 'hiee', 71, 8, 3+5j]

# using while loop
# i = 0
# out = []
# while i < len(a):
#     if type(a[i]) == int and a[i]% 2 == 0:
#             out += [a[i]**2]
#     else:
#         out += [a[i]]
#     i += 1
# print(out)

# using recursion
def int_sq(a, i=0, out = []):
    if i == len(a):
        return out
    if type(a[i]) == int and a[i]% 2 == 0:
            out += [a[i]**2]
    else:
        out += [a[i]]

    return int_sq(a, i+1, out)

# print(int_sq(a))


# =================================================================

# add into dictionary if the word is present more than once

a = 'python is very easy and is very funny is'.split()
# a = a.split()

# i = 0
# out = {}
# while i < len(a):
#     if a.count(a[i]) > 1 and a[i] not in out:
#         out[a[i]] = a.count(a[i])
#     i += 1
# print(out)

# using recursion
def str_d(a, i = 0, out = {}):
    if i == len(a):
        return out
    if a.count(a[i]) > 1 and a[i] not in out:
        out[a[i]] = a.count(a[i])
    return str_d(a, i+1, out)
# print(str_d(a))

# =================================================================

a = ['one', 'two', 'eight']
b = ['four', 'six', 'zero']
nums = {'zero':0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}
out = ''

for i in range(len(a)):
    a[i] = nums[a[i]]
    b[i] = nums[b[i]]

for i in range(len(a)):
    out += str(a[i] + b[i])

# print(int(out))

def get(a):
    nums = {'zero':0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}

    out = ''
    for i in a:
        out += str(nums[i])
    return int(out)

a = ['one', 'two', 'eight']
b = ['four', 'six', 'zero']
# print(get(a)+get(b))

# =================================================================
# lower case alphabets from given string which is in the even index

def lower(a, i = 0, out = ''):
    if i == len(a):
        return out
    if i % 2 == 0 and 'a'<= a[i] <= 'z':
        out += a[i]
    return lower(a, i+1, out)
# print(lower('pYThon'))

# =================================================================
# 

def fact(s, e, out = []):
    if s == e+1:
        return out
    factorial = 1
    
    for i in range(2,s+1):
        factorial *= i
    out += [factorial]

    return fact(s+1, e, out)
# print(fact(1, 5))


def fact(a):
    if a == 0 or a == 1:
        return 1
    return a * fact(a-1)

out = []
for i in range(1, 10):
    out += [fact(i)]
# print(out)


a = [1,2,3,4,5]
def yieldd(a):
    i = 0
    while i < len(a):
        yield a[i]
    i+=1
print(list(yieldd(a)))