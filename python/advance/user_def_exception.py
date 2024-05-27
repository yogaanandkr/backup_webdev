class Notavailable(Exception):
    pass

item = int(input('enter the count: '))
if item < 1:
    raise Notavailable("value should be greater than 1")
else:
    print("thankyou for purchasing")