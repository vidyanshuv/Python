def divides(m,n):
    if m%n == 0:
        return True
    return False


def ifeven(x):
    return divides(x,2)


def ifodd(x):
    return (not divides(x, 2))


# Test the above methods
a = ifeven(11)
print(f"Is the number an even number?: {a}")

b = ifodd(11)
print(f"Is the number an Odd number?: {b}")


""" ----------- String --------- """
print("ABCD")
print(''' This is 'HOW' we "Can" use double and single quotes for a 
      'String'. "---------The Key is to use 3 single quotes and it is done" ''') # Single Quotes

print("This is how i am using \"double quotes inside double quotes\"") # Double Quote in double quotes


"""--------------Lists -----------"""
a = [1, 2, "Babu", "Shona"]
# Using index to retrieve values of a certain index returns the value in same DT that the value is of e.g. 
print(type(a[0])) # prints <class 'int'>
print(type(a[2])) # prints <class 'str'>

# While slicing a list always results a list e.g. 
print(a[:1])
print(type(a[:1]))

print(a[:4])
print(type(a[:4]))

b = a # Making b hold same values as a
print(b)
a[0] = 5 # Changes value of both a and b's 0th index 
print(a)
print(b)
# this change only happen in case of mutable data types, not for immutable data types i.e. string, integer

# Actually copying the list is done like this:
b = a[:len(a)]  # Returns a new list and assigns that into b ---- b = a[:] works too ----
print(b)
a[0] = 10
print(a)
print(b)
print(" Lists a and b have different values now")


