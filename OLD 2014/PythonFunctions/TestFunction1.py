
# coding: utf-8

# In[1]:

def fib(n): # return Fibonacci series up to n
    "Return a list containing the Fibonacci series up to n"
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)    # see below
        a, b = b, a+b
    return result

