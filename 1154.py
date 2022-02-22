idades = []

idade = int(input())

while(idade>=0):
    idades.append(idade)
    idade = int(input())

qtdIdades = len(idades)
soma = 0
for i in range(qtdIdades):
    soma += idades[i]
print("{:.2f}".format(soma/qtdIdades))