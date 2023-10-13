class matrix:
	def __init__(self, width, height, fill): # fill is the character that is going to fill the matrix
		self.w = width # width
		self.h = height # height
		self.fill = fill
		self._mat = [] # i dunno why I named it _mat
		for i in range(self.h): # creating the matrix
			self._mat.append([])
			for j in range(self.w):
				self._mat[i].append(self.fill)
	def reset_mat(self): # resetting the matrix
		self._mat = []
		for i in range(self.h):
			self._mat.append([])
			for j in range(self.w):
				self._mat[i].append(self.fill)