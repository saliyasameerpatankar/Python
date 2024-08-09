n=int(input("enter n:"))
m=int(input("enter m:"))
d=max(n,m)
v=[]
for i in range(2,d):
    if (n%i==0)and(m%i==0):
         v.append(i)
print(v)
hcf=max(v)
lcm=(n*m)/hcf
gcd=(n*m)/lcm
print(lcm,gcd)
         
