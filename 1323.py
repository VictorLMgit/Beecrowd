import math

n = int(input())
while n > 0:

    fayman = 0
    for i in range (n):
        if n - i >= 0:
            fayman = fayman + math.pow(n-i,2)
        else:
            break
    print(round(fayman))

    n = int(input())