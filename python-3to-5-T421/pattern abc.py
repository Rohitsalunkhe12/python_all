cols=1
for row in range(65,71,1):
    for col in range(65,71,1):
        if col<=70-cols:
            print(" ",end=" ")
        else:
            print(chr(row),end=" ")
    cols+=1
    print()

"""
step:-1 for outer loop
cols = 1
row=65
inner loop will run
step:-1 for inner loop
col=65
if 65<=70-1
if 65<=69:
   print a first space
step:-2 for inner loop
col=66
if 66<=69:
   true
   print second space
step:-3
col=67
if 67<=69:
  true
   print third space
step:-4
col=68
if 68<=69:
  true
  printing fourth space

step:-5
col=69
if 69<=69:
   true
   printing fifth space

step :6
col=70
if 70<=69:
   false
   print A

step:-7
col=71
inner loop will get false
value of cols get increase
cols+=1










   





  







"""
