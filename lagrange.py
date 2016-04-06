#coding: utf-8

def interpolação(X, Y, Z, G):
	n = len(X)-1
	res = list()
	for z in Z:
		R = 0 
		for i in range(1,n+1):
			R += Y[i] * L(n,X,i,z)
		res.append(R)
	return res

def L(n,X,i,z):
	res = 1
	lista = list(range(1, n + 1))
	lista.pop(i - 1)
	for j in lista:
		res *= (z - X[j]) / (X[i] - X[j])
	return res