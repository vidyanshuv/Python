import sys

def print_fn():
    print("Hello World")

def sum_fn(a, b):
    print(int(a) + int(b))

if __name__ == "__main__":
    args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2:] = function args : (*unpacked)
    globals()[args[1]](*args[2:])

# How to run from CLI
"""
python demo.py print_fn
python demo.py sum_fn 5 8

"""