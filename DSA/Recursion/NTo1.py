# Normal Life
def OneToN(n):
    if(n==0):
        return 
    print(n)
    OneToN(n-1)

# OneToN(5)

# Mentos life (BackTracking)

def OneToNBackTracking(i,n):
    if(i < 1):
        return 
    print(i)
    OneToNBackTracking(i-1,n)

OneToNBackTracking(5,5)
