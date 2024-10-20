'''
Dado un número de dos cifras, diseñe un algoritmo que permita obtener el
número invertido
'''
n1 = int(input("Introduce un número de dos cifras: "))
decenas = n1/10
unidades = n1%10
inv = int(unidades*10+decenas) 
print("El numero invertido es: ",inv)