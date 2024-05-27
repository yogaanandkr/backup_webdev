# class one:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class two(one):
#     def __init__(self,name, age, course, duration):
#         super().__init__(name, age)
#         self.course = course
#         self.duration = duration

#     def display(self):
#         print(self.name, self.age, self.course, self.duration)

# ob = two('anand', 22, 'python', 6)
# ob.display()

class one:
    oneName = 'anand'
    def __init__(self, nameone):
        self.nameone = nameone

class two:
    twoName = 'twoooo'
    def __init__(self, nametwo):
        self.nametwo = nametwo

class three(two, one):
    threeName = 'threeee'
    def __init__(self,nameone,nametwo, namethree):
        super().__init__(nameone)
        super().__init__(nametwo)
        self.namethree = namethree

        print(self.nameone, self.nametwo, self.namethree)

ob = three('nameone', 'nametwo', 'namethree')