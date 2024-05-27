a = 'hello'
b = 'bye'
out= ''
if(len(a)>len(b)):
    large = len(a)
else:
    large = len(b)
for i in range(large):
    if (i<len(b)and i<len(a)):
        out += a[i] + b[i]
    else:
        out+= a[i]
print(out)