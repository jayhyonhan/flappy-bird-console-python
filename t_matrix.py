class matrix:
	def __init__(self, width, height, fill):
		self.w = width
		self.h = height
		self.fill = fill
		self._mat = []
		for i in range(self.h):
			self._mat.append([])
			for j in range(self.w):
				self._mat[i].append(self.fill)
	def reset_mat(self):
		self._mat = []
		for i in range(self.h):
			self._mat.append([])
			for j in range(self.w):
				self._mat[i].append(self.fill)