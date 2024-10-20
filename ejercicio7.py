'''
Realiza un programa que reciba una cantidad de minutos y muestre por pantalla
a cuantas horas y minutos corresponde
'''
min = input("Introduzca los minutos: ")
min = int(min)
h = min // 60 
m =  min % 60
print("Corresponde a:", h, "hora(s)", m, "minutos")