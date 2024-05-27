# Python program to illustrate destructor

# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     print(inner_function)
#     return inner_function

# closure_instance = outer_function(10)

# result = closure_instance(5)
# print(result)  # Output: 15

# def out(name):
#     def ins(age):
#         return (f'hello im {name} and im {age} years old')
#     return ins

# one = out('anand')
# two = one(22)
# print(two) 


# def parent(fun):
#     def child1():
#         print("im child 1")
#         fun()
#     return child1

# # @parent
# def child2():
#     print("im child 2")
# child21 = parent(child2)
# print(child21)


def fun():
    global a
    a = 10
fun()
print(a)
