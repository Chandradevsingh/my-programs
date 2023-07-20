import functools



def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #Do something before the function execution
        result = func(*args, **kwargs)
        #Do something after the function execution
        return result
    return wrapper


# @start_end_decorator
# def print_name():
#     print('Alex')

# print_name = start_end_decorator(print_name)

@my_decorator
def add5(x):        #TypeError: start_end_decorator.<locals>.wrapper() 
                    #takes 0 positional arguments but 1 was given
    return x + 5

# result = add5(10)
# print(result)
print(add5(10))

# print_name()