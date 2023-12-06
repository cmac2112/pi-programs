#simpler binary pi
from mpmath import mp

mp.dps = 100

def compute(n):
    pi_dig = mp.pi
    binary_dig = bin(int(pi_dig *(2 ** n)))[2:]
    return binary_dig.zfill(n)

result = compute(100)
print(result)
