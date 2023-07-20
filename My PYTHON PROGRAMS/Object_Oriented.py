# class Dog:
#     def bark(self):
#         print("bark")

# d = Dog()
# d.bark()
# print(type(d))

# #F- string
# name = "Dev"

# print("Hello", name)
# print("Hello " + name)
# print(f"Hello {name}")
# print(F"Hello {name} {name * 2}")
# print(F"Hello {2+3}")

# print(F"Hello {[1, 2, 3, 4]}")
# x = F"Hello {[1, 2, 3, 4]}"
# print(x)

# #unpacking
# tup = (1, 2, 3, 4, 5)
# lst = [1, 2, 3, 4, 5]
# string = "hello"
# dic = {"a": 1, "b": 2}
# coords = [4, 5]

# a, b, c, d, e = tup
# print(a, b, c, d, e)
# a, b, c, d, e = lst
# print(a, b, c, d, e)
# a, b, c, d, e = string
# print(a, b, c, d, e)
# a, b = dic
# print(a, b)
# a, b = dic.values()
# print(a, b)
# a, b = dic.items()
# print(a, b)
# x, y = coords
# print(x, y)
# # x, y = coords        #returns error because we don't have enough values to assign to these three variables.
# # print(x, y)

# #Multiple Assignment or Variable swap
# width, height = 400, 500
# width, height = height, width

# print(width, height)        #We've swamped the width and the height.

#Comprehension

# for i in range(100):      #This is not the pythonic way to do it. The pythonic way to do this is the following. 
#     x.append(0)

# x = [0 for i in range(100)]
# print(x)
# x = [i for i in range(100)]
# print(x)
# x = [i for i in range(100) if i % 2 == 0]
# print(x)
# x = [i*j for i in range(100) for j in range(10)]
# print(x)
# x = [[0 for _ in range(5)] for _ in range(5)]
# print(x)
# x = (i for i in "hello")
# print(tuple(x))

# sentence = "Hello, my name is dev"
# x = {char: sentence.count(char) for char in set(sentence)}
# print(x)

#Object Multiplication

# x = "dev" * 5
# print(x)

# x = [[1, 2, 3, 4, 5]] * 5
# print(x)

# x = (1, 2) * 5
# print(x)

# x = (1, 2) * (1, 2)     #returns a TypeError: can't multiply sequence by non-int of type 'tuple'
# print(x)

#Inline/Ternary Condition/ If statement

# x = 1 if 2 < 3 else 0
# print(x)

# x = 2 > 3 ? 1 : 0       #Javascript's Ternary Condition

# if 2 > 3:
#     x = 1
# else:
#     x = 0

#Zip function

# names = ["Dev Chauhan", "Sudheer Shekhawat", "Aditya Chauhan"]
# ages = [29, 30, 29]
# eye_color = ["Blue", "Brown", "Green"]

# print(list(zip(names, ages, eye_color)))
# # print(tuple(zip(names, ages, eye_color)))

# for names, ages, eye_color in zip(names, ages, eye_color):
#     if ages > 20:
#         print(names)
#     print(eye_color)

#*args and **kwargs

# def func1(arg1, arg2, arg3):
#     print(arg1, arg2, arg3)

# def func2(arg1 = None, arg2 = None, arg3 = None):
#     print(arg1, arg2, arg3)

# args = [1, 2, 3]
# kwargs = {"arg2" : 2, "arg1" : 1, "arg3" : 3}

# func1(*args)
# func2(**kwargs)

#For Else and While Else

# search = [1, 2, 3, 4, 5, 6, 7]
# target = 7
# found = False

# for element in search:
#     if element == target:
#         print('I found it!')
#         break
# else:
#     print('I didn\'t find it!')

# while i < len(search):
#     element = search[i]
#     if element == target:
#         print('I found it!')
#         break
#         i += 1
# else:
#     print("I didn't find it!")

#Sort by key
# lst =[[1, 2], [3, 4], [4, 2], [-1, 3], [4, 5], [2, 3]]

# def sort_function(x):
#     return x[0] + x[1]

# # lst.sort(key=lambda x: x[1] + x[0])
# lst.sort(key=sort_function)
# sorted(lst, key=)
# print(lst)

#Bonus - Itertools

import itertools

lst = [1, 2, 3, 4, 5]
sum_list = itertools.accumulate(lst)
print(list(sum_list))

lst2 = ['A', 'B', 'C', 'D']
chain_list = itertools.chain(lst, lst2)
print(list(chain_list))

name = ["Dev", "Sudheer", "Aditya", "Harsh", "Mohit"]
show = [1, 0, 1, 0, 1]
compressed_list = itertools.compress(name, show)
print(list(compressed_list))