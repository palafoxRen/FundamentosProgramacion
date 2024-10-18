'''
Un alumno desea saber cuál será su calificación final en la materia de
Algoritmos Dicha calificación se compone de los siguientes porcentajes:
• 55% del promedio de sus tres calificaciones parciales.
• 30% de la calificación del examen final.
• 15% de la calificación de un trabajo final.
'''
p1 = input("Nota del primer parcial: ")
p1 = int(p1)
p2 = input("Nota del segundo parcial: ")
p2 = int(p2)
p3 = input("Nota del tercer parcial: ")
p3 = int(p3)
np = ((p1 + p2 + p3) /3) / 100 * 55

nx = input("Nota del examen: ")
nx = int(nx)
nxf = nx / 100 * 30

nt = input("Nota del trabajo: ")
nt = int(nt)
ntf = nt / 100 * 15

cf = np + nxf + ntf

print("# Nota final de los tres parciales: ",np)
print("# Nota final del Examen: ",nxf)
print("# Nota final de los trabajos: ",ntf)
print("# NOTA FINAL: ",cf)