from random import randint

class Cell:
	def __init__(self, cell_num):
		self.cell_num = cell_num

	def __add__(self, other):
		self_cell_num = self.cell_num
		other_cell_num = other.cell_num
		return(self_cell_num+other_cell_num)

	def __sub__(self, other):
		self_cell_num = self.cell_num
		other_cell_num = other.cell_num
		return(self_cell_num-other_cell_num)

	def __mul__(self, other):
		self_cell_num = self.cell_num
		other_cell_num = other.cell_num
		return(self_cell_num*other_cell_num)

	def __truediv__(self, other):
		self_cell_num = self.cell_num
		other_cell_num = other.cell_num
		return(round(self_cell_num/other_cell_num))

	def make_order(self, row_len):
		cell_num = self.cell_num
		return([["*" for j in range(row_len)] for i in range(cell_num)])



c1 = Cell(33)
c2 = Cell(15)

print(c1+c2)

print(c1/c2)


