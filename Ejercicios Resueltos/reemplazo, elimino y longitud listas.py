listaSombrero = [1, 2, 3, 4, 5] # Esta es una lista existente de números ocultos en el sombrero.

listaReemplazo = int(input("Inserte numero entero de reemplazo: "))
listaSombrero[2] = listaReemplazo

print(listaSombrero[2])

del listaSombrero [-1]

print("Nueva longitud de lista:", len (listaSombrero))
print(listaSombrero)

#Escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (paso 1).
#Escribir una línea de código que elimine el último elemento de la lista (paso 2).
#Escribir una línea de código que imprima la longitud de la lista existente (paso 3).