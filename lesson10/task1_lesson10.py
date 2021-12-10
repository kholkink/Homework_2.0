class Matrix:
	def __init__(self, matrix):
		self.matrix = matrix
	def __add__(self, other):
		mass1 = []
		mass2 = []
		new_matrix = []
		for i in range(len(other.matrix)):
			for j in range(len(other.matrix[0])):
				mass1.append(other.matrix[i][j])
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[0])):
				mass2.append(self.matrix[i][j])
		for i in range(len(mass1)):
			mass1[i] += mass2[i]
		for i in range(len(self.matrix)):
			new_matrix_mass = []
			for j in range(len(self.matrix[0])):
				new_matrix_mass.append(mass1[i*len(self.matrix[0]) + j])
			new_matrix.append(new_matrix_mass)
		return Matrix(new_matrix)
	def __str__(self):
		str1 = ''
		str_big = ''
		for i in range(len(self.matrix)):
			str1 = ''.join(str(self.matrix[i])).strip('[]')
			str_big = str_big + str1 + '\n'
		return str_big.replace(',', '')
matrix1 = Matrix([[3,2,5], [1,6,11]])
matrix2 = Matrix([[4,1], [17,61], [32, 445]])
print(matrix1 + matrix2)
