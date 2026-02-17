# Normal Life
def OneToN(count,n):
    if(count > n):
        return 
    print(count)
    OneToN(count+1,n)

# OneToN(1,5)

# Mentos life (BackTracking)

def OneToNBackTracking(i,n):
    if(i < 1):
        return 
    OneToNBackTracking(i-1,n)
    print(i)

OneToNBackTracking(5,5)
    