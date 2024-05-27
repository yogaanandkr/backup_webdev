# class poly:
#     def work(self):
#         print('i can work')


# class poly2(poly):
#     def work(self):
#         print('i will not work')
#         super().work()

# ob = poly2()
# ob.work()

class oper:
    def __init__(self, a) -> None:
        self.a = a

    def __add__(self, other):
        print(self.a + other.a)

    def __sub__(self, other):
        print(self.a - other.a)

ob1 = oper(5)
ob2 = oper(10)
ob1-ob2