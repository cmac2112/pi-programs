#binary digits of pi
from mpmath import mp



def compute(n, userinp):
    mp.dps = userinp
    pi_digit = mp.pi
    binary_digit = bin(int(pi_digit * (2 ** n)))[2:] #[2: cuts off first two digits
    #because when printed this will show binary signature, we dont need that
    #int converts the operation into a digit
    #bin converts the digit into a binary string?
    return binary_digit.zfill(n)
#zfill pads zeros to the left of the number to ensure desired length is reached(n)\


def main():
    userinp = int(input("Enter desired decimal precision (Higher more precise, Longer load time)"))
    n = int(input("enter number of digits to compute:"))
    x = 1
    y = 2
    xy = bin(x + y)[2:] #messing with bin
    print(xy)
    
    result = compute(n, userinp)
    print(result)
    
main()
