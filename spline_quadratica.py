from numpy import zeros

def interpol_spline_quadratica(X, Y, z):

	D, H = difdiv(X, Y)
	n = len(X)
	A = zeros((n, n))
	B = zeros(n - 2)
	C = copy(B)

	B[0], B[1] = copy(D[0]), copy(D[0])


	for i in range():
		for j in range():
			None


def difdiv(X, Y):
	B, H = [], []
	for i in range(1, len(X)-1):
		h = X[i] - X[i-1]
		H.append(h)
		B.append((Y[i] - Y[i-1]) / h)

	return  B, H