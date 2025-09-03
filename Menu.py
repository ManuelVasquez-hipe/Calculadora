import math

def calculadora():
    while True:
        print("\n ==== calculadora de python")
        print("Suma")
        print("Resta")
        print("Multiplicación")
        print("Division")
        print("raiz cuadrada")
        print("porcentaje")
        opcion = input("elige una opcion Suma 1, Resta 2, multiplicacion 3, Divicion 4, raiz cuadrada 5, porcentaje 6, salir 7: ")

        if opcion == "7":
            print("saliendo de la calculadora adios")
            break
        try:
            if opcion in ["1", "2", "3", "4", "6"]:
                num1 = float(input("ingresa el primer numero: "))
                num2 = float(input("ingresa el segundo numero: "))
            elif opcion == "5":
                num1 = float(input("ingresa el numero para sacar la raiz cuadrada: "))
                num2 = None
            else:
                print("opcion invalida")
                continue
        except ValueError:
            print("error, ingresa un numero valido")
            continue

        if opcion == "1":
            resultado = num1 + num2
            print(f"el resultado de la suma es {resultado}")
        
        elif opcion == "4":
            if num2 == 0:
                print("error, no se puede dividir entre cero")
                continue
            resultado = num1 / num2
            print(f"el resultado de la division es {resultado}")
        elif opcion == "5":
            if num1 < 0:
                print("error, no se puede sacar la raiz cuadrada de un numero negativo")
                continue
            resultado = math.sqrt(num1)
            print(f"el resultado de la raiz cuadrada es {resultado}")
calculadora()
