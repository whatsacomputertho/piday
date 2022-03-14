from functools import reduce
import sympy as sp
try:
    from sympy.mpmath import mp
except ImportError:
    from mpmath import mp

def take_input():
    k = 0
    print("Input the number of digits of pi which you would like to output!")
    try:
        ip = str(input())
        if ip != "pie":
            k = int(ip)
        else:
            k = ip
    except Exception as e:
        print(str(e))
    return k

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def filter_input(input):
    if(input == "pie"):
        print("PIEEE")
        return 10
    else:
        if(sp.isprime(input)):
            print("That's a nice prime number ya got there.")
        else:
            print("You didn't give me a prime number.  I am unhappy.  Anyways, here are the factors of your input:")
            print(str(factors(input)))
        return input

mp.dps = filter_input(take_input())

print("And finally, here is the pi that you requested.")
print(mp.pi)