'''
Programa que calcule el área y el perímetro de un rectángulo a partir de su base y su altura
Entradas:
  base: integer 
  altura: integer
Salidas: 
  perímetro: integer
  área: integer
Análisis: 
  se requiere calcular con las fórmulas para área y perímetro
'''
Base = input("Ingresa la base del rectángulo: ")
Base = int(Base)
Áltura = input("Ingresa la áltura del rectángulo: ")
Áltura = int(Áltura)
Área = Base * Áltura
Perímetro = (Base + Áltura) * 2
print ("El área del rectángulo es ", Área)
print ("El perímetro del rectángulo es: ", Perímetro)