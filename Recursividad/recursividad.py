#Convertir a Binario:
def convertiABinario(decimal):
    if(decimal ==0):
        return " "
    else:
        return convertiABinario(decimal//2) + str(decimal%2)

print(convertiABinario(9))

#Contar Dígitos:

#Raíz Cuadrada Entera:

#Convertir a Decimal desde Romano:

#Suma de Números Enteros:

