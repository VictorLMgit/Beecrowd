import math
def isPrime(x):
    for i in range (2, math.ceil(math.sqrt(x))):
        if (x%i==0):
            return False
    return True

def firstFactorPrime(x):
    for i in range (2, math.ceil(math.sqrt(x))):
        if (x%i==0 and isPrime(i)):
            return i
    return x



K, L = [int(x) for x in input().split(" ")]

while (not(K == 0 and L == 0)):
    if(K%2==0 and L>2):
        print("BAD 2")
        
    elif(K%2==0 and L<=2):
        print("GOOD")

    elif(L> firstFactorPrime(K)):
        print("BAD {}".format(firstFactorPrime(K)))
    else:
        print("GOOD")
    K, L = [int(x) for x in input().split(" ")]