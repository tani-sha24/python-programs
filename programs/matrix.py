A = [[1, 2], [3, 4]]
B = [[5, 6],[7, 8]]
addition = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("Matrix Addition:")
for row in addition:
    print(row)
multiplication = [[sum(A[i][k] * B[k][j] for k in range(len(B)))
                   for j in range(len(B[0]))] 
                   for i in range(len(A))]
print("Matrix Multiplication:")
for row in multiplication:
    print(row)
