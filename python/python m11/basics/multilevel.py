class bat:
    def __init__(self, brand, owner):
        self.brand = brand
        self.owner = owner

    def disp_obj1(self):
        print(self.brand, self.owner)

class ball:
    def __init__(self, ball_brand, ball_owner):
        self.ball_brand = ball_brand
        self.ball_owner = ball_owner

    def disp_obj2(self):
        print(self.ball_brand, self.ball_owner)

class stump:
    def __init__(self, s_brand, s_owners):
        self.s_brand = s_brand
        self.s_owners = s_owners

    def disp_obj3(self):
        print(self.s_brand,self.s_owners)

class cricket(bat, ball, stump):
    def __init__(self, brand, owner, ball_brand, ball_owner, s_brand, s_owner):
        bat.__init__(self, brand=brand, owner=owner)
        ball.__init__(self, ball_brand=ball_brand, ball_owner=ball_owner)
        stump.__init__(self, s_brand=s_brand, s_owners=s_owner)

    def disp_cric(self):
        print(self.brand, self.owner, self.ball_brand, self.ball_owner, self.s_brand,self.s_owners)

obj = cricket('ss', 'dhoni', 'puma', 'kholi', 'addidas', 'sachin')
obj.disp_cric()
