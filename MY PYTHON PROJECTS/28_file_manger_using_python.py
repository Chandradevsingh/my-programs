import os

path = input('Enter your path : ')

files = os.listdir(path)

for i in files:
    filename, extension = os.path.splitext(i)
    print(filename, extension)
    extension_1 = extension[1:]

    if os.path.exists()