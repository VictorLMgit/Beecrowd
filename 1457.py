def oraculo (num,k):
    i = 1
    total = num
    while not num-(i*k) <= 0:
        total = total * (num-(i*k))
        i = i+1
    return total
qtd = int(input())
for i in range(qtd):
    num = input()
    k = num.count('!')
    if num[:3].isnumeric():
        novo = num[:3]
        novo=int(novo)
        print(oraculo(novo,k))

    elif num[:2].isnumeric():
        novo = num[:2]
        novo=int(novo)
        print(oraculo(novo, k))

    elif num[:1].isnumeric():
        novo = num[:1]
        novo=int(novo)
        print(oraculo(novo, k))