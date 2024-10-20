'''
Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos
puntos en el plano. Calcula y muestra la distancia entre ellos.
'''
X1 = input("Introduzca la coordenada x1: ")
X1 = int(X1)
Y1 = input("Introduzca la coordenada y1: ")
Y1 = int(Y1)
X2 = input("Introduzca la coordenada x2: ")
X2 = int(X2)
Y2 = input("Introduzca la coordenada y2: ")
Y2 = int(Y2)

distancia = ((X2 - X1)**2 + (Y2 - Y1)**2)**(1/2)
print("La distancia es de: ",distancia)