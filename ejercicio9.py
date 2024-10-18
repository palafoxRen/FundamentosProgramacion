'''
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
desea saber cuánto deberá pagar finalmente por su compra.
'''
pi = input("Introduzca el total de su compra: ")
pi = int(pi)
d = pi*15/100
pf = pi-d
print("El total de su compra con descuento es de: ", pf)