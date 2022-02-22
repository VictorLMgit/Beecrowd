qtd = int(input())
for i in range (qtd):
    nome, forca = [x for x in input().split(" ")]

    if(nome == "Thor"):
        print("Y")
    else:
        print("N")
