lista = []
lista = input().split(" ")
A = int(lista[0])
for i in range(1,len(lista)):
    if(int(lista[i]) > 0 ):
        N = int(lista[i])
        break
soma = 0
while(N<=0):
    N = int(input())
for i in range(N):
    soma = soma + (A+i)
print (soma)