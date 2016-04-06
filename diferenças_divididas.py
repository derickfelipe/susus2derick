#coding: utf-8

def difdiv(X, Y):
	D, H = [], []
	for i in range(1, len(X)):
		h = X[i] - X[i-1]
		H.append(h)
		D.append((Y[i] - Y[i-1]) / h)
	return  D, H

def achar_intervalo(X, z):
	for i in range(0, len(X)):
		if z > X[i]:
			return i