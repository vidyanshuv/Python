import array
import numpy as np

""" Creating array using array library """
my_array = array.array('i', [1, 2, 3, 4, 5])

my_arr = np.array([6, 7, 8, 9, 10])

""" Inserting elements into array """
my_array.insert(0, 11)  # using array.insert(index, value)
my_arr = np.insert(my_arr, 0, 12)  # using numpy.insert(array, object, value, axis = None)

""" Accessing Array Element """
for i in my_array:
    print(i)

for x in my_arr:
    print(x)

""" Deleting array element """
my_array.remove(11)

""" Searching for elements in Array """
my_array = array.array('i', [1, 2, 3, 4, 5, 6])

# Linear Search: iterating over array and compare each element with your searched value


def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


print(linearSearch(my_array, 6))