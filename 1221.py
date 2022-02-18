import math
qtd = int(input())
while qtd > 0:
    num = float(input())
    i = 2
    isw = 0
    for i in range (2,round(math.sqrt(num))):
        if (num % i == 0):
            print("Not Prime")
            isw = 10
            break
    if isw == 0:
        print("Prime")
    qtd = qtd - 1