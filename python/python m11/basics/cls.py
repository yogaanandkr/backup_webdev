
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

c1 = hotel('Anand', 'anand@gmail.com', 7397576683, 10, True)
c1.display_customer()
print(hotel.h_rating)
# hotel.ch_rating(10)
print(hotel.h_rating)