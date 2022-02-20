import math
def volumeEsfera(raio):
    pi = 3.1415
    raioCubo = pow(raio,3)
    return (4/3)*pi*raioCubo


raioEsfera , gas = [int(x) for x in input().split(" ")]
qtdBaloes = int(gas/volumeEsfera(raioEsfera))

print(qtdBaloes)