def shop():
    item = int(input('enter the no of items: '))
    if item < 10:
        print('enjoy')
    else:
        raise SyntaxError('you cant take this much')
    
# shop()

try:
    shop()
except Exception as e:
    print(e)

    