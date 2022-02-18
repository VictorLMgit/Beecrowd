vet = []
n = int(input())
for i in range(n):
    nome = input()
    vet.append(nome)
conth=0
conts=0
for i in range(n):
    if vet[i][0] == '+':
        vet[i]=vet[i].replace('+ ','')

        conth+=1
    else:
        conts+=1
        vet[i]=vet[i].replace('- ','')

vet.sort()
for i in range(n):
    print(vet[i])
print("Se comportaram: {} | Nao se comportaram: {}".format(conth,conts))