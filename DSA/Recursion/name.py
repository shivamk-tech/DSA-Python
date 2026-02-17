
def PrintName(count,n):
    if(count > n):
        return
    print("Shivam")
    PrintName(count+1,n)

PrintName(1,5)