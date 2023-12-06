#non binary digits of pi

from mpmath import mp

mp.dps = 10000

def pi(n):
    pi_dig = mp.pi
    pi = int(pi_dig * (n ** 2))
    return pi

result = pi(1000000000000000)
print(result)
#got to be a better way, just ripped this from binary method

#mp.pi holds pi, could probably just print it itself

def compute(digits):
    pi = mp.pi

    return pi

pi = compute(10000)

print(pi)

#duh
