# import random

# a = random.random()        #It genetates a random float between 0 and 1.
# a = random.uniform(1, 10)        #This will generate a random float between 1 and 10.
# a = random.randint(1, 10)        #This will generate a random integer between 1 and 10.
#                                  #It includes the upperbound.
# print(a)
# a = random.normalvariate(0, 1)
# print(a)

# mylist = list('ABCDEFGH')
# print(mylist)
# a = random.choice(mylist)
# a = random.sample(mylist, 3)
# a = random.choices(mylist, k=3)
# random.shuffle(mylist)
# print(mylist)

# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))

# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))

# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))

# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))
# import secrets

# a = secrets.randbelow(10)        #It has an exclusive upper bound. It will generate a true random 
#                                  #number between 0 and 10. And 10 is not included.
# print(a)
# a = secrets.randbits(4)        #It generates a random integer with k random bits.
# print(a)

# mylist = "ABCDEFGH"
# a = secrets.choice(mylist)        #It will pick a random choice from the given sequence.
#                                   #That is not reproducible.
# print(a)

import numpy as np

# a = np.random.rand(3)
# print(a)

# a = np.random.randint(0, 10, 3)
# print(a)

# a = np.random.randint(0, 10, (3, 4))        #For higher dimentions, use a tuple.
# print(a)

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr)

# np.random.shuffle(arr)
# print(arr)

# np.random.seed(1)
# print(np.random.rand(3,3))

# np.random.seed(1)
# print(np.random.rand(3,3))




