

#new code

    
cols = 1
a= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for row in range(0,6,1):
    for col in range(0,6,1):
        if col <= 5 - cols:
            print(" ", end=" ")
        else:
            print(a[row], end=" ")
    cols += 1
    print()



 
