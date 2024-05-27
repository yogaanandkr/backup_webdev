# def insta(fun):
#     def inner(*args, **kwargs):
#         print('args', args)
#         print('kwargs', kwargs)
#         for key, val in kwargs.items():
#             print(key, 'is', val)
#         print('logout...')
#     return inner

# @insta
# def a(*args, **kwargs):
#     print('chat', args)
#     print('dictionary', *kwargs)

# a('one', 'two', three = 3, four = 4)

import time

def calc(fun):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = fun(*args, **kwargs)
        print('result:', result)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'start_time: {start_time:.6f} seconds')
        print(f'end_time: {end_time:.6f} seconds')
        print(f'Time taken: {elapsed_time:.6f} seconds')
        return result
    return inner

@calc
def cube(a):
    return a * a * a

# Test the decorator
cube(3)
