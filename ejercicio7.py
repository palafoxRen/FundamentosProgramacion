'''
Realiza un programa que reciba una cantidad de minutos y muestre por pantalla 
a cuantas horas y minutos corresponde.
'''
m = input("Introduzca los minutos: ")
m = int (m)
r = m // 60
s = m % 60
print("El resultado en horas es: ", r, s)