a=[6,7,2,5,1,8,4]
b=[]
min=a[0]
print(min)
for i in range(1,len(a)):
    while(a[i]):
     if a[i]<min:
        b.append(a[i])
    min=a[i]
print(b)
