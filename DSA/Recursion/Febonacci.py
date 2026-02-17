def Febonacci(n):
    if(n==1):
        return 1
    if(n==0):
        return 0
    return Febonacci(n-1) + Febonacci(n-2)

print(Febonacci(6))

