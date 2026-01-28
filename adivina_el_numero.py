import random #esto importa una herramienta para generar numeros aleatorios
#el programa elige un numero secreto entre 1y100

numero_secreto = random.randint(1,100)
intentos_restantes = 3
victoria=False
historial=[]
print("---Tienes 3 intentos para adivinar el numero (1-100)---")

#mientras tengamos intentos y no hayamos ganado...

while intentos_restantes > 0 and victoria== False:
   print(f"\nTe quedan {intentos_restantes} intentos.")
   intento=int(input("Cual es tu Numero?"))

   if intento ==numero_secreto:
     print("¡¡WOW!! Eres un ganador Adivinaste haz GANADO" ) 
     victoria=True
   elif intento < numero_secreto: 
     print("el numero secreto es mas grande")
     intentos_restantes =intentos_restantes-1
   else:
    print("el numero secreto es mas pequeño.")
    intentos_restantes = intentos_restantes-1

if victoria == False: 
  print(f"\nSe agotaron los intentos.el numero era {numero_secreto}.suerte la Proxima.")