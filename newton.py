import copy
def interpol_Newton (X, B, z, G):
	n = len(X)-1
	
	R = copy.copy(B[n])
	for i in range(n-1,0,-1):			
		R = R*(z-X[i]) + B[i]
	return R


		

