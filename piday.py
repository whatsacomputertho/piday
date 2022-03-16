from functools import reduce
import sympy as sp
try:
    from sympy.mpmath import mp
except ImportError:
    from mpmath import mp

def take_input():
    k = 0
    print("Input the number of digits of pi which you would like to output, or input q to quit!")
    try:
        ip = str(input())
        if ip == "q":
            print("Aww, see ya later I guess :')")
            quit()
        if ip not in ["pie", "pi"]:
            try:
                k = int(ip)
            except Exception as e:
                print(e.__cause__)
                print("What the heck was that I told you to enter a number!!")
                print("Fine, I'm going to input 10 for you.  Hope you're happy...")
                return 10
        else:
            k = ip
    except Exception as e:
        print(str(e))
    return k

def factors(n):
    factors = list(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    factors.sort()
    return factors

def filter_input(input):
    if(input == "pie"):
        print("PIEEE")
        return 10
    elif(input == "pi"):
        with open("pi-with-digits.txt") as pi:
            pistr = ''
            for line in pi:
                pistr+=line
            print(pistr)
        return 3
    elif(input == 1855):
        print("Penn State was founded on February 22, 1855!")
        return input
    else:
        if(sp.isprime(input)):
            print("That's a nice prime number ya got there.")
        else:
            print("You didn't give me a prime number.  I am unhappy.  Anyways, here are the factors of your input:")
            print(str(factors(input)))
        return input

def main():
    while 1:
        mp.dps = filter_input(take_input())
        print("And finally, here is the pi that you requested.")
        print(mp.pi)

main()