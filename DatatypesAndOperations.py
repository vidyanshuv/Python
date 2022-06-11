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
