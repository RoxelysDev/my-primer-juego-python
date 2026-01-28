import random

def jugar_partida():
    numero_secreto = random.randint(1, 100)
    intentos_restantes = 5 # ¡Te doy 5 intentos para que sea más justo!
    historial = [] 

    print("\n--- ADIVINA EL NÚMERO (VERSIÓN INTELIGENTE) ---")

    while intentos_restantes > 0:
        print(f"\nIntentos anteriores: {historial}")
        # Usamos try-except para evitar errores si el usuario no introduce un número
        try:
            intento = int(input(f"Tienes {intentos_restantes} vidas. ¿Número?: "))
        except ValueError:
            print("¡Ojo! Debes introducir un número válido.")
            continue 

        if intento < 1 or intento > 100:
            print("Por favor, introduce un número entre 1 y 100.")
            continue

        # Verificamos si el número ya está en la lista
        if intento in historial:
            print("¡Ya probaste ese número! No seas despistado, intenta con otro.")
            continue 

        # Si es un número nuevo, lo guardamos
        historial.append(intento)

        if intento == numero_secreto:
            print("¡Ganaste! Eres una máquina.")
            return # Ganó, salimos de la función
        
        # Lógica de pistas
        if intento < numero_secreto:
            print("Pista: Es más grande.")
        else:
            print("Pista: El número secreto es menor.")
        
        intentos_restantes -=1 

    print(f"Game Over. El número era {numero_secreto}.")

# Bucle principal para jugar varias veces
while True:
    jugar_partida()
    if input("\n¿Otra partida? (s/n): ").lower() != "s":
        print("¡Gracias por jugar!")
        break


    