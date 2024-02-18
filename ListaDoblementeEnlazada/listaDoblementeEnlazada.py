class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.sig = None
        self.ant = None

class ListaDobleE:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tam = 0

    def vacia(self):
        return self.cabeza == None    

    def agregarFinal(self, nombre, apellido, carnet):
        if self.vacia():
            self.cabeza = self.cola = Nodo(nombre, apellido, carnet)
        else:
            tmp = self.cola
            self.cola = tmp.sig = Nodo(nombre, apellido, carnet)
            self.cola.ant = tmp
        self.tam += 1

    def agregarInicio(self, nombre, apellido, carnet):
        if self.vacia():
            self.cabeza = self.cola = Nodo(nombre, apellido, carnet)
        else:
            tmp = Nodo(nombre, apellido, carnet)
            tmp.sig = self.cabeza
            self.cabeza.ant = tmp
            self.cabeza = tmp
        self.tam += 1

    def print(self): 
        tmp = self.cabeza
        while tmp != None:
            print(f"(Nombre: {tmp.nombre}, Apellido: {tmp.apellido}, Carnet: {tmp.carnet})", end=" <-> ")
            tmp = tmp.sig

    def eliminarInicio(self): 
        if self.vacia():
            print("Lista vacía")
        elif self.cabeza.sig == None:
            self.cabeza = self.cola = None
            self.tam = 0
        else:
            self.cabeza = self.cabeza.sig
            self.cabeza.ant = None
            self.tam -= 1
    
    def eliminarFinal(self):
        if self.vacia():
            print("Lista vacía")
        elif self.cabeza.sig == None:
            self.cabeza = self.cola = None
            self.tam = 0
        else:
            self.cola = self.cola.ant
            self.cola.sig = None
            self.tam -= 1

try:
    if __name__ == "__main__":
        opc = 0
        nNodo = ListaDobleE()
        while opc != 6:
            print("\n------------------------------------------------",)
            print("**** Menu ****", end='\n')
            print("Elige una opción (Número) para ingresar hacer una acción")
            print("-------------------------------------------------")
            print("1 - Inserta un nuevo nodo al principio")
            print("2 - Inserta un nuevo nodo al final")
            print("3 - Eliminar el primer nodo")
            print("4 - Eliminar el último nodo")
            print("5 - Moestrar lista")
            print("6 - Salir")
            opc = int(input("Ingrese su opción(Número): "))

            if opc == 1:
                nombre = input("Ingresa el nombre: ")
                apellido = input("Ingresa el apellido: ")
                carnet = input("Ingresa el carnet: ")
                nNodo.agregarInicio  (nombre, apellido, carnet)
            elif opc == 2:
                nombre = input("Ingresa el nombre: ")
                apellido = input("Ingresa el apellido: ")
                carnet = input("Ingresa el carnet: ")
                nNodo.agregarFinal(nombre, apellido, carnet)
            elif opc == 3:
                nNodo.eliminarInicio()
            elif opc == 4:
                nNodo.eliminarFinal()
            elif opc == 5:
                print("\n------------------------------------------------",)
                nNodo.print()
            elif opc == 6:
                print("Sesión Terminada, si necesita ingresar nuevamente ejecute el codigo en CLI")
            else:
                print("opción inválida.")
except Exception as e:
    print(e)