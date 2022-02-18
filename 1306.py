i = 0
while True:
    r, n = list(map(int, input().split()))
    d = 1
    i = i + 1
    if r == 0 and n == 0:
        break
    if (n>=r):
        print("Case {}: 0".format(i))
    else:
        while (r - n > n):
            d = d + 1
            r = r-n
            if d > 26:
                print("Case {}: impossible".format(i))
                break
        if (d<=26):
            print("Case {}: {}".format(i,d))
