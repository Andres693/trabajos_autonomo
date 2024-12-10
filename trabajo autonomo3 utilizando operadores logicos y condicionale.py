import random

def ahorcado():
    palabras = ["iguana", "aguila", "lechuza", "armadillo", "tigre"]
    palabra = random.choice(palabras)
    letras_adivinadas = []
    intentos = 6

    while intentos > 0:
        palabra_mostrar = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_mostrar += letra    
            else:
              palabra_mostrar += "_"
        print(palabra_mostrar)

        if "_" not in palabra_mostrar:
            print("¡Felicidades! Has adivinado la palabra:", palabra)
            break

        intento = input("ingresa una letra:").lower()

        if intento in letras_adivinadas:
            print("ya has ingresado esa letra.")
        elif intento in palabra:
            letras_adivinadas.append(intento)
            print("¡Correcto!")
        else:
            intentos -= 1
            print("Incorrecto. te quedan",intentos,"intentos.")

        if intentos == 0:
            print("¡Has perdido! la palabra era:", palabra)

ahorcado()
    

