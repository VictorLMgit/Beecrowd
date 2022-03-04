def media(notas):
    somaNotas = 0
    for i in notas:
        somaNotas = somaNotas + i
    return somaNotas/len(notas)
casosDeTeste = int(input())
for i in range(casosDeTeste):
    notasAlunos = input().split(" ")
    notasAlunos.pop(0)
    for i in range(len(notasAlunos)):
        notasAlunos[i] = int(notasAlunos[i])

    mediaTurma = media(notasAlunos)

    acimaDaMedia = 0
    for nota in notasAlunos:
        if(nota>mediaTurma):
            acimaDaMedia = acimaDaMedia + 1
    porcentagem = (acimaDaMedia*100/len(notasAlunos))
    print("{:.3f}%".format(porcentagem))
    