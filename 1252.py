def par(x):
    if (x%2 == 0):
        return True
    return False

qtd = int(input())
nums = []
for i in range(qtd):
    num = int(input())
    nums.append(num)
pares = []
impares = []

for i in nums:
    if (par(i)):
        pares.append(i)
    else:
        impares.append(i)



sortPares = sorted(pares)
sortImpares = sorted(impares, reverse=True)

for i in sortPares:
    print(i)
for i in sortImpares:
    print(i)
