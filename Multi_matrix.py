A=[[1,4],
   [2,5],
   [3,6],
   [4,7]]


B=[[1,2,3],
   [4,5,6]]

A_column=len(A[0])
A_row=len(A)
B_column=len(B[0])
B_row=len(B)

if A_column==B_row:
                                    #A  X B ---> C
                                    #4X2 2X3 --> 4X3
                                    #mXn nXk --> mXk
                                    #len(A)=m ,len(A[0])=n, len(B)=n , len(B[0])=k 
    C=[[]]*(len(A))
    c1=[]

    for k in range(0,B_column):
        c1.append(0)
    for m in range (0,A_row):
        C[m]=c1

#    for m in range (0,A_row):
#        for k in range(0,B_column):
#            C[m][k]=int(C[m][k])

'''
else:
    print("matrices requiremnts not matched for multiplication")
    
#C=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]   

for i in range(0,len(C)):
        for j in range(0,len(C[0])):
            for k in range(0,len(B)):
                C[i][j]+=A[i][k]*B[k][j]
for ro in C:
        print(ro)   
'''
user=C
#print(len(user[0])) ### for B if A*B
print(((user[0][0]))) ### for A if A*B
