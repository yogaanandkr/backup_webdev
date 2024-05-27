class human:
    def __init__(self, name) -> None:
        self.name = name
        print('im init fun of human class')
    
    def eat(self):
        print(f'{self.name} can eat')

class male(human):
    def __init__(self, male_name) -> None:
        self.male_name = male_name
        print("i'm init method of male")

    def work(self):
        print(f'{self.male_name} can work')

class female(human):
    def __init__(self, female_name, name) -> None:
        human.__init__(self,name)
        self.female_name = female_name
        print("i'm init method of female")

    def sleep(self):
        print(f'{self.female_name} can sleep')

ob = female('sushi', 'pandaram')
ob.sleep()
ob.eat()

