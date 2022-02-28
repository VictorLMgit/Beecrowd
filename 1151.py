n = int(input())
a = 1
b = 1
c = 0
if (n == 1):
    print('0')
elif (n==2):
    print("0 1")
else:
    print("0 1 1", end=' ')
    for i in range(3,n-1 ):
        c = a + b
        a = b
        b = c
        print(c, end=' ')
    print(a+b)