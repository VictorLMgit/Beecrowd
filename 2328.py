quantidadeDeRepeticoes = int(input())
cortes = []
estoque = 0
cortes = input().split(" ")

for i in range(quantidadeDeRepeticoes):
    
    estoque = estoque + int(cortes[i]) - 1

print(estoque)