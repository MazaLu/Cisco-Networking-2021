numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numero = int(input ("Introduzca un numero entero:"))

while numero != 777:
    if numero > numeroSecreto:
        numeroSecreto = numero
    numero = int(input("¡Ja, ja! ¡Estás atrapado en mi ciclo!"))

print("¡Bien hecho, muggle! Eres libre ahora")