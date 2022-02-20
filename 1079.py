qtd = int(input())
for i in range (qtd):
    x, y, z = [float(x) for x in input().split(" ")]
    x = x*2
    y= y*3
    z = z*5
    numerador = x + y + z
    denominador = 10
    media_ponderada = numerador/denominador
    print("{:.1f}".format(media_ponderada))