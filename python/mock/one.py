ans = '123'
num = int(ans)
sum = 0
while num>0:
    ld = num%10
    sum = sum + ld
    num = num//10

print(sum)