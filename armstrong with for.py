n=1634
n1=n
p=len(str(n))
arm = 0
for i in range(0,p,1):
    arm = arm+(n%10)**p
    n=n//10
if n1==arm:
    print(n1, "Is an Armstrong number")
else:
    print(n1,"is not a Armstrong number")
