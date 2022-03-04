vet = []
for i in range(10):
    n = int(input())
    if(n>0):
        vet.append(n)
    else:
        vet.append(1)
for i in range(10):
    print("X[{}] = {}".format(i,vet[i]))