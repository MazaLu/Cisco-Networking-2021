miLista = [10, 1, 8, 3, 5]

miLista [0], miLista [4] = miLista [4], miLista [0]
miLista [1], miLista [3] = miLista [3], miLista [1]

print(miLista) 

#with for

miLista = [10, 1, 8, 3, 5]
longitud = len(miLista)

for i in range (longitud // 2):
    miLista[i], miLista[longitud-i-1] = miLista[longitud-i-1], miLista[i]

print(miLista)

#Hemos asignado la variable longitud a la longitud de la lista actual (esto hace que nuestro código sea un poco más claro y más corto).
#Hemos lanzado el ciclo for para que se ejecute a través de su cuerpo longitud // 2 veces (esto funciona bien para listas con longitudes pares e impares, porque cuando la lista contiene un número impar de elementos, el del medio permanece intacto).
#Hemos intercambiado el elemento i (desde el principio de la lista) por el que tiene un índice igual a (longitud-i-1) (desde el final de la lista); en nuestro ejemplo, for i igual a 0 la (longitud-i-1) da 4; for i igual a 3, da 3: esto es exactamente lo que necesitábamos