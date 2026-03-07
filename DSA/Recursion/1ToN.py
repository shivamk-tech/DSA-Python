# Normal Life
def OneToN(count,n):
    if(count > n):
        return 
    print(count)
    OneToN(count+1,n)

# OneToN(1,5)

# Mentos life (BackTracking)

def OneToNBackTracking(i):
    if(i < 1):
        return 
    OneToNBackTracking(i-1)
    print(i)

OneToNBackTracking(5)
    