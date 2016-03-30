import math
import newton
import lagrange
import spline_linear
#import matplotlib.pyplot as pyplot
#import numpy as np

arquivo = input ('digite o caminho do arquivo: ')
arquivo = open(arquivo, 'r')
datafile = arquivo.readlines()


datafile[0] = datafile[0].rstrip()
aux = datafile[0].split(" ")
X = [-1]+aux	

datafile[1] = datafile[1].rstrip()
aux = datafile[1].split(" ")
Y = [-1]+aux

datafile[2] = datafile[2].rstrip()
aux = datafile[2].split(" ")
Z = [-1]+aux

G = int(datafile[3])

X = [float(x) for x in X]
Y = [float(x) for x in Y]
Z = [float(x) for x in Z]


#usar para criar mais z's
#Z = [-1.0]+[x for x in np.arange(1.0,8.0,0.1)]


def diferenças_divididas(B,G):
	n = len(X)-1
	for k in range(1,n):
		for i in range(G+1, k, -1):
			B[i] = (B[i]-B[i-1]) / (X[i] - X[i-k])
	return B



if(G > len(X)-1):
	print("Atencao! O grau precisa ser menor do que o numero de pontos informados.")


else:
	listaResultados = []
	numPts = G+1
	numPtsCeil = math.ceil(numPts/2)
	numPtsFloor = math.floor(numPts/2)
	ini = 1
	fim = len(X)-1
	for z in Z[1:]:
		Xescolhidos = [-1.0]
		Yescolhidos = [-1.0]	

		if (z > X[len(X)-1] or z < X[1]):
			print ("%f nao esta entre os valores de x, portanto interpolacao nao pode ser feita" % (z))
			Z.remove(z)
			
		
		else:
			for i in range(1,len(X)):
				if (z > X[i] and z < X[i+1]):
					if (i > numPtsFloor and (len(X)-1 >= i+numPtsCeil-1)):
						ini = i-numPtsFloor
						fim = i+numPtsCeil-1
					else:
						if(i <= numPtsFloor):
							ini = 1
							fim = i + numPtsCeil + numPtsFloor - i
						else:	
							ini = i - numPtsFloor - (numPtsCeil-(len(X) - i))
							fim = len(X)-1
					
			
			Xescolhidos = Xescolhidos+X[ini:fim+1]
			Yescolhidos = Yescolhidos+Y[ini:fim+1]
					
			#B = diferenças_divididas(Yescolhidos,G)
			#result = newton.interpol_Newton (Xescolhidos, B, z, G)
			#result = lagrange.interpol_Lagrange(X, Y, z)
			result = spline_linear.interpol_spline_linear(X, Y, z)
			listaResultados.append(result)
			print ("f(",round(z,4),") = ",result)
	
	
	'''pyplot.plot(Z[1:],listaResultados)
	pyplot.ylabel('f(x)')
	pyplot.xlabel('x')
	pyplot.show()'''
	
