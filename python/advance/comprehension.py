a = [1,2,3,4,5,6,7,8]
# b = [i for i in range(1,11)]
# print(b)
# str1 = (('one', 1), ('two', 2), ('three', 3), ('four', 4))
# ans = {a:b for a, b in str1 }
# print(ans)

# wap to extract all the even nos from range 1 to 100
ans = [i for i in range(1,101) if i%2==0]
# print(ans)


# =================================================================
# wap to extract all the integers from given list
a = ['hello', 10, 'world', 20, 30]
ans = [i for i in a if type(i)== int]
# print(ans)

# =================================================================
a = [10, 'hiee', [1,2,3],9.8, 3+5j]
ans = [len(i) if type(i) in [list, str, dict, tuple, set] else 1 for i in a ]
# print(ans)

a = 'Python is very easy'
ans = [(i, len(i)) for i in a.split()]
# print(ans)

# a = [(1,3), (1,4), (1,5), (2,3),]
a = [1,2,3]
b = [3,4,5]
ans = {(i,j)for i in a for j in b}
# print(ans)

ans = []
for i in a:
    for j in b:
        ans += [(i,j)]
# print(ans)


# =================================================================
# wap to print sq of number if its even print cube of it 
sq = {i**2 if i % 2==0 else i**3 for i in range(1, 101)}
# print(sq)

a = ['a', 'b', 'c', 'd', 'e', 'f']
b = [1,2,3,4]
ans = {i:j for i,j in zip(a,b)}
print(ans)