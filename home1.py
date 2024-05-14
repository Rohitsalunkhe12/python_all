a=[1,2,1,2,33,44,55,3]
max_num=a[0]
for num in a:
    if num>max_num:
        max_num=num
print("the max no of list is:",max_num)



#find min number of above list

a=[1,2,1,2,33,44,55,3]
max_num=a[0]
for num in a:
    if num<max_num:
        max_num=num
print("the min no of list is:",max_num)


#2nd maximum number of list

a=[1,2,1,2,33,44,55,3]
a.sort(reverse=True)
print("2nd highest number:",a[1])


