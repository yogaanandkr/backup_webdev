# a = open('/home/yoga-anand/dev/psp/python/advance/new.txt', "a")
# # b = a.read()
# # print(a.read())
# # a.write('''print("helloworld")\n''')
# a.writelines(['hello\n','world'])
# a.close()
# a = open('/home/yoga-anand/dev/psp/python/advance/new.txt', "r+")
# print(a.read())
# # print(a.readline())
# # print(a.readline())
import csv
a = open('excel.csv', 'w')
b = csv.writer(a)
b.writerow(['sno', 'name', 'age'])
b.writerows([['01', 'anand', '22'],['02', 'yoga','20']])
a.close()

c = open('excel.csv', 'r')
d = csv.reader(c)
print([i for i in d if i != []])


