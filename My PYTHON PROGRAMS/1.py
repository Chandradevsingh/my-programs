# print("Dev Chauhan")
# x = 5
# y = "Sally"
# print(type(x))
# print(type(y))

# x = str(3)
# y = int(3)
# z = float(3)

# print(type(x))
# print(type(y))
# print(type(z))

#String variables can be declared either by using single or double quotes.
#Variable Names are case-sensitive.

# a = 4
# A = "Sally"

#A will not overwrite a.

# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)


#Multi Words Variable Names
# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.

# a = "Hello World!"
#Get the characters from position 2 to position 5 (not included):
# print(a[2:5])
# print(a[:5])
# print(a[2:])
# print(a[-5:-2])
# print(a[1])
# print(len(a))

# for x in "banana":
#     print(x)

# txt = "the best things in life are free."
# print("free" in txt)
# print("expensive" not in txt)

# if "expensive" not in txt:
#     print(("No, expensive is not present."))

# a.upper()
# a.lower()
# a.strip()

# print(a.replace("H", "J"))

# print(a.split(","))

# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# age = 29

# txt = "My name is Dev, and I am {}"

# print(txt.format(age))

#Python Booleans - True or False

# print(bool("Hello"))
# print(bool(15))


#Pyramid, Turbogear, CherryPy etc.

# A python developer skillset includes :
#Core python skills:

    #Data Structures

    #OOP Concepts

    #Packages and Functions

    #Database and its connection

#Data Science skills:

    #Numpy

    #Pandas

    #Scipy

    #Matplotlib

    #Machine Learning algorithms

#Web Development Skills

    #Django Framework

    #Web Scraping

    #API Handling

    #Back-end connection
        
# id()
# type()
# int()
# float()
# str()
# hex()
# oct()
# complex()
# tuple()
# list()
# set()

#Defining Strings
#Strings are defined using opening and closing delimiters. These delimiters are pairs of single or double quotes.
# print('this is a string')
#Sample String
# test = 'random'
# how to get reverse string in python
# test[::-1]
# test.upper()
# test.lower()
# print(test.upper()), print(test.lower())
# test = 'Hello World!'
# sliced = test.split(" ")
# print('there is an \t space')
# print('there is an \n space')


#Lists
#In short, a list is a collection of arbitrary objects, somewhat akin to an array in many other programming languages but more flexible.

#Python lists are a type of sequence. Each object in a list is assigned an index as is typical for all sequences. These objects can be manipulated using its respective index.

#Defing lists
# a = [1,2,3]
#Features of Python Lists
#Lists are ordered.
#Lists elements can be manupulated using its index.
#Lists are mutable.
#Lists are dynamic.
#Lists can contain arbitrary objects.
#Lists can be nested to arbitrary depth.

#It's essentially what we call slicing by using strides.
# I'm taking strides. I'm not considering elements consecutively but I'm skipping certain elements in between.
#Lists Methods
# a = [1,2,3]
# a.append(4)
# a.append([5,6,7])
# a.extend([5,6,7])
# a.remove(5)
# a.pop()

#Tuple
#Tuples are another ordered collection of objects like lists, except for 2 properties where they differ
#Tuples are immutable.
#Tuples are defined using parenthesis instead of square brackets.

# d = dict([('banana','yellow'), ('apple','red'), ('grape','green')]) 
# del.d['banana']
# d.get('apple')
# d.items()
# d.values()
# d.keys()
# d.popitem()


#Dictionaries
#Dictionaries are another type of composite data types and also a collection of objects much like Tuples and Lists. Like Lists they are also mutable, Dynamic and can be nested. A key difference is that they are unordered. 
#Also items in dictionaries are paired using keys unlike Lists and Tuples where each item is assigned an index.

#Defining a Dictionary :

# A Dictionary is defined using curly braces. Each key-value pair is seperated using commas. The key and values are themselves seperated using a colon.

# d = {'banana':'yellow', 'apple':'red', 'grape':'green'}
# d = dict([('banana','yellow'), ('apple', 'red'), ('grape', 'green')])

#Python Type Hierarchy
#Below is the hierarchies for standard types that are built into python. It is important to note that with future versions these may change with new types being introduced or existing being modified.   
#None - Single object with this value accessed through built in name 'None'. Truth value is false.
#Ellipses - Single object with this value accessed through the built-in name Ellipses. It is used to indicate the presence of the '_' syntax in a slice. Its truth value is true. 
#Numbers - Immutable, Created through numeric literals and outputs of arithmatic expressions and arithmatic built in functions. Subtypes are :
    #Integers
        #plain Numbers - These represents numbers in the range -2147483648 through 2147483647.
        #Long Integers - These represent numbers in an unlimited range, subject to available (virtual) memory only.
    #Floating Point Numbers - These represent machine-level double precision floating point numbers.
    #Complex Numbers - These represent complex numbers as a pair of machine-level double precision floating point numbers.
#Sequences - These represent finite ordered sets indexed by natural numbers. Subtypes are based on mutability.
    #Immutable Sequences        
        #Strings - The items of a string are characters.
        #Unicode - The items of a unicode object are unicode characters.
        #Tuples - The items of a tuple are arbitrary objects.
    #Mutable Sequences
        #Lists - The items of a list are arbitrary python objects.
#Mappings - These represent finite sets of objects indexed by arbitrary index sets.
    #Dictionaries - These represent finite sets of objects indexed by nearly arbitrary values. These indexes must be of immutable data types.
#Callable types
    #User-defined functions
    #User-defined methods
    #Built-in functons
    #Bilt-in methods
    #Classes
    #Class Instances
#Modules - # Modules are large libraries or larger pieces of code or applications that contain various different methods and functions and objects and classes within them. and module are something that we'll think about little later.
#Files - files are datatypes that are called using the open() function.
#Internal Types 


#Arithmatic operators
#The floor division returns us the largest whole number that is lesser than the result of division.
#+, -, *, /, //, **, %

#Logical operators
#And, or, not
#Logical And: returns True if both operands are true. x and y
#Logical Or: returns True if either of operands are true. x or y
#Logical Not: True if operand is false.  not x

#Comparision operators
# == (Equal to)
# != (not equal to)
#greater than > : True if left operand is greater than the right.
#less than < : True if left operand is less than the right.
#greater than or equal to >= 
#less than or equal to <= 

#Assignment operators
#=
#+=
#-=
#*=
#/=
#%=
#//=
#**=

#Special Operators
#Identity operators : is and is not operators
#menbership operators: in and not in operators

#Math module
    #Constants of Math Module
        #Pi
        #Tau
        #Euler's Number
        #NaN (Not a number)
        #Infinity

#Pi - Pi(π) is the ratio of a circle's circumference(c) to its diameter(d):
        #   π = c/d
        #You can access pi as follows:
        #math.pi
        #math.pi always returns a float value.
        #Pi is a fractional number.
    #Tau - Tau (τ) is the ratio of a circle's circumference to its radius. The constant is equal to 2π or roughly 6.28. Like pi tau is an irrational number because it's just pi times 2. It also returns a float value.
    #You can use tau as follows:
    #math.tau

#Euler's Number - Euler's number(e) is a constant that is the base of natural logarithm. A mathmatical function that is commonly used to calculate rates of growth or decay. As with pi and tau Euler's number is an irrational number with infinite decimal places. The value of e is often approximated as 2.718. The function returns a float number.
# You can access the Euler's Number from the math module as follows :
# math.e


#Infinity - Infinity can't be defined by a number. Rather it's s mathmatical concept representing something that is never-ending or boundless. Infinity can go in either direction positive or negative.
    #You can represents infinity as follows:
    #math.inf
    #math.nan


    #type(math.inf)
    #type(math.nan)

#Arithmatic Functions
#Factorial
#Ceiling
#Floor
#Truncate Numbers
#Greatest Common Divisor
#Least Common Multiple

# math.factorial()
# math.ceil()
# math.floor()
# math.trunc()   #Rounds down and rounds up respectively.
# math.gcd()
# math.lcm()
# math.perm(n,k)
# math.comb(n,k)

#Power and Logrithmic Functions
#Power Function
#Exponential Function
#Logrithmic Functions
#Square Root Function

# math.pow()      #base python function pow()
# math.exp()      #e to the power n
#remaining = initial*math.exp(-0.693*time/half_life)
# math.log(8)
# math.log10(8)
# math.sqrt()

#Trignometric Functions
#sin
#Cosine
#Tan
#Arcsin
#Arccosine
#Arctan

# math.sin()
# math.cosine()
# math.tan()
# math.atan()
# math.acosine()
# math.asin()

#Hyperbolic Fuctions
#Hyperbolic sin
#Hyperbolic Cosine
#Hyperbolic Tan
#Hyperbolic Arcsin
#Hyperbolic Arccosine
#Hyperbolic Arctan

# math.sinh()
# math.cosineh()
# math.tanh()
# math.atanh()
# math.acosineh()
# math.asinh()

#Conditional Statements
#erroneous
#Iterable


# print("Hello world!")
# print("I will perform basic maths")
# a = 3
# b = 5
# c = a+b
# print("The result of addition of 3 and 5 is", c)
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)

