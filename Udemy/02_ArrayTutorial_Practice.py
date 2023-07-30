from array import *

""" Time and space complexity for an array operation """
#   Operation                       Time Complexity             Space Complexity
#   Creating an empty array         O(1)                        O(1)
#   Creating array with n element   O(n)                        O(n)
#   Inserting 1 element             O(n)                        O(1)
#   Traverse an array               O(n)                        O(1)
#   Accessing a given cell          O(1)                        O(1)
#   Searching a given value         O(n)                        O(1)
#   Deleting a given value          O(n)                        O(1)

# 1. Create an array and traverse
my_array = array('i', [1, 2, 3, 4, 5, 6, 7, 8])
for i in my_array:  # O(n)
    # print(i)
    continue
# 2. Access individual elements through index
indzero = my_array[0]
indone = my_array[1]
indlast = my_array[-1]

# 3. Append values to array using append() method
my_array.append(9)

# 4. Insert values to array using insert() method
# 5. Extend python array using extend() method
# 6. Add items from list to array using fromlist() method
# 7. Remove any array element using remove() method
# 8. Remove last element using pop() method
# 9. Fetch index of any element using index() method
# 10. Reverse a python array using reverse() method
# 11. Get array buffer information through buffer_info() method
# 12. Check for number of occurrences of an element using count() method
# 13. Convert array to string using tostring() method
# 14. convert array to python list using tolist() method
# 15. Append a string to char array using fromstring() method
# 16. Slice elements from an array

