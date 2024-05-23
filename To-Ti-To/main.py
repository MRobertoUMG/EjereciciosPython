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
puntuacion_jugador_1 = StringVar()
pts_1 = 0
puntuacion_jugador_2 = StringVar()
pts_2 = 0
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

        for i in range(0,9):
            nuevo_nodo = Nodo({"posicion": i, "valor": "Null", "puntos": 0 })
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        #ListaSimple.desbloquear(self)

        mi_lista.imprimir_lista()

        global nombre_jugador_1, nombre_jugador_2
        #nombre_jugador_1 = simpledialog.askstring("Jugador", "Nombre del juador: ")
        nombre_jugador_1 = "Robert"
        nombre_jugador_2 = "Máquina"

        turno_jugador.set("TURNO: " + nombre_jugador_1)     
      
    def asignar_X_O(self,get_posicion, puntos):
        global turno, nombre_jugador_1,nombre_jugador_2, pts_1,pts_2

        actual1 = self.cabeza
        
        while actual1:
           
            if actual1.dato["posicion"] == get_posicion and turno == 0:
                
                actual1.dato["valor"] = "X"
                actual1.dato["puntos"] = puntos
                pts_1 = int(pts_1) + int(puntos)

                lista_btns[get_posicion].config(bg="white")
                lista_btns[get_posicion].config(text="X")
                #lista_btns[get_posicion].config(state="disable")
                turno = 1
                turno_jugador.set("Turno: " + nombre_jugador_2)
                puntuacion_jugador_1.set(nombre_jugador_1)
                #print(actual1.dato["posicion"])        
            elif actual1.dato["posicion"] == get_posicion and turno == 1:
                actual1.dato["valor"] = "O"
                actual1.dato["puntos"] = puntos
                pts_2 = int(pts_2) + int(puntos)

                lista_btns[get_posicion].config(bg="lightblue")
                lista_btns[get_posicion].config(text="O")
                #lista_btns[get_posicion].config(state="disable")
                turno = 0
                turno_jugador.set("Turno: " + nombre_jugador_1)
                #print(actual1.dato["posicion"])

            lista_btns[get_posicion].config(state="disable")
            actual1 = actual1.siguiente

            puntuacion_jugador_1.set(nombre_jugador_1 + ": " + str(pts_1)  + " pts" )
            puntuacion_jugador_2.set(nombre_jugador_2 + ": " + str(pts_2) + " pts" )

        mi_lista.validar_ganador()
            
        actual = self.cabeza
        while actual:
            puntos = str(actual.dato["puntos"])
            print(actual.dato["valor"] + "|" + puntos, end=" -> ")
            actual = actual.siguiente
        print("None")
            
        #print("None")
        #print(posicion  mcvv)
      

    def validar_ganador(self):
        nodo = self.cabeza
        tablero = []
        while nodo:
            tablero.append(nodo.dato)
            nodo = nodo.siguiente
        print("---------------------------------------------------")
        #print(tablero[0]["posicion"])

        if(tablero[0]["valor"] == "X" and tablero[1]["valor"] == "X" and tablero[2]["valor"] == "X") or (tablero[3]["valor"] == "X" and tablero[4]["valor"] == "X" and tablero[5]["valor"] == "X") or (tablero[6]["valor"] == "X" and tablero[7]["valor"] == "X" and tablero[8]["valor"] == "X"):
            messagebox.showinfo("Felicidades!", "GANADOR: " + nombre_jugador_1)
            mi_lista.bloquear()
        elif(tablero[0]["valor"] == "X" and tablero[3]["valor"] == "X" and tablero[6]["valor"] == "X") or (tablero[1]["valor"] == "X" and tablero[4]["valor"] == "X" and tablero[7]["valor"] == "X") or (tablero[2]["valor"] == "X" and tablero[5]["valor"] == "X" and tablero[8]["valor"] == "X"):
            messagebox.showinfo("Felicidades!", "GANADOR: " + nombre_jugador_1)
            mi_lista.bloquear()
        elif(tablero[0]["valor"] == "X" and tablero[4]["valor"] == "X" and tablero[8]["valor"] == "X") or (tablero[2]["valor"] == "X" and tablero[4]["valor"] == "X" and tablero[6]["valor"] == "X"):
            messagebox.showinfo("Felicidades!", "GANADOR: " + nombre_jugador_1)
            mi_lista.bloquear()
        if(tablero[0]["valor"] == "O" and tablero[1]["valor"] == "O" and tablero[2]["valor"] == "O") or (tablero[3]["valor"] == "O" and tablero[4]["valor"] == "O" and tablero[5]["valor"] == "O") or (tablero[6]["valor"] == "O" and tablero[7]["valor"] == "O" and tablero[8]["valor"] == "O"):
            messagebox.showinfo("Felicidades!", "GANADOR: " + nombre_jugador_2)
            mi_lista.bloquear()
        elif(tablero[0]["valor"] == "O" and tablero[3]["valor"] == "O" and tablero[6]["valor"] == "O") or (tablero[1]["valor"] == "O" and tablero[4]["valor"] == "O" and tablero[7]["valor"] == "O") or (tablero[2]["valor"] == "O" and tablero[5]["valor"] == "O" and tablero[8]["valor"] == "O"):
            messagebox.showinfo("Felicidades!", "GANADOR: " + nombre_jugador_2)
            mi_lista.bloquear()
        elif(tablero[0]["valor"] == "O" and tablero[4]["valor"] == "O" and tablero[8]["valor"] == "O") or (tablero[2]["valor"] == "O" and tablero[4]["valor"] == "O" and tablero[6]["valor"] == "O"):
            messagebox.showinfo("Felicidades!", "GANADOR: " + nombre_jugador_2)
            mi_lista.bloquear()
       
        print("---------------------------------------------------")
    def desbloquear(self):
        for i in range(0,9):
            lista_btns[i].config(state="normal")

    def bloquear(self):
        for i in range(0,9):
            lista_btns[i].config(state="disable")

    '''def retirar_primero(self):
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente´'''

    '''def retirar_ultimo(self):
        if self.cabeza.siguiente == None:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = None'''
    
    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato["valor"] , end=" -> ")
            actual = actual.siguiente
        print("None")


mi_lista = ListaSimple()


#BUTTONS
btn0 = Button(window, width=8, height=4, bg="#011A27", command=lambda: mi_lista.asignar_X_O(0,3))
lista_btns.append(btn0)
btn0.place(x=50,y=50)
btn1 = Button(window, width=8, height=4, bg="#011A27", command=lambda: mi_lista.asignar_X_O(1,2))
lista_btns.append(btn1)
btn1.place(x=150,y=50)
btn2 = Button(window, width=8, height=4, bg="#011A27",command=lambda: mi_lista.asignar_X_O(2,3))
lista_btns.append(btn2)
btn2.place(x=250,y=50)
btn3 = Button(window, width=8, height=4, bg="#011A27", command=lambda: mi_lista.asignar_X_O(3,2))
lista_btns.append(btn3)
btn3.place(x=50,y=150)
btn4 = Button(window, width=8, height=4, bg="#011A27", command=lambda: mi_lista.asignar_X_O(4,4))
lista_btns.append(btn4)
btn4.place(x=150,y=150)
btn5 = Button(window, width=8, height=4, bg="#011A27", command=lambda: mi_lista.asignar_X_O(5,2))
lista_btns.append(btn5)
btn5.place(x=250,y=150)
btn6 = Button(window, width=8, height=4,bg="#011A27", command=lambda: mi_lista.asignar_X_O(6,3))
lista_btns.append(btn6)
btn6.place(x=50,y=250)
btn7 = Button(window, width=8, height=4, bg="#011A27", command=lambda: mi_lista.asignar_X_O(7,2))
lista_btns.append(btn7)
btn7.place(x=150,y=250)
btn8 = Button(window, width=8, height=4, bg="#011A27", command=lambda: mi_lista.asignar_X_O(8, 3))
lista_btns.append(btn8)
btn8.place(x=250,y=250)


mostrar_turno_participante = Label(window, textvariable=turno_jugador).place(x=150, y=15)
participante_pts_1= Label(window, textvariable=puntuacion_jugador_1).place(x=100, y=350)
participante_pts_1= Label(window, textvariable=puntuacion_jugador_2).place(x=200, y=350)


iniciar_juego = Button(window, background="green", borderwidth=0,  fg="white", text="Iniciar juego", width=15, height=3,command=lambda: mi_lista.funcion_iniciar()).place(x=130, y=400)
#
#mi_lista.bloquear()
#print("Retira el ultimo elemento de la lista")
#mi_lista.retirar_ultimo()
#mi_lista.imprimir_lista()
#print("Retira el primer elemento de la lista")
#mi_lista.retirar_primero()
#mi_lista.imprimir_lista()

window.mainloop()