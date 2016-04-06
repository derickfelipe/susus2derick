#coding: utf-8
#from diferenças_divididas import difdiv
from numpy import zeros

def interpolação(X, Y, Z, G):
	res = []
	for z in Z:
		n = len(X) - 1
		B = difdiv(X, Y, G)
		R = B[n].copy()
		for i in range(n - 1,0 ,- 1 ):			
			R = R * (z - X[i]) + B[i]
		res.append(R)
	return res

def difdiv(X, Y, G):
	n = len(X) - 1
	B = zeros(n+1)
	for k in range(1,n):
		for i in range(G+1, k, -1):
			B[i] = (B[i]-B[i-1]) / (X[i] - X[i-k])
		# if k==1:
		# 	print ('\n B = ', B)
	return B