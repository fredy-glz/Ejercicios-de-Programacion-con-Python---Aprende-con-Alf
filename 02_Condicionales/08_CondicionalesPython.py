# JOSE ALFREDO ROMERO GONZALEZ 
# 12/10/2020
puntuacion = float(input("Ingrese su puntuacion: "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
elif puntuacion == 0.4:
    nivel = "Aceptable"
elif puntuacion >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
    
if nivel == "":
    print("Puntuación no valida")
else:
    dinero = 2400 * puntuacion
    print("La cantidad de dinero que usted recibira es de: " + str(dinero) + "$")
    print("Su puntuación es: " + nivel)
    
# SOLUCION DE https://aprendeconalf.es/
bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación: "))
# Clasifiación por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
# Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))
