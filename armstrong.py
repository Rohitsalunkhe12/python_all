n=1634
p = len(str(n))
n1=n
arm=0
#arm = 152
while n!=0:
    arm = arm+(n%10)**p
    n=n//10
if n1==arm:
    print(n1, "Is an Armstrong number")
else:
    print(n1,"is not a Armstrong number")
    
    
