import sqlite3
try:
    a = sqlite3.connect('my_db.db')
    b = a.cursor()
    b.execute('''CREATE TABLE IF NOT EXISTS emp(empid number(4) unique, ename varchar(20), age number(3))''')
    b.execute('''insert into emp values(7, 'anand', 21)''')
    # b.execute('''drop table if exists emp''')
    a.commit()
    a.close()
except Exception as e:
    print(e)

a = sqlite3.connect('my_db.db')
b = a.cursor()
res = b.execute('''select * from emp''')
print(res.fetchall())
a.close()