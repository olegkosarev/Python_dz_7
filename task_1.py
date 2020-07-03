from random import randint

class Matrix:
	def __init__(self, my_matrix):
		self.my_matrix = my_matrix


	def __str__(self):
		my_matrix = self.my_matrix
		str_matrix = ""

		for row in my_matrix:
			str_row = ""
			for num in row:
				str_row = f"{str_row} {num}"
			str_matrix = f"{str_matrix}\n{str_row}"

		return(str_matrix)


	def __add__(self, other):
		self_matrix = self.my_matrix
		other_matrix = other.my_matrix
		str_matrix = ""

		for row_index in range(0,len(self_matrix)):
			str_row = ""
			for num_index in range(0,len(self_matrix[0])):
				num_sum = (self_matrix[row_index])[num_index] + (other_matrix[row_index])[num_index]
				str_row = f"{str_row} {num_sum}"
			str_matrix = f"{str_matrix}\n{str_row}"

		return(str_matrix)

		
def my_matrix(row_cnt, num_cnt):
	return([[randint(1,100) for j in range(num_cnt)] for i in range(row_cnt)])

my_matrix1 = my_matrix(3,4)


m1 = Matrix(my_matrix1)
print(m1)

my_matrix2 = my_matrix(3,4)


m2 = Matrix(my_matrix2)
print(m2)

print(m1+m2)


