from ctypes import *

c_file = "C:/Users/welcome/Desktop/Python Projects/mylib1.so"
c_fun = CDLL(c_file)

print("Enter two numbers")
a,b = int(input()), int(input())
result = c_fun.product(a,b)
print("The result is :", result)