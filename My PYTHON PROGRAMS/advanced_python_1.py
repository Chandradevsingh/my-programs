#Exceptions
# a = 5
# b = c       #NameError: name 'c' is not defined
# f = open("somefile.txt")        #FileNotFoundError: [Errno 2] No such file or directory: 'somefile.txt'

# a = [1, 2, 3]
# # a.remove(4)        #ValueError: list.remove(x): x not in list
# print(a)

# print(a[4])        #IndexError: list index out of range

# my_dict = {"name": 'Max'}
# print(my_dict["age"])        #KeyError: 'age'   

# x = 5
# if x < 0:
#     raise Exception('x should be positive.')        #Base Exception

# x = -5
# assert(x>=0)        #AssertionError

# x = -5
# assert(x>=0), 'x is not positive'        #AssertionError: x is not positive

# try:
#     a = 5/0
# except:
#     print('an error happened.')

# try:
#     a = 5/0
# except Exception as e:
#     print(e)

# try:
#     a = 5/0
#     b = a + "10"
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('everything is fine.')

# try:
#     a = 5/1
#     b = a + "10"
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('everything is fine.')

# try:
#     a = 5/1
#     b = a + 4
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('everything is fine.')
# finally:
#     print('cleaning up...')

# class ValueTooHighError(Exception):
#     pass

# class ValueTooSmallError(Exception):
#     def __init__(self, message, value):
#         self.message = message
#         self.value = value
        
# def test_value(x):
#     if x > 100:
#         raise ValueTooHighError('Value is too high.')        #ValueTooHighError: Value is too high.
#     if x < 5:
#         raise ValueTooSmallError('Value is too small.', x)
    
# try: 
#     test_value(1)
# except ValueTooHighError as e:
#     print(e)
# except ValueTooSmallError as e:
#     print(e.message, e.value)

#Logging

