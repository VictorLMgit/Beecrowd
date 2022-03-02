from operator import truediv


CONSOANTES = ['b','c','d','f', 'g','h','j','k','l', 'm','n','p','q','r','s','t','v','x','z','y','w']
qtd = int(input())
for i in range(qtd):
    nome = input()
    dificil = False
    nomeModificado = nome.lower()
    nomeModificado = nomeModificado+'aaa'

    for i in range(len(nome)):
        if (nomeModificado[i] in CONSOANTES) and (nomeModificado[i+1] in CONSOANTES) and (nomeModificado[i+2] in CONSOANTES):
            print('{} nao eh facil'.format(nome))
            dificil = True
            break
    if(not dificil):
        print("{} eh facil".format(nome))
