while True:
    qtd = int(input())
    if qtd == 0:
        break
    dp1, dp2 = list(map(int, input().split()))
    for i in range(qtd):

        x, y = list(map(int, input().split()))
        if x > dp1 and y > dp2:
            print("NE")
        if x < dp1 and y < dp2:
            print("SO")
        if x > dp1 and y < dp2:
            print("SE")
        if x < dp1 and y > dp2:
            print("NO")
        if x == dp1 or y == dp2:
            print('divisa')