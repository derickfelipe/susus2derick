import copy
def interpol_Lagrange (X, Y, z):
	n = len(X)-1
	res = 0 
	for i in range(1,n+1):
		res += Y[i]*L(n,X,i,z)
	return res

def L(n,X,i,z):
	res = 1
	lista = list(range(1,n+1))
	lista.pop(i-1)
	for j in lista:
		res *= (z-X[j])/(X[i]-X[j])
	return res



