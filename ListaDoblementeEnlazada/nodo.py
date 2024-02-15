class Nodo:
    def __init__(self, data):
        self.name = data["name"]
        self.surname = data["surname"]
        self.id = data["id"]
        self.sig = None
        self.ant = None

class ListaDoble:
    #root
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertarAlPrincipio(self, data):
        nuevoNodo = Nodo(data)
        nuevoNodo.sig = self.cabeza
        self.cabeza = nuevoNodo

    def insertarAlFinal(self, data):
        nuevoNodo = Nodo(data)
        nuevoNodo.ant = self.cola
        self.cola = nuevoNodo
    
    def imprimir(self):
        #insertPrincipio
        actual = self.cabeza
        while actual:
            print(actual.name, end=" -> ")
            actual = actual.sig
        #insertFinal
        ultimo = self.cola
        while ultimo:
            print(ultimo.name, end=" -> ")
            ultimo = ultimo.ant
        print("None")


nodo = ListaDoble()
nodo.insertarAlPrincipio({"name":"Mario", "surname":"Rompich", "id":213})
nodo.insertarAlPrincipio({"name":"Jonh", "surname":"Jerez", "id":257})
nodo.insertarAlPrincipio({"name":"nathy", "surname":"Jerez", "id":257})

nodo.insertarAlFinal({"name":"Astrid", "surname":"Archila", "id":2045})
nodo.imprimir()



