from tkinter import *
from tkinter import messagebox
from tkinter  import  simpledialog

window = Tk()

#CUSTOMING FRAME
window.configure(background='#011A27')
window.geometry("370x500")
window.title("TOTITO ;)")

turno = 0
nombre_jugador_1 = ""
nombre_jugador_2 = ""
lista_btns = []
tablero = []
turno_jugador = StringVar()


class Nodo:
    def __init__(self, dato):
        self.dato = dato 
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None
 
    def funcion_iniciar(self):
         for i in range(1,10):
            nuevo_nodo = Nodo({"posicion": i, "valor": "N"})
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    def asignar_X_O(self,get_posicion):
        actual = self.cabeza
        while actual:
            if actual.dato["posicion"] == get_posicion:
                print(actual.dato["posicion"]) 

            actual = actual.siguiente
        #print("None")
        #print(posicion)

    def retirar_primero(self):
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente

    def retirar_ultimo(self):
        if self.cabeza.siguiente == None:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = None

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato["valor"] , end=" -> ")
            actual = actual.siguiente
        print("None")


mi_lista = ListaSimple()
#mi_lista.funcion_iniciar()

#BUTTONS
btn0 = Button(window, width=8, height=4, bg="#011A27", command=lambda: mi_lista.asignar_X_O(1))
lista_btns.append(btn0)
btn0.place(x=50,y=50)
btn1 = Button(window, width=8, height=4, bg="#011A27", command=lambda: mi_lista.asignar_X_O(2))
lista_btns.append(btn1)
btn1.place(x=150,y=50)
btn2 = Button(window, width=8, height=4, bg="#011A27",command=lambda: mi_lista.asignar_X_O(3))
lista_btns.append(btn2)
btn2.place(x=250,y=50)
btn3 = Button(window, width=8, height=4, bg="#011A27", command=lambda: mi_lista.asignar_X_O(4))
lista_btns.append(btn3)
btn3.place(x=50,y=150)
btn4 = Button(window, width=8, height=4, bg="#011A27", command=lambda: mi_lista.asignar_X_O(5))
lista_btns.append(btn4)
btn4.place(x=150,y=150)
btn5 = Button(window, width=8, height=4, bg="#011A27", command=lambda: mi_lista.asignar_X_O(6))
lista_btns.append(btn5)
btn5.place(x=250,y=150)
btn6 = Button(window, width=8, height=4,bg="#011A27", command=lambda: mi_lista.asignar_X_O(7))
lista_btns.append(btn6)
btn6.place(x=50,y=250)
btn7 = Button(window, width=8, height=4, bg="#011A27", command=lambda: mi_lista.asignar_X_O(8))
lista_btns.append(btn7)
btn7.place(x=150,y=250)
btn8 = Button(window, width=8, height=4, bg="#011A27", command=lambda: mi_lista.asignar_X_O(9))
lista_btns.append(btn8)
btn8.place(x=250,y=250)

mostrar_turno_participante = Label(window, textvariable=turno_jugador).place(x=100, y=20)
iniciar_juego = Button(window, background="green", borderwidth=0,  fg="white", text="Iniciar juego", width=15, height=3,command=mi_lista.funcion_iniciar()).place(x=130, y=350)
'''mi_lista.agregar_elemento("Juan")
mi_lista.agregar_elemento("Maria")
mi_lista.agregar_elemento("Jose")
mi_lista.agregar_elemento("Douglas")
mi_lista.agregar_elemento("Pedro")'''
print("Muestra la lista inicialmente completa")
mi_lista.imprimir_lista()
#print("Retira el ultimo elemento de la lista")
#mi_lista.retirar_ultimo()
#mi_lista.imprimir_lista()
#print("Retira el primer elemento de la lista")
#mi_lista.retirar_primero()
#mi_lista.imprimir_lista()



#bloquear()

window.mainloop()