#coding: utf-8

def interpolação(X, Y, Z):
	n = len(X)
	res = list()
	for z in Z:
		s = 0
		c = []
		for j in range(1 , n):
			if z <= X[j]:
				b = (Y[j] - Y[j-1]) / (X[j] - X[j-1])
				s = Y[j-1] + (b * (z - X[j-1]))
		res.append(s)
	return res
	