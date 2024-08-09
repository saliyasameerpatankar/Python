i=[1,3,5,3,7,1,9,8]
v=[]
for j in range(len(i)):
    if j!=0:
      j*=-1
      v.append(i[j])
v.append(i[0])
print(v)    
    
    

