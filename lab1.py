import random

def matrix_multiplication(A, B):
	rows_A = len(A)

	cols_A = len(A[0])

	rows_B = len(B)

	cols_B = len(B[0])

	if rows_A != cols_B:
		return("Неможливо помножити матриці", rows_A, cols_B)

	else:
		result = [[0 for row in range(cols_B)] for col in range(rows_A)]
		for s in range(rows_A):
			for j in range(cols_B):
				for k in range(cols_A):
					result[s][j] += A[s][k] * B[k][j]
		return result
		

def createMatrix(rowCount, colCount, dataList):
    mat = []
    if colCount > rowCount:
        for i in range(rowCount):
            rowList = []
            for j in range(colCount):
                rowList.append(dataList[rowCount * i + j])
            mat.append(rowList)
        return mat

    else:
        for i in range(colCount):
            rowList = []
            for j in range(rowCount):
                rowList.append(dataList[rowCount * i + j])
            mat.append(rowList)
        return mat


def list_input(a,b):
	alpha = []
	for i in range(a):
		for j in range(b):
			alpha.append(random.randint(0,9))
	return alpha



x = 3
y = 3

c = 3
d = 3

input1 = list_input(x, y)
input2 = list_input(c, d)

#print(input1, input2)

mat1 = createMatrix(x, y, input1)
mat2 = createMatrix(c, d, input2)

print(mat1,",", mat2)

plural = matrix_multiplication(mat1, mat2)
print(plural)