class Zoo:
    a = 'anaconda'
    b = 'buffalo'
    c = 'camel'

ob1 = Zoo()
ob2 = Zoo()

# Zoo.b = 'bear'
# print(Zoo.a,Zoo.b, Zoo.c)
# print(ob1.a,ob1.b, ob1.c)
# print(ob2.a,ob2.b, ob2.c)
# ob1.c = 'cheetah'
# print(Zoo.a,Zoo.b, Zoo.c)
# print(ob1.a,ob1.b, ob1.c)
# print(ob2.a,ob2.b, ob2.c)
# ob2.a = 'python'
# print(Zoo.a,Zoo.b, Zoo.c)
# print(ob1.a,ob1.b, ob1.c)
# print(ob2.a,ob2.b, ob2.c)


class bank:
    bname = 'HDFC'
    bloc = 'Nagawara'
    bIFSC = 'HDFC0000765'

omen = bank()

omen.name = 'Omen'
omen.email = 'omenduelist@gmail.com'
omen.phno = 7397576683
omen.accno = 194108120706
omen.place = 'madurai'

# print(f''ANK NAME ; {omen.bname}
# NAME: {omen.name}
# EMAIL: {omen.email}
# PHNO: {omen.phno}
# ACCNO: {omen.accno}
# PLACE: {omen.place}
# BANK LOCATION: {omen.bloc}
# IFSC: {omen.bIFSC}
# ''')


class library:
    lib_name = 'brainup'
    lib_branch = 'bangalore'
    lib_closing_time = '10:00 pm'

    def __init__(self, name, age, borrowed, returned, attendance):
        self.name = name
        self.age = age
        self.books_borrowed = borrowed
        self.books_returned = returned
        self.avg_weekly_attendance = attendance
    
obj1 = library('Iron man', 33, 10, 5, 3.3)


# obj2 = library()


# obj3 = library()


# print(f'''LIBRARY NAME ; {obj1.lib_name}
# lib_branch: {obj1.lib_branch}
# name: {obj1.name}
# age: {obj1.age}
# books_borrowed: {obj1.books_borrowed}
# books_returned: {obj1.books_returned}
# avg_weekly_attendance: {obj1.avg_weekly_attendance}
# ''')

class hospital:
    hospital_name = 'Global'
    hospital_location = 'Chennai'
    hospital_duration = '24hrs'

    def __init__(self, name, age, doctor, phno, city, problem, admitted):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.phno = phno
        self.city = city
        self.problem = problem
        self.admitted = admitted

# pat1 = hospital('abc', 43, 'Anand', 34232344232, 'bangalore', 'heart', True)
# pat2 = hospital('def', 55, 'santhosh', 75646566464, 'chennai', 'brain', False)
# pat3 = hospital('ghi', 80, 'vaibhavi', 86465654552, 'hyderabad', 'kidney', True)

# print(f'''hospital name ; {pat1.hospital_name}
# hospital_location: {pat1.hospital_location}
# hospital_duration: {pat1.name}
# name: {pat1.name}
# age: {pat1.age}
# doctor: {pat1.doctor}
# phno: {pat1.phno}
# city: {pat1.city}
# problem: {pat1.problem}
# admitted: {pat1.admitted}
# ''')

# print(f'''hospital name ; {pat2.hospital_name}
# hospital_location: {pat2.hospital_location}
# hospital_duration: {pat2.name}
# name: {pat2.name}
# age: {pat2.age}
# doctor: {pat2.doctor}
# phno: {pat2.phno}
# city: {pat2.city}
# problem: {pat2.problem}
# admitted: {pat2.admitted}
# ''')


# print(f'''hospital name ; {pat3.hospital_name}
# hospital_location: {pat3.hospital_location}
# hospital_duration: {pat3.name}
# name: {pat3.name}
# age: {pat3.age}
# doctor: {pat3.doctor}
# phno: {pat3.phno}
# city: {pat3.city}
# problem: {pat3.problem}
# admitted: {pat3.admitted}
# ''')


# out = 'hbeylelo'
a= 'hello'
b = 'bye'
out = ''
great = len(a) if len(a)>len(b) else len(b)
for i in range(great):
    if i < len(b) and i < len(a):
        out += a[i] + b[i]
    elif i < len(a):
        out += a[i]

# print(out)

# out = 'hbeylelo'
a= 'hello'
b = 'bye'
out = ''
for i in range(max(len(a),len(b))):
    if i<len(a):
        out+=a[i]
    if i<len(b):
        out+=b[i]
# print(out)
        
    
class bike:

    # def __init__(self):
    #     print('init')
    def wheels(self, name, years):
        self.name = name
        self.years = years


pulsar = bike()
bike.wheels(pulsar,'fzs', 3)
# print(pulsar.name, pulsar.years)
# pulsar.wheels()
# apachee = bike()


class company:
    def __init__(self, name, id, sal, desig):
        self.name = name
        self.id = id
        self.sal = sal
        self.desig = desig

    def display(self):
        print(self.name, self.id, self.sal, self.desig)

    def ch_sal(self, new_sal):
        self.sal = new_sal

    def ch_desig(self, new_desig):
        self.desig = new_desig

# emp1 = company('anand', 1, 1000000, 'CEO')
# emp1.display()
# emp1.ch_sal(9000000)
# emp1.display()


class m11:
    trainer = 'Mr. Deepak'
    subject = 'Python'


    def __init__(self, name, age, email, mock_rating):
        self.name = name
        self.age = age
        self.email = email
        self.mock_rating = mock_rating

    @classmethod
    def ch_sub(cls, new):
        cls.subject = new

    def display(self):
        print(f'''Hi I'm {self.name} and I'm {self.age} years old. I'm a student of {self.trainer} who is training me on {self.subject} and I scored rating of {self.mock_rating} in mock''')

    def ch_mock_rating(self, new_rating):
        self.mock_rating = new_rating

    def ch_email(self, new_email):
        self.email = new_email

# anand = m11('Anand', 22, 'yokeshanand762001@gmail.com', 'p1c1')
# anand.display()
# anand.ch_mock_rating('p*c*')
# print(m11.subject)
        
# m11.ch_sub("sql")
# print(m11.subject)
# anand.display()


class hotel:
    h_name = "Anjappar"
    h_rating = 9.5

    def __init__(self, cname, cemail, cphno, crating, cregular):
        self.cname = cname
        self.cemail = cemail
        self.cphno = cphno
        self.crating = crating
        self.cregular = cregular

    @classmethod
    def ch_rating(cls, new):
        cls.h_rating = new
        print("Hotel name: ", cls.h_name, '\t',"Hotel rating (new): ", cls.h_rating)

    def display_customer(self):
        print("customer name: ", self.cname, '\n')
        print("customer email: ", self.cemail, '\n')
        print("customer phno: ", self.cphno, '\n')
        print("customer crating: ", self.crating, '\n')
        print("customer cregular: ", self.cregular, '\n')

    def ch_crating(self, new):
        self.crating = new

# c1 = hotel('Anand', 'anand@gmail.com', 7397576683, 10, True)
# c1.display_customer()
# print(hotel.h_rating)
# hotel.ch_rating(10)
# print(hotel.h_rating)

# =================================================================
# wap to create a class name bank with min 3 static members with 2 object, 5 object members and create a method to withdraw and deposit
class bank:
    bname = 'Axis'
    bloc = 'Madurai'
    bIFSC = 'AXIS000002562'

    def __init__(self, cname, pho, acc, bal):
        self.cname = cname
        self.pho = pho
        self.acc = acc
        self.bal = bal

    def display(self):
        print(f' \nBank Name: {self.bname} \n Bank Location: {self.bloc} \n Cust name: {self.cname} \n Cust account: {self.acc} \n Cust balance: {self.bal}')

    @classmethod
    def disp_cls(cls):
        print(cls.bname, cls.bloc, cls.bIFSC)

    def deposit(self, amt):
        self.bal = self.add(self.bal, amt)
        print('deposited amount: ', amt, '\n', 'acc balace: ', self.bal)

    def withdraw(self, amt):
        if (amt > self.bal):
            return 'insufficient balance'
        self.bal = self.sub(self.bal, amt)
        print('withdrawn amount: ', amt, '\n', 'acc balace: ', self.bal)



    @staticmethod
    def add(a,b):
        return a + b
    @staticmethod
    def sub(a,b):
        return a - b

anand = bank('Anand', 73975766833, 10025658255248963, 500000)
print(anand)
# # anand.display()
# anand.deposit(100)
# print(anand.withdraw(500101))


# =================================================================
# wap to find sum of two number using obj method, class method, static method

class sum:
    aa = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print (self.a + self.b)

    @classmethod
    def c_sum(cls, one, two):
        cls.aa = one
        cls.b = two
        return cls.aa + cls.b
    
    def s_sum(self, a, b):
        return self.s_sum(a, b)
    
    @staticmethod
    def s_sum(a, b):
        return a + b
    
# sum1 = sum(44,4)
# print(sum1.aa)
# print(sum1.c_sum(3,4))
# print(sum1.s_sum(10, 10))
# print(sum1.aa)
# sum2 = sum(1,1)
# print(sum2.aa, 'sum2 aa')

# =================================================================
# wap to create a library   
class library:
    books = {'python': 20, 'sql':10, 'web': 50, 'django': 60, 'java': 5}

    def __init__(self, books_issued = {}):
        self.books_issued = books_issued
        self.issued = False
        for i in self.books:
            self.books_issued[i] = False
        nxt = input("enter 1. to get some other books.   enter 2. to return books: ")
        if nxt == '1':
            self.issue()
        if nxt == '2':
            self.returnn()

    # @classmethod
    # def ch_rec(cls, name):
    #     cls.books[name] -= 1

    def issue(self, name = ''):
        print(self.books)
        name  = input("enter the book to be issued: ")
        if self.books[name] > 0 and self.books_issued[name] == False:
            print(f"{name} issued to ")
            self.books_issued[name] = True
            self.issued = True
            self.books[name] -= 1
            # self.ch_rec(name)
            nxt = input("enter 1. to get some other books.   enter 2. to return books: ")
            if nxt == '1':
                self.issue()
            if nxt == '2':
                self.returnn()
    
        elif self.books[name] == 0:
            print(self.books)
            print (f"there are no {name} books left")
            nxt = input("enter 1. to get some other books.   enter 2. to return books: ")
            if nxt == '1':
                self.issue()
            if nxt == '2':
                self.returnn()
        elif (self.books_issued[name] == True):
            print(f"you already have borrowed {name} book")
            nxt = input("enter 1. to get some other books.   enter 2. to return books: ")
            if nxt == '1':
                self.issue()
            if nxt == '2':
                self.returnn()
        else:
            print('enter a valid book name')
            nxt = input("enter 1. to get some other books.   enter 2. to return books: ")
            if nxt == '1':
                self.issue()
            if nxt == '2':
                self.returnn()

    def returnn(self, name = ''):
        print(self.books)
        name  = input("enter the book to be returned: ")
        if (self.issued == True) and (self.books_issued[name] == True):
            self.books[name] += 1
            self.books_issued[name] = False
            for i in self.books_issued:
                if self.books_issued[i] == True:
                    break
                else:
                    self.issued = False
            nxt = input("enter 1. to get some other books.   enter 2. to return books: ")
            if nxt == '1':
                self.issue()
            if nxt == '2':
                self.returnn()
        else:
            print (f"you didnt borrowed {name} book")
            nxt = input("enter 1. to get some other books.   enter 2. to return books: ")
            if nxt == '1':
                self.issue()
            if nxt == '2':
                self.returnn()

    def display(self):
        print(self.books)

# anand = library()
# anand.display()
# anand.issue()
# anand.display()
# anand.returnn()
# anand.display()
# print(library().books)
        
class Amazon:
    products = {
        "ps5":{"price": 45000, "avl_qty": 500}, "laptop":{"price": 75000, "avl_qty": 600},"watch":{"price": 5000, "avl_qty": 2000}
    }

    def __init__(self, name, phno, email, bought={}):
        self.name = name
        self.phno = phno
        self.email = email
        self.bought = bought

    def buy(self, p_name='', qty=0):
        p_name = input("enter the product name: ").lower()
        qty = int(input("Enter the qty to purchase: "))
        if p_name in self.products:
            if qty < self.products[p_name]["avl_qty"]:
                self.bought[p_name] = {"price": self.products[p_name]["price"]*qty, "qty": qty}
                print(f"Hi {self.name}, your invoice :{self.bought}")

                self.products[p_name]["avl_qty"] -= qty

                print("All products and avl_qty are: ", self.products)
            else:
                print("We don't have enough products try less qty")
                self.buy()
        else:
            print(f"We have no products in the name {p_name} enter a different product")
            
            self.buy()

print("Login to shop!!!")

# buyer1 = Amazon(input("enter your name: "), input("enter your phone number: "), input("enter your email: "))

buyer1 = Amazon("anand", 739757668, "anand@gmail.com")
buyer1.buy()

data = [['Hi', 'Python']]
print("yes" if 'hi' in data[0][0] else data[0][1])
