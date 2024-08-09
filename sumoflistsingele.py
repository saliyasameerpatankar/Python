a=int(input("enter n: "))
b=[int(i) for i in str(a)]
sum=0
for i in b:
    sum+=i
print(sum)
y=[int(i) for i in str(sum)]
if len(y)==1:
    print("yes sum is: ",sum)
else:
    print("no")
