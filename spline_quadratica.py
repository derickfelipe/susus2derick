#coding: utf-8
from numpy import zeros
from numpy.linalg import solve
from copy import copy
from diferenças_divididas import difdiv, achar_intervalo

def interpolação(X, Y, Z):

	n = len(X) - 2 # numero de pontos -1 (n = n márcia)
	D, H = difdiv(X, Y)
	D += n * [0]
	A = zeros(((n + 1) + n, (n + 1) + n))   
	B = zeros(n + 1)
	C = B.copy()			#zeros(n-1)

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

	R = solve(A, D)

	j = 1
	for i in range(1, n + 1):
		B[i] = R[j]
		C[i] = R[j+1]
		j += 2

	print('Equação geral genérica: Si(z) = ai + bi(z - xi) + ci(z - xi)²')
	res = list()
	i = 0
	for z in Z:
		e = achar_intervalo(X, z)
		i += 1
		print('Equação geral para z{0:2d}: S({1:2f}) = {2:2f} + {3:2f}({1:2f} - {4:2f}) + {5:2f}({1:2f} - {4:2f})²'.format(i, z, Y[e], B[e], X[e], C[e]))
		r = Y[e] + B[e] * (z - X[e]) + (C[e] * (z - X[e])) ** 2
		print('Resultado: ', r)
		res.append(r)
	return res