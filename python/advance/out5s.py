import time
# def gen(a):
#     time.sleep(5)
#     return a * 5

# # time.sleep(5)
# print(gen(5))

def calculate(fun):
    def inner(*args, **kwargs):
        result = fun(*args, **kwargs)
        time.sleep(5)
        return abs(result)
    return inner

@calculate
def sub(a, b):
    return a - b 
@calculate
def sum(a, b):
    return a + b
@calculate
def mul(a, b):
    return a * b
@calculate
def div(a, b):
    return a / b

print(sum(5, -10))
print(sub(5, 10))
print(mul(-5, 10))
print(div(5, -10))