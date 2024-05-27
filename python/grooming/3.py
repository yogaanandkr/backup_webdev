class par:
    _name = 'Ramesh'

    def role(self):
        print(self._name, 'is my dad')

class child(par):
    ch_name = 'anand'
    
    def ch_role(self):
        print(self.ch_name, 'is son of', self._name)
        super().role()  
        self.sta(self.ch_name)

    @staticmethod
    def sta(a):
        print('hello im static method', a)


    def __del__(self) :
        print("destructor called all deleted")


ob = child()
ob.ch_role()
# del ob
# ob.ch_role()    

# print(str('hello'))

# print(chr(ord('A')+ 32))