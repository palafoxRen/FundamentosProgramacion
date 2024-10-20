'''
Pide al usuario dos números y muestra la "distancia" entre ellos (el valor
absoluto de su diferencia, de modo que el resultado sea siempre positivo).
'''
n1 = input("Escribe el primer valor: ")
n1 = int(n1)
n2 = input("Escribe el segundo valor: ")
n2 = int(n2)
d = abs(n1 - n2)
print("La distancia entre los dos numero es: ",d)