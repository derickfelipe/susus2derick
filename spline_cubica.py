#coding: utf-8
from diferenças_divididas import difdiv, achar_intervalo
from numpy import zeros, linalg

def interpolação(X, Y, Z, tipo = 'natural'):

	n = len(X)		#n = número de pontos
	DD, H = difdiv(X, Y)
	D = zeros(n)
	M = zeros((n, n))
	B = zeros(n - 1)
	C = zeros(n - 1)
	M[0][0] = 1
	M[n-1][n-1] = 1

	for i in range(1, n - 1):
		M[i][i-1] = H[i-1]
		M[i][i] = 2 * H[i-1] * H[i]
		M[i][i+1] = H[i]

	E = [0] + [6 * (DD[i] - DD[i-1]) for i in range(1, n - 1)] + [0]
	if tipo == 'natural':
		E[0] = 0
		E[-1] = 0
	elif tipo == 'not-a-knot':
		E[0] = copy(E[1])
		E[-1] = copy(E[n])
	elif tipo == 'blablabla':
		E[0] = 'outroblalala'
		E[-1] = 'outroblalala2'

	S = linalg.solve(M, E)

	for i in range(n - 1):
		B[i] = (DD[i] - S[i+1] + 2 * S[i] * H[i]) / 2
		C[i] = S[i] / 2
		D[i] = (S[i+1] - S[i]) / (6 * H[i])

	print('Equação geral genérica: S(x) = ai + bi(x - xi) + ci(x - xi)² + di(x - xi)³')
	res = list()
	i = 0
	for z in Z:
		e = achar_intervalo(X, z)
		i += 1
		print('Equação geral para z{0:2d}: S({1:2f}) = {2:2f} + {3:2f}({1:2f} - {4:2f}) + {5:2f}({1:2f} - {4:2f})² + {6:2f}({1:2f} - {4:2f})³'.format(i, z, Y[e], B[e], X[e], C[e], E[e]))
		cont = z - X[e]
		r = Y[e] + B[e] * cont + C[e] * cont ** 2 + D[e] * cont ** 3 
		print('Resultado: ', r)
		res.append(r)
	return res