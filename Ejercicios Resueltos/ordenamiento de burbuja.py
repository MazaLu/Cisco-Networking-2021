miLista = [8, 10, 6, 2, 4] # lista para ordenar
swap = True # True para ingresar al bucle while

while swap:
    swap = False # no hay swaps hasta ahora:
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swap = True # ocurrió el intercambio:
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print(miLista)