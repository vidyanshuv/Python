# A Simple function to print anything
def my_function():
    print("This is the function I created")

my_function()

# Function with arguments:
def addition_function(a, b):
    return a + b

print(f"Sum of both numbers is {addition_function(3, 4)}")


# Returning a collection from function
def list_return(a,b, c):
    add = a + b + c
    product = a * b * c
    return [add, product]

returned_val = list_return(2,3,4)
print(returned_val)

def dict_return(a, b, c):
    add = a + b + c
    product = a * b * c
    return {"Sum": add, "Product": product}

returned_val = dict_return(2,3,4)
print(returned_val)

""" Function with a docstring explaining the function & parameters"""
def docstring_function(a, b, c):
    """
    This function calculates & returns sum & product of 3 integers.
    :param a: First input
    :type a: int
    :param b: Second input
    :type b: int
    :param c: Third Input
    :type c: int
    :return: Returns the sum & product of all inputs
    """
    ds_add = a + b + c
    ds_product = a * b * c
    return ds_add, ds_product


addition, product = docstring_function(2,3,4)
print(f"Sum of inputs = {addition}, product of inputs = {product}")