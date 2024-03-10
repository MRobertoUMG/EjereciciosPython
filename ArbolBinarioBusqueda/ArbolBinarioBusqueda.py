class NodoArbol:
    def _init_(self, valor):
        self.izq = None
        self.der = None
        self.valor = valor 
    
class ArbolBinario:
    def _init_(self):
        self.raiz = None
    
    def insertar(self, valor):
        self.raiz = self.insertar2(valor, self.raiz)
        
    def insertar2(self, valor, nodo):
        if nodo is None:
            return NodoArbol(valor)
        if valor < nodo.valor:
            nodo.izq = self.insertar2(valor, nodo.izq)
        elif valor > nodo.valor:
            nodo.der = self.insertar2(valor, nodo.der)
        return nodo
    
    def mostrar(self, nodo):
        if nodo is not None:
            if nodo.izq is not None:
                print(nodo.valor, "-> ", nodo.izq.valor)
            if nodo.der is not None:
                print(nodo.valor, "-> ", nodo.der.valor)
                
            self.mostrar(nodo.izq)
            self.mostrar(nodo.der)

arbol = ArbolBinario()

arbol.mostrar(arbol.raiz)

nombre_archivo = input("Introduce el nombre del archivo: ")
with open(nombre_archivo, "r") as archivo:
    for linea in archivo:
        arbol.insertar(int(linea.strip())) 

arbol.mostrar(arbol.raiz)