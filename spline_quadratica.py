from numpy import zeros

def interpol_spline_quadratica(X, Y, z):

	D, H = difdiv(X, Y)
	n = len(X)
	A = zeros((n, n))
	B = zeros(n - 2)
	C = copy(B)

	B[0], B[1] = copy(D[0]), copy(D[0])
	C[0] = 0
	A[0][0] = 1git 

	for i in range(1, n):
		for j in range(n):
			None


def difdiv(X, Y):
	B, H = [], []
	for i in range(1, len(X)-1):
		h = X[i] - X[i-1]
		H.append(h)
		B.append((Y[i] - Y[i-1]) / h)

	return  B, H