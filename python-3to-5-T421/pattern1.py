row=1
while row<=4:
    col=1
    while col<=row:
        if row==3 and col==1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
        col+=1
    row+=1
    print()
