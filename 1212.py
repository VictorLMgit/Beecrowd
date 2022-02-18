import math
def Plus1 (somou):
    return not somou
n = j = 1
while n != 0 or j != 0:
    k = []
    n , j = [int(x) for x in input().split(" ")]
    m = n
    o = j
    l = []
    somou = False
    count = 0

    while m > 0:
        k.append(m%10)
        m = m/10
        m = math.floor(m)
    while o > 0:
        l.append(o%10)
        o = o/10
        o = math.floor(o)

    if len(k) > len(l):
        for i in range (len(k) - len(l)):
            l.append(0)
    elif len(k) < len(l):
        for i in range (len(l) - len(k)):
            k.append(0)

    for i in range(len(k)):
        if Plus1(somou) == False:
            if k[i] + l[i] + 1 >= 10:
               count += 1
            else:
               somou = Plus1(somou)
        elif k[i] + l[i] >= 10:
            count += 1
            somou = Plus1(somou)
    if n != 0 or j!= 0:
        if count == 0:
            print("No carry operation.")
        elif count == 1:
            print("1 carry operation.")
        else:
            print("{} carry operations.".format(count))