import copy
def interpol_spline_linear(X, Y, z):
	n = len(X)
	s = 0
	c = []
	for j in range(1,n):
		if z <= X[j]:
			b = (Y[j]-Y[j-1]) / (X[j] - X[j-1])
			s = Y[j-1] + (b * (z - X[j-1]))
			print ('\nb', b)
	return s
	

