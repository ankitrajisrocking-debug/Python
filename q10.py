import numpy as np

A = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
B = [ [9, 8, 7], [6, 5, 4], [3, 2, 1] ]


#				WITHOUT NUMPY

def add( A, B):
	return [ [A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range (len(A))]
	
def sub(A, B):
	return [[ A[i][j] - B[i][j] for j in range (len(A[0]))] for i in range (len(A))]
	
def mul( A, B):
	return [ [sum(A[i][k] * B[k][j] for k in range( len(B)))
				for j in range (len(B[0]))] for i in range(len(A)) ]
				
				
def transpose(A):
	return [[ A[i][j] for i in range(len(A)) ] for j in range( len(A[0])) ]
	

print("Without Numpy", )
print("Addition: ", add(A, B))
print("Sbtraction: ", sub( A, B) )
print("Multiplication: ", mul( A, B))
print("Transpose: ", transpose(A))



#				with numpy
X, Y = np.array(A), np.array(B)
print("\nWith Numpy: ")
print("Addition: \n", X + Y)
print("Subtraction:\n", X  - Y)     
print("Multiplication: \n", X @ Y)
print(" Transpose: \n", X.T) 
