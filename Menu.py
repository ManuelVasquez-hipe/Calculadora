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

        if opcion == "2":
            resultado = num1 - num2
            print(f"el resultado de la resta es {resultado}")
        
        elif opcion == "3":
            resultado = num1 * num2
            print(f"el resultado de la multiplicacion es {resultado}")
        elif opcion == "6":
           resultado = (num1 * num2) / 100
           print(f"el resultado del porcentaje es {resultado}")
calculadora()

#Mi parte