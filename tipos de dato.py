import random

def ahorcado():
    palabras = ['manzana', 'pera', 'uva', 'naranja']
    palabra = random.choice(palabras)
    letras_adivinadas = []
    intentos = 6

    while intentos > 0:
        falladas = 0
        for letra in palabra:
            if letra in letras_adivinadas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
                falladas += 1
        if falladas == 0:
            print("\n¡Felicidades! Has ganado.")
            break

        print("\nIntentos restantes:", intentos)
        letra_usuario = input("Ingresa una letra: ").lower()

        if letra_usuario in palabra:
            letras_adivinadas.append(letra_usuario)
        else:
            intentos -= 1
            print("Letra incorrecta.")

    if intentos == 0:
        print("\n¡Has perdido! La palabra era:", palabra)

ahorcado()