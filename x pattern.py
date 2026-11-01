
def row(a):
    l=1
    b=a
    for p in range(1,a+1):
        for j in range(1,a+1):
            if p==l and j==b:
                print("*",end="")
                l=l+1
                b=b-1
            elif p == j:
                print("*",end="")
            else:
                print(" ",end="")
        print( )
row(7)
            
                