import random

numero_secreto=random.randint(1,100)

print("---¡Bienvenido al JUEGO DE ADIVINAR! ---")
intento=input("He pensado un numero del 1 al 100.¿ Cual crees que es")
intento=int (intento)
#Toma de decisiciones 

if intento ==numero_secreto:
   print("¡¡WOW!! Eres un ganador Adivinaste")
else:
   print("Casi.... pero NO. el Numero era el " + str(numero_secreto) + ".")