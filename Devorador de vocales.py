﻿userWord = input("Ingrese una palabra:")
userWord = userWord.upper()
letra = letra + "Fizz"

for letra in userWord:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        print(letra)
