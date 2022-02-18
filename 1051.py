valor = float(input())
imposto = 0
if valor >= 0 and valor <= 2000.00:
    print("Isento")
elif valor > 2000 and valor <= 3000:    
    imposto =  (0.08) * (valor-2000)
elif valor > 3000 and valor <= 4500:
    parte1 = (0.08)*1000
    parte2 = (0.18)*(valor - 3000)
    imposto = parte1 + parte2
    
elif valor > 4500:
    parte1 = (0.08)*1000
    parte2 = (0.18)*1500
    parte3 = (0.28)*(valor - 4500)
    imposto = parte1 + parte2 + parte3

if(imposto>0):
    print("R$ {:.2f}".format(imposto))