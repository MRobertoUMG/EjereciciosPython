#Convertir a Binario:

def convertiABinario(decimal):
    if(decimal ==0):
        return " "
    else:
        return convertiABinario(decimal//2) + str(decimal%2)

'''print(convertiABinario(9))'''
    
#-------------------------------------------------------------------------

#Contar Dígitos:
def contarDigitos(numero):
    if numero < 10:
        return 1
    else:
        return 1 + contarDigitos(numero // 10)

#print(contarDigitos(4822102))
#-------------------------------------------------------------------------
#Raíz Cuadrada Entera:
def raizCuadradaEntera(num, candidato=0):
  
    if candidato**2 >= num:
        return candidato -1
    else:
        return raizCuadradaEntera(num, candidato + 1)

#print(raizCuadradaEntera(37))

#-------------------------------------------------------------------------
#Convertir a Decimal desde Romano:
def romanoADecimal(romano):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(romano) == 0:
        return 0
    
    if len(romano) == 1:
        return romanos[romano]

    if romanos[romano[0]] < romanos[romano[1]]:
        return romanos[romano[1]] - romanos[romano[0]] + romanoADecimal(romano[2:])
    else:
        return romanos[romano[0]] + romanoADecimal(romano[1:])
#print(romanoADecimal("XV"))
#-------------------------------------------------------------------------
#Suma de Números Enteros:
def SumaNumerosEnteros(numero):
    if numero == 1: 
        return 1
    else:
        return numero + SumaNumerosEnteros(numero - 1)

#-------------------------------------------------------------------------
#print(SumaNumerosEnteros(4))

try:
    if __name__ == "__main__":
        opc = 0

        while opc != 6:
            print("\n------------------------------------------------",)
            print("**** Menu ****", end='\n')
            print("Elige una opción (Número) para ingresar hacer una acción")
            print("-------------------------------------------------")
            print("1 - Convertir a Binario")
            print("2 - Contar Dígitos")
            print("3 - Raíz Cuadrada Entera")
            print("4 - Convertir a Decimal desde Romano")
            print("5 - Suma de Números Enteros")
            print("6 - Salir")
            opc = int(input("Ingrese su opción(Número): "))

            if opc == 1:
                numero = int(input("Ingresa el número a convertir en binario: "))
                print("Número convertido en binario: " + convertiABinario(numero))
            elif opc == 2:
                numero = int(input("Ingresa el número que deseas que cuente el numero de dígitos:"))
                print(f"Número de dígitos: {contarDigitos(numero)}")
            elif opc == 3:
               numero = int(input("Ingresa el número que deseas que calcule la raiz cuadrada entera:"))
               print(f"Raiz cuadrada entera: {raizCuadradaEntera(numero)}")
            elif opc == 4:
                numero = str(input("Ingresa el número romano que deseas convertir a decimal:"))
                print(f"Número en decimal: {romanoADecimal(numero)}")
            elif opc == 5:
                numero = int(input("Ingresa el número entero que desees que se sume:"))
                print(f"La suma de los números enteros: {SumaNumerosEnteros(numero)}")
            elif opc == 6:
                print("Sesión Terminada, si necesita ingresar nuevamente ejecute el codigo en CLI")
            else:
                print("opción inválida.")
except Exception as e:
    print(e)

