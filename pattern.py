row=1
while row<=5:
    col=1
    while col<=4:
        if col==1 or col==4 or row==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    print()
    row+=1
        
