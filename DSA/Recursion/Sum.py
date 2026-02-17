# Using function with return
def Summation(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return n + Summation(n-1)

print(Summation(10))
print

# Using basic technique

def OneToNBackTracking(i,n):
    if(i < 1):
        print(n)
        return 
    OneToNBackTracking(i-1,n+i)

OneToNBackTracking(5,0)
    