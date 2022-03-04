def fibonacci(n):
    a = 1
    b = 1
    c = 0
    if (n == 1):
        return 1
    elif (n==2):
        return 1
    else:
        for i in range(3,n):
            c = a + b
            a = b
            b = c
        return(a+b)
while True:
    try:   
        n,m = input().split(" ")
        n = int(n)
        m = int(m)
        print(fibonacci(fibonacci(n))%m)
    except EOFError:
        break