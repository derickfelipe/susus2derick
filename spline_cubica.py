#coding: utf-8
from spline_quadratica import difdiv, achar_intervalo
from numpy import zeros, linalg

def spline_cubica(X, Y, Z, tipo = 'natural'):

	n = len(X)		#n = número de pontos
	DD, H = difdiv(X, Y)
	D = zeros(n)

	if tipo == 'natural':
		#E[0] = 0
		#E[n+1] = 0
		pass
	elif tipo == 'not-a-knot':
		E[0] = 'blablabla'
	elif tipo == 'blablabla':
		E[0] = 'outroblalala'

	M = zeros((n, n))
	B = zeros(n-1)
	C = zeros(n-1)
	M[0][0] = 1
	M[n-1][n-1] = 1

	for i in range(1, n-1):
		M[i][i-1] = H[i-1]
		M[i][i] = 2 * H[i-1] * H[i]
		M[i][i+1] = H[i]

	


	E = [0] + [6 * (DD[i] - DD[i-1]) for i in range(1, n-1)] + [0]
	
	print(M)
	print(E)
	S = linalg.solve(M, E)



	for i in range(n-1):
		B[i] = (DD[i] - S[i+1] + 2 * S[i] * H[i]) / 2
		C[i] = S[i] / 2
		D[i] = (S[i+1] - S[i]) / (6 * H[i])

	print('de 0 a n-1:')
	print('A: ', Y[:-1])	# Y = A[i]
	print('B: ', B)
	print('C: ', C)
	print('D: ', D)
	print('S: ', S)

	#print('Equação geral genérica: P(x) = ai + bi(x - xi) + ci(x - xi)² + di(x - xi)³')
	i = 0
	for z in Z:
		e = achar_intervalo(X, z)
		i += 1
		#print('Equação geral para z{0:2d}: P({1:2f}) = {2:2f} + {3:2f}({4:2f} - {5:2f}) + {6:2f}({7:2f} - {8:2f})² + {9:2f}({10:2f} - {11:2f})²'.format(i, z, Y[e], B[e], z, X[e], C[e], z, X[e], D[e], z, X[e]))
		cont = z - X[e]
		r = Y[e] + B[e] * cont + C[e] * cont ** 2 + D[e] * cont ** 3 
		print('Resultado: ', r)

# X = [3, 4.5, 7, 9]
# Y = [2.5, 1, 2.5, 0.5]
# z = [3.5]

# spline_cubica(X, Y, z)