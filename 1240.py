import math
qtd = int(input())
for i in range (qtd):
    A = []
    n, j = [int(x) for x in input().split(" ")]
    B = []
    cont = 0
    while n > 0:
        A.append(n % 10)
        n = n / 10
        n = math.floor(n)
    while j > 0:
        B.append(j % 10)
        j = j / 10
        j = math.floor(j)
    if len(B) > len(A):
        print("nao encaixa")
        cont += 1
    else:
        for i in range(len(B)):
            if B[i] != A[i]:
                print("nao encaixa")
                cont += 1
                break
    if cont == 0:
        print("encaixa")

