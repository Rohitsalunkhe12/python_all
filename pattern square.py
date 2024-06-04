for row in range(1,6,1):
    for col in range(1,6,1):
        if (row==1 or row==5 or col==1 or col==3 or col==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
