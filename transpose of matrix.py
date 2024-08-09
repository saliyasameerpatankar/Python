a= [[1,2], [3,4]]
res= [[0,0], [0,0]]
for i in range(len(a)):
    for j in range (len (res)):
        res[i][j] =a[j][i]
print ("Transpose matrix", res)
