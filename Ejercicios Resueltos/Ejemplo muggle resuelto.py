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

numero = 0

while numero != numeroSecreto:
    numero = int(input("Estimado Muggle, introduzca un numero entero: "))
    if numero != numeroSecreto:
        print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
print("¡Bien hecho, muggle! Eres libre ahora")