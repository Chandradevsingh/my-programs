from array import array

arr = array('l')

# arr2 = array(arr.typecode)
for i in range(10):
    arr.append(i)

print(arr)

# array_list = arr2.tolist()
# array_list
array_string = arr.tobytes()
print(array_string)
array_again = arr.frombytes(array_string)
print(array_again)

