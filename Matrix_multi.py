A=[[1,2,3],
   [4,5,6],
   [7,8,9]]

B=[[1,4,7],
   [2,5,8],
   [3,6,9]]

#3X3 3X2 --> 3*2

C= [[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(0,len(C)):
    for j in range(0,len(C[0])):
        for k in range(0,len(B)):
            C[i][j]+=A[i][k]*B[k][j]
for ro in C:
    print(ro)