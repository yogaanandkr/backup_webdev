string = 'abc' #yad #yac
out = ''
i = 0
j = 1
ch = 'r'

if ch == 'l' and j > i+1:
    print('into first')
    for a in range(len(string)):
        if i > a:
            out += string[a]
        else:
            if(chr(ord(string[a])-1) == '`'):
                out+= chr(ord(string[a])+ 25)
            else:
                out+= chr(ord(string[a])-1)
else:
    for a in range(len(string)):
            if a == i:
                if(chr(ord(string[i])-1) == '`'):
                    out+= chr(ord(string[i])+ 25)   
                else:
                    out+= chr(ord(string[i])-1)
            elif a == j:
                out += chr(ord(string[j])-1)
            else:
                out += string[a]
print(out)

out = ''
if ch == 'r' and j > i+1:
    for a in range(len(string)):
        if i > a:
            out += string[a]
        else:
            if(chr(ord(string[a])) == 'z'):
                out+= chr(ord(string[a])- 25)
            else:
                out+= chr(ord(string[a])+1)
else:
    for a in range(len(string)):
            if a == i:
                if(chr(ord(string[i])) == 'z'):
                    out+= chr(ord(string[a])- 25)
                else:
                    out+= chr(ord(string[a])+1)
            elif a == j:
                out += chr(ord(string[a])+1)
            else:
                out += string[a]

print(out)