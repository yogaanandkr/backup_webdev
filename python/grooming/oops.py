class inher:
    cname = 'python' #static/class member

    # def __init__(self, name, age ):
    #     self.name = name
    #     self.age = age

    def start(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)
        self.detail(self.name, self.age)

    def chage(self, new):
        self.age = new
    
    @classmethod
    def ch_name(cls, new):
        cls.cname = new
        cls.age = new

    @staticmethod
    def detail(a, b):
        print('hi im', a, 'and my age is', b )


ob = inher()
ob.start('anand', 22)
ob.mark = 88
ob.chage(20)
print(ob.age)
print(ob.cname, 'before chage')
ob.ch_name('yoga')
print(ob.cname)
print(ob.age)
ob.detail('pytthon', 10000)
