n=int(input())
n = n*n
if (n%2==0):
    print("{} casas brancas e {} casas pretas".format(int(n/2),int(n/2)))
else:
    print("{} casas brancas e {} casas pretas".format(int(n/2)+1,int(n/2)))