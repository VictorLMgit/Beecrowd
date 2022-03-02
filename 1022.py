import math

def divisores(x):
    divisores = []
    if x < 0:
        x = x*(-1)

    metadeDeX = math.ceil(x/2)
    
    for i in range(1,metadeDeX + 1):
        if (x%i == 0):
            divisores.append(i)
    divisores.append(x)
    return divisores

def maiorDivisorComum(x, y):
    divisoresDeX = divisores(x)
    divisoresDeY = divisores(y)
    maiorDivisorComum = 1
    for i in divisoresDeX:
        if ((i in divisoresDeY)):
            maiorDivisorComum = i
    
    return maiorDivisorComum

qtd = int(input())
for i in range(qtd): 
    N1, B1, D1, OP, N2, B2, D2 = [(x) for x in input().split(" ")]

    N1 = int(N1)
    D1 = int(D1)
    N2 = int(N2)
    D2 = int(D2)

    numResult = 0
    denResult = 0

    if(OP=="+"):
        numResult = N1*D2 + N2*D1
        denResult = D1*D2
    elif(OP == "*"):
        numResult = N1*N2
        denResult = D1*D2
    elif(OP == '/'):
        numResult = N1*D2
        denResult = N2*D1
    elif(OP == "-"):
        numResult = N1*D2 - N2*D1
        denResult = D1*D2

    print("{}/{}".format(numResult,denResult),end=' = ')
    mdc = maiorDivisorComum(numResult,denResult)
    while (mdc != 1):
        mdc = maiorDivisorComum(numResult,denResult) 
        numResult = numResult/mdc
        denResult = denResult/mdc
    print("{}/{}".format(int(numResult),int(denResult)))
    