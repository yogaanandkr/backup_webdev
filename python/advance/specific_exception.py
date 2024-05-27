try:
    a = int(input("enter a: "))
    b = eval(input("enter b: "))
    c = a/b
    print(c)

except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)
except TypeError as e:
    print(e)

finally:
    print('hello')

# print(100/0)

# if (100/0):
#     print('success')

# else:
#     print("erroor")
    
# import builtins

# # Get all the attributes (error types) from the builtins module
# error_types = [getattr(builtins, error_name) for error_name in dir(builtins) if isinstance(getattr(builtins, error_name), type)]

# # Print the error types

# # try:
# #     a = int(input("enter a: "))
# #     b = eval(input("enter b: "))
# #     c = a/b
# #     print(c)
# # except
# # for error_type in error_types:
# #     try:
# #         pass
# #     except error_type as e:
# #         print (e)
