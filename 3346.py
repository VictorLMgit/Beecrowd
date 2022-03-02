a,b = [float(x) for x in input().split(" ")]
flutuacao = ((((1.0 + a/100.00) * (1.0 + b/100.00)) - 1.0) * 100.0)

print("{:.6f}".format(flutuacao))