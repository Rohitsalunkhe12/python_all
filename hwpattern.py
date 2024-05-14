a="CAB"
for row in range (5):
    for col in range (5):
        if col==0:
            if col==0:
                print(" ",end=" ")
            else:
                print(a[row-1],end= " ")
        elif col==1:
            if row==0:
                print(a[0],end= " ")
            else:
                print(" ",end= " ")
        else:
                print(" ",end= " ")
    print()
                
                    
           
