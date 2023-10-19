"""
- Recursion occurs when a function calls itself.
- Every recursive function has an iterative solution, though it might be more complex to create.
- Recursion is not optimized as a function calling itself caused recursive actions to be stored into Stack memory,
  mostly has > O(n) time complexity i.e. O(n) + the time required to insert actions to stack memory.
- Not ideal to use when a simple iterative function can be created.
- More useful when dealing with Graphs & Nodes.
"""

# Q1> W.A.P. to calculate factorial of a number using recursion
"""
Approach to the problem:
Step 1: Identifying the recursive case - The flow
       n! = n * (n-1) * (n-2) *......* 2 * 1
    => n! = n * (n-1)!
Step 2 - Base Case: the stopping criterion:
    -> 0! = 1
    -> 1! = 1
Step 3 - Unintentional Case - The constraints:
    -> factorial(-1) = ??
    -> factorial(2.5) = ??
"""


def factorial(n):
    assert 0 < n == int(n), "Input must be a non-negative integer."
    if n in [0, 1]:
        return 1
    return n * factorial(n-1)


num = 4
print(f"Factorial of {num} is: {factorial(num)}")


# Q2> WAP to generate fibonacci numbers
"""
Approach to the problem:
Step 1: Identifying the recursive case - The flow
    0 1 1 2 3 5 8 13.....
    taking 5 = 3 + 2
    i.e.   f(n) = f(n-1) + f(n-2)
Step 2: Base Case - the Stopping criterion:
    -> n in [0, 1] : return n
    ->  

Step 3: Unintentional Case - The constraints:
    -> fibonacci(-1) = ??
    -> fibonacci(2.5) = ??
"""


def fibonacci(n):
    assert n >= 0 and n == int(n), "Input must be a non-negative integer."
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(f"Number of fibonacci elements are: {fibonacci(8)}")

# Q2> WAP to calculate sum of all elements of a list
"""
Approach to the problem:
Step 1: Identifying the recursive case - The flow
    let MyList = [1, 2, 3, 4, 5]
    sum(MyList) = 1 + sum([2, 3, 4, 5])
Step 2: Base Case - the Stopping criterion:
    -> -1 element in the list
Step 3: Unintentional Case - The constraints:
    - Check if input is a list or not
"""


def sum_list(p_list):
    if not isinstance(p_list, list):
        return -1
    elif len(p_list) == 1:
        return p_list[0]
    total = p_list[0] + sum_list(p_list[1:])
    return total


print(f"Sum of list is: {sum_list([1, 2, 3, 4, 5])}")

# Q3> WAP to calculate n^m with recursion
"""
Approach to the problem:
Step1: Recursive flow
    power(n, m) = n * power(n, m-1)
Step 2: Base condition
    Stop at m == 0 so that it doesn't go backwards and multiplies -ve numbers   
Step 3: Unintentional Case - The constraints:
    m should be integers and a +ve integer
"""


def power(n, m):
    assert 0 <= m == int(m)
    if m == 0:
        return 1
    return n * power(n, m-1)


print(f"power: {power(2, 3)}")

# Q4> WAP to calculate sum of positive integers of n+(n-2)+(n-4)+....until(n-x <= 0)
"""
Approach to the problem:
Step 1 - Recursive Flow:
    let n = 10
    sum = 10 + (10-2) + (10-4) + (10-6) + (10-8)
    sum(n) = n + sum(n-2) 
Step 2: Base Condition
    - Stop at n = 0
Step 3: Unintentional Case - The constraints:
    - N should be a positive integer
"""


def sum_positive(n):
    assert isinstance(n, int) and n == int(n), f"Input should be a positive integer instead provided: {n}"
    if n == 0:
        return 0
    elif n < 0:
        return 1
    return n + sum_positive(n-2)


print(f"Sum of positive numbers: {sum_positive(15)}")

