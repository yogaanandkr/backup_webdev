class encap:
    course = 'python'

    def check(self):
        print(self.course)

    class two(encap):
        def __init__(self):
            print(self.course)

# ob=encap()
# ob.check()
ob2 = encap.two()
print(ob2.__course)