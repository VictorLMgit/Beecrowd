def perfeito(x):
    somaDivisoresDeX=0
    metade = int(x/2)
    for i in range(1,metade + 1):
        if(x%i == 0):
            somaDivisoresDeX = somaDivisoresDeX + i
    if (somaDivisoresDeX == x):
        return True
    return False

qtd = int(input())

for i in range (qtd):
    x = int(input())

    if(not x%2 == 0):
        print("{} nao eh perfeito".format(x))
    else:
        if(perfeito(x)):
            print("{} eh perfeito".format(x))
        else:
            print("{} nao eh perfeito".format(x))
    