x=1
while x<=10:
    z=1
    while z<=x-1:
        print (" ",end="")
        z=z+1
    y=10-x+1
    while y>0:
        print("*", end="")
        y=y-1
    y=10-x
    while y>0:
        print("*", end="")
        y=y-1
    print()
    x=x+1