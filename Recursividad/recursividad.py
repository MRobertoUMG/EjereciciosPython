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

#Suma de Números Enteros:
def SumaNumerosEnteros(numero):
    if numero == 1:
        return 1
    else:
        return numero + SumaNumerosEnteros(numero - 1)
    
print(SumaNumerosEnteros(4))

