try:
    a = int(input("enter a: "))
    b = eval(input("enter b: "))
    c = a/b
    print(c)
except Exception as e :
    print(e)