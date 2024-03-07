numero_como_cadena = input("Escribe un número: ")
numero = float(numero_como_cadena)
if numero == 0:
    print("Neutro")
elif numero < 0:
    print("Negativo")
else:
    print("Positivo")



"""ejercicio2"""
a=int(input("digite un numero "))
b=int(input("digite un numero "))
c=int(input("digite un numero "))

menor =a
mayor =a
 
if b < menor:
    menor =b
    
elif b > mayor:
  mayor =b

if c < menor:
  menor =c

elif c > mayor:
  mayor =c

"""ejercicio3"""

  def encontrar_mayor_menor():
 num1 = float(input("Ingresa el primer número: "))
 num2 = float(input("Ingresa el segundo número: "))

 if num1 > num2:
   print("El primer número ({}) es mayor que el segundo número ({}).".format(num1, num2))
   print("El segundo número ({}) es menor que el primer número ({}).".format(num2, num1))
  elif num1 < num2:

   print("El segundo número ({}) es mayor que el primer número ({}).".format(num2, num1))
   print("El primer número ({}) es menor que el segundo número ({}).".format(num1, num2))
 else:
   print("Ambos números son iguales.")

 """ejerecicio4"""


def encontrar_mayor_menor_tres():

 num1 = int(input("Ingresa el primer número: "))

 num2 = int(input("Ingresa el segundo número: "))

 num3 = int(input("Ingresa el tercer número: "))

 mayor = max(num1, num2, num3)
 menor = min(num1, num2, num3)

  print("El número mayor es:", mayor)
  print("El número menor es:", menor)

"""ejerecicio5"""

def sumar_restar():

 a = float(input("Ingresa el primer número: "))
 b = float(input("Ingresa el segundo número: "))


 if a < b:

 resultado = a + b
 else:
 resultado = a - b
   print("El resultado es:", resultado)

"""ejerecicio6"""

def encontrar_cociente():

 a = float(input("Ingresa el primer número: "))

 b = float(input("Ingresa el segundo número: "))


 if b == 0:
   print("La división por cero no está definida.")

 else:

 cociente = a / b

  print("El cociente de {} y {} es: {}".format(a, b, cociente))

  """ejerecicio6"""

def sumar_o_multiplicar():

 a = float(input("Ingresa el primer número: "))
 b = float(input("Ingresa el segundo número: "))

 if a < 0 or b < 0:
  resultado = a + b
 else:
  resultado = a * b
  print("El resultado es:", resultado)

  """ejerecicio7"""

def verificar_bisiesto():
 year = int(input("Ingresa un año: "))

 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(year, "es un año bisiesto.")
 else:
  print(year, "no es un año bisiesto.")


# Función principal
def main():
 while True:
  print("\nMenú:")
  print("1. Verificar si un número es positivo o negativo")
  print("2. Encontrar el mayor y menor de dos números")
  print("3. Encontrar el mayor y menor de tres números")
  print("4. Sumar o restar dos números")
  print("5. Encontrar el cociente de dos números")
  print("6. Sumar o multiplicar dos números")
  print("7. Verificar si un año es bisiesto")
  print("8. Salir")


 opcion = int(input("Selecciona una opción: "))
if opcion == 1:

   verificar_positivo_negativo() 

 elif opcion == 2:
   encontrar_mayor_menor()
 elif opcion == 3:
   encontrar_mayor_menor_tres()
 elif opcion == 4:
   sumar_restar()
 elif opcion == 5:
 encontrar_cociente()
 elif opcion == 6:
  sumar_o_multiplicar()
 elif opcion == 7:
  verificar_bisiesto()
 elif opcion == 8:
  print("Saliendo del programa...")
  break
 else:
  print("Opción no válida. Por favor, selecciona una opción válida.")
if __name__ == "__main__":
  main()


"""ciclcos1"""


numero = float(input("Ingresa un número: "))

if numero > 0:

  print("El número ingresado es positivo.")
elif numero < 0:
  print("El número ingresado es negativo.")
else:

  print("El número ingresado es cero.")


"""ciclos2"""


num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if num1 > num2:

  print("El primer número ({}) es mayor que el segundo número ({}).".format(num1, num2))
  print("El segundo número ({}) es menor que el primer número ({}).".format(num2, num1))

elif num1 < num2:
  print("El segundo número ({}) es mayor que el primer número ({}).".format(num2, num1))
  print("El primer número ({}) es menor que el segundo número ({}).".format(num1, num2))

else:
  print("Ambos números son iguales.")


"""ciclos3"""

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)

 print("El número mayor es:", mayor)
 print("El número menor es:", menor)

"""ciclos4"""

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

if a < b:
 resultado = a + b
else:
 resultado = a - b
print("El resultado es:", resultado)

"""ciclo5"""

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

if b == 0:

 print("La división por cero no está definida.")
else:
 cociente = a / b

 print("El cociente de {} y {} es: {}".format(a, b, cociente))


"""ciclo6"""

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))


if a < 0 or b < 0:
 resultado = a + b
else:
 resultado = a * b
 print("El resultado es:", resultado)


"""ciclo7"""

year = int(input("Ingresa un año: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
 print(year, "es un año bisiesto.")
else:
 print(year, "no es un año bisiesto.")




