while True:
  try:
    num = int(input())
    ones = 1
    contOnes = 1
    while(not(ones%num == 0)):
        ones = (ones*10) + 1
        contOnes+=1
    print(contOnes)
  except EOFError:
    break