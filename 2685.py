while True:
  try:
    
    grau = int(input())
    if((grau>=0 and grau<90) or grau == 360):
        print('Bom Dia!!')
    if(grau>=90 and grau<180):
        print('Boa Tarde!!')
    if(grau>=180 and grau<270):
        print('Boa Noite!!')
    if(grau>=270 and grau<360):
        print('De Madrugada!!')

  except EOFError:
    break