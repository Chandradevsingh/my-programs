#Lists
#Lists : ordered, mutable, allow duplicate elements
# mylist = ["banana", "cherry", "apple"]
# print(mylist)

# mylist2 = list()    #Create an empty list with list function
# print(mylist2)      #Later on you can append items

# mylist3 = [5, True, "apple", "apple"]
# print(mylist3)
# item = mylist3[0]
# print(item)
# item1 = mylist3[5]      #Gives error, IndexError: list index out of range.
# print(item1)
# last_Item = mylist3[-1]
# second_last_item = mylist3[-2]

# for i in mylist:        #You don't need to call this x, you can call this x.
#     print(i)

# if"banana" in mylist:
#     print("yes")
# else:
#     print("No")

# print(len(mylist))

# mylist.append("lemon")
# print(mylist)

# mylist.insert(1, "blueberry")
# print(mylist)

# item = mylist.pop() #This returns the last item and also removes it.
# print(item)
# item = mylist.remove("cherry") #This returns the last item and also removes it.
# print(mylist)
# item = mylist.clear()       #Removes or clears all elements.
# print(mylist)
# item = mylist.reverse()
# print(mylist)
# mylist.sort(reverse=True)
# print(mylist)
# new_list = sorted(mylist)
# print(mylist)
# print(new_list)
# mylist = [0]*5
# print(mylist)

# mylist1 = [1, 2, 3, 4, 5]
# newlist = mylist + mylist1
# print(newlist)
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # a = mylist[1:5]
# # print(a)
# # a = mylist[::2]
# # print(a)
# a = mylist[::-1]
# print(a)

#Memory assignment of the list in the memory
# list_org = ['banana', 'cherry', 'apple']
# list_copy = list_org
# list_copy.append('lemon')        #Both lists get modified.
# print(list_copy)
# print(list_org)

#Actual copy methods

# list_org = ['banana', 'cherry', 'apple']
# list_copy = list_org.copy()
# list_copy.append('lemon')
# print(list_copy)
# print(list_org)

# list_org = ['banana', 'cherry', 'apple']
# list_copy = list(list_org)
# list_copy.append('lemon')
# print(list_copy)
# print(list_org)

# list_org = ['banana', 'cherry', 'apple']
# list_copy = list_org[:]
# list_copy.append('lemon')
# print(list_copy)
# print(list_org)

# mylist = [1, 2, 3, 4, 5, 6]
# a = [i*i for i in mylist]
# # print(mylist)
# # print(a)

#Tuples
#Tuple : ordered, immutable, allow duplicate elements
#mytuple = ("Max", 28, "Boston")
# mytuple = "Max", 28, "Boston"
# mytuple = tuple(["Max", 28, "Boston"])
# print(mytuple)

# item = mytuple[0]
# item = mytuple[3]       #gives error, IndexError:  tuple index out of range

# mytuple[0] = "Dev"      #TypeError: 'tuple' object does not support item assignment
# for i in mytuple:
#     print(i)

# if "Tim" in mytuple:
#     print("yes")
# else:
#     print("No")

# mytuple = ('a', 'p', 'p', 'l', 'e')
# print(len(mytuple))

# print(mytuple.count('p'))
# print(mytuple.index('p'))
# print(mytuple.index('o'))       #ValueError: tuple.index(x): x not in tuple

# mylist = list(mytuple)
# # print(mylist)
# mytuple2 = tuple(mylist)
# print(mytuple2)

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# b = a[::-1]
# print(b)

# my_tuple = "Max", 28, "Boston"
# name, age = my_tuple        #ValueError: too many values to unpack (expected 2)
# print(name)
# print(age)
# print(city)

# my_tuple = [0, 1, 2, 3, 4]

# i1, *i2, i3 = my_tuple

# print(i1)
# print(i2)
# print(i3)

# import sys

# my_list = [0, 1, 2, "hello", True]
# my_tuple = [0, 1, 2, "hello", True]
# print(sys.getsizeof(my_list), "bytes")
# print(sys.getsizeof(my_tuple), "bytes")

# import timeit
# print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number =100000))
# print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number =100000))

#Dictionaries
#Dictionary : key-value pairs, unordered, Mutable
# mydict = {"name": "Max", "age": 28, "city": "New York"}
# mydict2 = dict(name="Mary", age=27, city="Boston")
# print(mydict2)
# value = mydict["lastname"]      #KeyError: 'lastname'
# print(value)
# mydict["email"] = "max@xyz.com"
# print(mydict)

# mydict["email"] = "coolmax@xyz.com"
# print(mydict)

# del mydict["name"]
# mydict.pop("age")
# mydict.popitem()
# print(mydict)

# if "name" in mydict:
#     print(mydict["name"])

# try:
#     print(mydict["Error"])
# except:
#     print("Error")

# for key in mydict.keys():
#     print(key)

# for value in mydict.values():
#     print(value)

# for key, value in mydict.items():
#     print(key, value)

# mydict = {"name": "Max", "age": 28, "city": "New York"}
# print(mydict)

# # mydict_copy = mydict.copy()
# mydict_copy = dict(mydict)


# mydict_copy["email"] = "max@xyz.com"

# print(mydict_copy)
# print(mydict)

# my_dict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
# my_dict_2 = dict(name = "Mary", age = 27, city = "Boston")

# my_dict.update(my_dict_2)
# print(my_dict)

# my_dict = {3: 9, 6:36, 9: 81}
# print(my_dict)

# # value = my_dict[0]      #KeyError: 0
# value = my_dict[3] 
# print(value)

# my_tuple = (8, 7)
# mydict = {my_tuple : 15}
# print(mydict)

# my_list = [8, 7]
# mydict = {my_list : 15}        #TypeError: unhashable type: 'list'
# print(mydict)

#Sets
#Set : unordered, mutable, no duplicates
# my_set = {1, 2, 3, 4, 5, 1, 2, 3}
# my_set = set("Dev DDDD")
# print(my_set)

#myset = {}
# myset = set()
# myset.add(1)
# myset.add(2)
# myset.add(3)
# myset.remove(3)
# # myset.remove(4)        #KeyError: 4
# myset.discard(4)
# print(myset.pop())
# print(myset)

# for i in myset:
#     print(i)

# if 4 in myset:
#     print("yes")
# else:
#     print("No")

# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}

# u = odds.union(evens)
# print(u)

# i = odds.intersection(evens)
# print(i)

# i = evens.intersection(primes)
# print(i)

# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3, 10, 11, 12}

# diff = setA.difference(setB)
# print(diff)

# diff = setA.symmetric_difference(setB)
# print(diff)

# diff = setB.symmetric_difference(setA)
# print(diff)

# setA.update(setB)
# print(setA)

# setA.intersection_update(setB)
# print(setA)

# setA.difference_update(setB)
# print(setA)

# setA.symmetric_difference_update(setB)
# print(setA)

# setA = {1, 2, 3, 4, 5, 6}
# setB = {1, 2, 3}
# setC = {7, 8}

# print(setA.issubset(setB))
# print(setB.issubset(setA))

# print(setA.issuperset(setB))
# print(setB.issuperset(setA))

# print(setA.isdisjoint(setB))
# print(setA.isdisjoint(setC))

# setA = {1, 2, 3, 4, 5, 6}
# setB = setA

# setB.add(7)

# print(setB)
# print(setA)

# setA = {1, 2, 3, 4, 5, 6}
# setB = setA.copy()

# setB.add(7)

# print(setB)
# print(setA)

# setA = {1, 2, 3, 4, 5, 6}
# setB = set(setA)

# setB.add(7)

# print(setB)
# print(setA)

# a = frozenset([1, 2, 3, 4])        
# a.add(2)        #AttributeError: 'frozenset' object has no attribute 'add'
# a.remove(2)        #AttributeError: 'frozenset' object has no attribute 'remove'
# print(a)

#Stings
#string - ordered, immutable, text representation
# my_string = 'Hello world!'
# my_string = """Hello \
# World"""
# my_string = 'Hello World'
# # char = my_string[0]
# # my_string[0] = 'h'        #TypeError: 'str' object does not support item assignment
# substring = my_string[::-1]
# print(substring)
# greeting = 'Hello'
# name = "Tom"
# sentence = greeting + " " + name
# print(sentence)
# greeting = "Hello"
# for i in greeting:
#     print(i)
# if 'ell' in greeting:
#     print('yes')
# else:
#     print("No")

# my_string = '    Hello World    '
# my_string = my_string.strip()
# print(my_string)

# my_string = 'Hello World'
# my_string = my_string.count('p')
# print(my_string)

# my_string = 'Hello World'
# print(my_string.replace('World', 'universe'))

# my_string = 'how are you doing'

# my_list = my_string.split()

# print(my_list)

# my_string = 'how,are,you,doing'
# my_list = my_string.split(',')
# print(my_list)
# new_string = ' '.join(my_list)
# print(new_string)

# my_list = ['a']*6

# print(my_list)

# my_string = ''
#Bad python code
# for i in my_list:
#     my_string += i
# print(my_string)
#Good python code
# my_string = ''.join(my_list)
# print(my_string)

# from timeit import default_timer as timer

# my_list = ['a']*1000000

# start = timer()
# my_string = ''
# #Bad python code
# for i in my_list:
#     my_string += i
# stop = timer()
# print(stop - start)
# #Good python code
# start = timer()
# my_string = ''.join(my_list)
# # print(my_string)
# stop = timer()
# print(stop - start)

#String formating
#%, format(), f-string
# var = "Tom"
# my_string = 'the variable is %s' % var
# print(my_string)

# var = 3
# my_string = 'the variable is %d' % var
# print(my_string)

# var = 3.5325425645
# my_string = 'the variable is %f' % var
# print(my_string)

# var = 3.5325425645
# my_string = 'the variable is %.2f' % var
# print(my_string)

# var = 3.53453532
# my_string = "the variable is {}".format(var)
# print(var)

# var = 3.53453532
# var2 = 6
# my_string = "the variable is {:.2f} and {}".format(var, var2)
# print(var)

# var = 3.235454645
# var2 = 6

# my_string = f"the variable is {var*2} and {var2}"
# print(my_string)

#Collections : 
#Collections : Counter, namedtuple, orderedDict, defaultdict, deque

# from collections import Counter

# a = "aaabbbbbbbcccccccc"
# my_counter = Counter(a)
# print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.most_common(1))
# print(my_counter.most_common(1)[0])
# print(my_counter.most_common(1)[0][0])
# print(list(my_counter.elements()))

# from collections import namedtuple
# point = namedtuple('point', 'x, y')
# pt = point(1, -4)
# print(pt)
# print(pt.x, pt.y)

# from collections import OrderedDict
# ordered_dict = OrderedDict()

# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4
# ordered_dict['a'] = 1

# print(ordered_dict)

# from collections import defaultdict

# d = defaultdict(int)

# d['a'] = 1
# d['b'] = 2

# print(d['c'])       #default value for an integer is 0.

# d = defaultdict(float)

# d['a'] = 1
# d['b'] = 2

# print(d['c'])       #default value for a float is 0.0.

# d = defaultdict(list)

# d['a'] = 1
# d['b'] = 2

# print(d['c'])       #It returns a default empty list.

# from collections import deque

# d = deque()

# d.append(1)
# d.append(2)
# d.appendleft(3)
# d.pop()
# print(d)
# d.popleft()
# print(d)
# d.clear()
# print(d)
# d.extend([4, 5, 6])
# print(d)
# d.extendleft([7, 8, 9])
# print(d)
# d.rotate(1)
# print(d)
# d.rotate(-1)
# print(d)

#itertools
#itertools: product, permutation, combinations, accumulate, groupby, and infinite iterators
# from itertools import product

# a = [1, 2]
# b = [3, 4]

# prod = product(a, b)
# print(list(prod))

# prod = product(a, b, repeat=2)
# print(list(prod))

# from itertools import permutations

# a = [1, 2, 3]
# perm  = permutations(a, 2)
# print(list(perm))

# from itertools import combinations, combinations_with_replacement

# a = [1, 2, 3, 4]
# comb = combinations(a, 2)       #Second argument as lengh is mandatory here.
# print(list(comb))
# comb_wr = combinations_with_replacement(a, 2)
# print(list(comb_wr))

# from itertools import accumulate
# import operator
# a = [1, 2, 3, 4]
# acc = accumulate(a, func=operator.mul)
# print(a)
# print(list(acc))

# from itertools import accumulate
# import operator
# a = [1, 2, 5, 3, 4]
# acc = accumulate(a, func=max)
# print(a)
# print(list(acc))

# from itertools import groupby

# a = [1, 2, 3, 4]

# def smaller_than3(x):
#     return x < 3
# group_obj = groupby(a, key=smaller_than3)
# print(group_obj)

# for key, value in group_obj:
#     print(key, list(value))

# from itertools import groupby

# a = [1, 2, 3, 4]

# group_obj = groupby(a, key=lambda x: x<3)
# print(group_obj)

# for key, value in group_obj:
#     print(key, list(value))

# from itertools import groupby

# person = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
#           {'name': 'Lisa', 'age': 27}, {'name': 'claire', 'age': 28}]

# group_obj = groupby(person, key=lambda x: x['age'])
# print(group_obj)

# for key, value in group_obj:
#     print(key, list(value))

# from itertools import count, cycle, repeat

# for i in count(10):       count(start, [step])
#     print(i)
#     if i == 15:
#         break

# from itertools import count, cycle, repeat

# a = [1, 2, 3]

# for i in cycle(a):        
#     print(i)

# from itertools import count, cycle, repeat

# a = [1, 2, 3]

# for i in repeat(1, 4):        #repeat(elem, n) 
#     print(i)

#lambda
#lambda arguments : expression

# add10 = lambda x: x + 10

# print(add10(5))

# def add10_func(x):
#     return x + 10

# mult = lambda x,y: x*y

# print(mult(2, 7))

# points2D = [(1, -2), (15, 1), (5, -1), (10, 4)]

# points2D_sorted = sorted(points2D)

# print(points2D)

# print(points2D_sorted)

# points2D = [(1, -2), (15, 1), (5, -1), (10, 4)]

# points2D_sorted = sorted(points2D, key = lambda x: x[1])

# print(points2D)

# print(points2D_sorted)

# points2D = [(1, -2), (15, 1), (5, -1), (10, 4)]

# def sort_by_y(x):
#     return x[1]

# points2D_sorted = sorted(points2D, key = lambda x: x[0] + x[1])

# print(points2D)

# print(points2D_sorted)

#map
#map(func, seq)
# a = [1, 2, 3, 4, 5]
# b = map(lambda x: x*2, a)
# print(list(b))

# c = [x*2 for x in a]
# print(c)

#filter
#filter(func, seq)
# a = [1, 2, 3, 4, 5, 6]

# b = filter(lambda x:x%2 == 0, a)

# print(list(b))

# c = [x for x in a if x%2 == 0]

# print(c)
#reduce
#reduce(func, seq)
# from functools import reduce
# a = [1, 2, 3, 4, 5, 6]

# product_a = reduce(lambda x,y: x*y, a)

# print(product_a)

