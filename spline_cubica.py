#coding: utf-8
from spline_quadratica import difdiv


def spline_cubica(X, Y, Z, tipo = 'natural'):

	n = len(X) - 1		#n = número de pontos
	DD, H = difdiv(X, Y)

	S = zeros(n, n)
	if tipo == 'not-a-knot':
		S[0] = 'blablabla'
	elif tipo == 'blablabla':
		S[0] = 'outroblalala'

	for i in range(n+1):
		preenche matriz S

	for i in range(n+1):
		B[i] = (DD[i] - S[i+1] + 2 * S[i] * H[i]) / 2
		C[i] = S[i] / 2
		D[i] = (S[i+1] - S[i]) / (6 * H[i])

	print('Equação geral genérica: P(x) = ai + bi(x - xi) + ci(x - xi)² + di(x - xi)³')
	i = 0
	for z in Z:
		e = achar_intervalo(X, z)
		i += 1
		print('Equação geral para z{0:2d}: P({1:2f}) = {2:2f} + {3:2f}({4:2f} - {5:2f}) + {6:2f}({7:2f} - {8:2f})² + {9:2f}({10:2f} - {11:2f})²'.format(i, z, Y[e], B[e], z, X[e], C[e], z, X[e], D[e], z, X[e]))
		cont = z - X[e]
		r = Y[e] + B[e] * cont + C[e] * cont ** 2 + D[e] * cont ** 3 
		print('Resultado: ', r)

def achar_intervalo(X, z):
	for i in range(0, len(X)):
		print(i, X[i])
		if z > X[i]:
			return i
