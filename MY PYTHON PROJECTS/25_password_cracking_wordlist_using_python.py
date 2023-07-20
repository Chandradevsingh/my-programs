from string import *
from itertools import product




# value = ascii_letters        #It returns only lowercase and uppercase alphabets.
# print(ascii_letters)
# value = punctuation
# print(value)
# value = digits
# print(value)

value = ascii_letters + digits + punctuation
print(value)
for i in range(1, 3):
    for j in product(value, repeat=i):
        word = "".join(j)
        p = open('password.txt', 'a')
        p.write(word)
        p.write('\n')