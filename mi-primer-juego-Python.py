import random

numero_secreto = random.randint(1, 100)
intentos_restantes = 3
historial = [] # Lista vacía para empezar

print("--- ADIVINA EL NÚMERO (VERSIÓN INTELIGENTE) ---")

while intentos_restantes > 0:
    print(f"\nIntentos anteriores: {historial}")
    # Usamos try-except para evitar errores si el usuario no introduce un número
    try:
        intento = int(input(f"Tienes {intentos_restantes} vidas. ¿Número?: "))
    except ValueError:
        print("¡Ojo! Debes introducir un número válido.")
        continue # Volvemos al inicio del bucle sin gastar un intento

    # Verificamos si el número ya está en la lista
    if intento in historial:
        print("¡Ya probaste ese número! No seas despistado, intenta con otro.")
        continue # Salta el resto del código y vuelve al inicio del bucle

    # Si es un número nuevo, lo guardamos
    historial.append(intento)

    if intento == numero_secreto:
        print("¡Ganaste! Eres una máquina. 🏆")
        break # Rompe el bucle inmediatamente
    
    # Lógica de pistas
    if intento < numero_secreto:
        print("Pista: Es más grande.")
    else:
        print("Pista: Es más pequeño.")
    
    intentos_restantes -= 1 # Forma corta de restar 1

if intentos_restantes == 0:
    print(f"Game Over. El número era {numero_secreto}.")


    