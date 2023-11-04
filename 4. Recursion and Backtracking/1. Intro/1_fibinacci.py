"""
f(n) = f(n-1) + f(n-2)

Recursion has 3 things - 
1. Base case  Eg - n == 0
2. Working towards the base case  Eg - how to deal with n
3. Recursive call  Eg - f(n-1), f(n-2), f(n+1) etc
"""


def fibo(n):

    # Base case if n == 1 or 2
    if n == 1 or n == 2:
        return 1
    
    return fibo(n-1) + fibo(n-2)

print(fibo(90))