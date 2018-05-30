# File: something.py
# Using name to run code 
from fib import fib

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

