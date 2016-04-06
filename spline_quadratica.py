from numpy import zeros, linalg
from copy import copy

def interpol_spline_quadratica(X, Y, Z):

	n = len(X) - 2 # numero de pontos -1 (n = n márcia)
	D, H = difdiv(X, Y)
	D += (n) * [0]
	# os indices deve estar todos errados. modificamos n = len(X) - 1 para n = len(X) - 2 
	A = zeros((n+1 + n, n+1 + n))   
	B = zeros(n + 1)
	C = copy(B)			#zeros(n-1)

	B[0], B[1] = copy(D[0]), copy(D[0])
	C[0] = 0
	A[0][0] = 1

	j = 1
	for i in range(1, n+1):	
		A[i][j] = 1
		A[i][j+1] = H[i] 
		j += 2

	A[n+1][0] = B[0]
	A[n+1][1] = 1			# conferir este valor

	j = 2
	for i in range(1, n):
		A[i + n+1][j-1] = -1
		A[i + n+1][j] = -2 * H[i]
		A[i + n+1][j+1] = 1
		j += 2

	R = linalg.solve(A, D)

	j = 1
	for i in range(1, n+1):
		B[i] = R[j]
		C[i] = R[j+1]
		j += 2

	#print(Y, B, C)
	print('Equação geral genérica: P(x) = ai + bi(x - xi) + ci(x - xi)²')
	i = 0
	for z in Z:
		e = achar_intervalo(X, z)
		i += 1
		print('Equação geral para z{0:2d}: P({1:2f}) = {2:2f} + {3:2f}({4:2f} - {5:2f}) + {6:2f}({7:2f} - {8:2f})²'.format(i, z, Y[e], B[e], z, X[e], C[e], z, X[e]))
		r = Y[e] + B[e] * (z - X[e]) + (C[e] * (z - X[e])) ** 2
		print('Resultado: ', r)

def achar_intervalo(X, z):
	for i in range(0, len(X)):
		if z > X[i]:
			return i

	return None

def difdiv(X, Y):
	D, H = [], []
	for i in range(1, len(X)):
		h = X[i] - X[i-1]
		H.append(h)
		D.append((Y[i] - Y[i-1]) / h)
		#print(D)

	return  D, H

# X = [3, 4.5, 7, 9]
# Y = [2.5, 1, 2.5, 0.5]
# z = [3.5]

# interpol_spline_quadratica(X, Y, z)