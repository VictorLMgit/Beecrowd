
def isLeap(year):
    if((year%4 == 0 and not year%100==0) or year%400==0):
        return  True
    return False
def isHuluculu(year):
    if(year%15==0):
        return True
    return False
def isBulukulu(year):
    if(year%55 == 0 and isLeap(year)):
        return True
    return False
gapLine = False
while True:
  try:
    year = int(input())
    if(gapLine):
        print()
    gapLine = True
    if(isLeap(year)):
        print("This is leap year.")
    if(isHuluculu(year)):
        print("This is huluculu festival year.")
    if(isBulukulu(year)):
        print("This is bulukulu festival year.")
    if(not(isLeap(year) or isHuluculu(year) or isBulukulu(year))):
        print("This is an ordinary year.")
  except EOFError:
    break