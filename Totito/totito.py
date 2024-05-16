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

#BLOQUEAMOS LAS CASILLAS HASTA QUE DEN CLICK EN EL BOTON INICIAR
def bloquear():
    for i in range(0,9):
        lista_btns[i].config(state="disable")

#DESBLOQUEAMOS LAS CASILLAS DESPUES DE PRECIONAR EL BOTON INICIAR
def funcion_iniciar():
    for i in range(0,9):
        lista_btns[i].config(state="normal")
        lista_btns[i].config(bg="white")
        lista_btns[i].config(text="")
        tablero[i] = "N"
    global nombre_jugador_1, nombre_jugador_2
    #PARAMS TITLE// TEXT
    nombre_jugador_1 = simpledialog.askstring("Jugador", "Escriba el nombre del juador 1: ")
    nombre_jugador_2 = simpledialog.askstring("Jugador", "Escriba el nombre del juador 2: ")
    turno_jugador.set("Turno: " + nombre_jugador_1)
    

def cambiar(numero):
    global turno, nombre_jugador_1,nombre_jugador_2
    if tablero[numero] == "N" and turno == 0:
        lista_btns[numero].config(text="X")
        lista_btns[numero].config(bg="gray")
        tablero[numero] = "X"
        turno = 1
        turno_jugador.set("Turno: " + nombre_jugador_2)
    elif tablero[numero] == "N" and turno == 1:
        lista_btns[numero].config(text="O")
        lista_btns[numero].config(bg="lightblue")
        tablero[numero] = "O"
        turno = 0
        turno_jugador.set("Turno: " + nombre_jugador_1)
    lista_btns[numero].config(state="disable")
    verificar()
    #print(numero)

def verificar():
    if (tablero[0] == "X" and tablero[1] == "X" and tablero[2] == "X") or (tablero[3] == "X" and tablero[4] == "X" and tablero[5] == "X") or (tablero[6] == "X" and tablero[7] == "X" and tablero[8] == "X"):
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste jugador " + nombre_jugador_1)

    elif (tablero[0] == "X" and tablero[3] == "X" and tablero[6] == "X") or (tablero[1] == "X" and tablero[4] == "X" and tablero[7] == "X") or (tablero[2] == "X" and tablero[5] == "X" and tablero[8] == "X"):
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste jugador " + nombre_jugador_1)

    elif (tablero[0] == "X" and tablero[4] == "X" and tablero[8] == "X") or (tablero[2] == "X" and tablero[4] == "X" and tablero[6] == "X"):
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste jugador " + nombre_jugador_1)
    elif (tablero[0] == "O" and tablero[1] == "O" and tablero[2] == "X") or (tablero[3] == "O" and tablero[4] == "O" and tablero[5] == "O") or (tablero[6] == "O" and tablero[7] == "O" and tablero[8] == "O"):
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste jugador " + nombre_jugador_2)

    elif (tablero[0] == "O" and tablero[3] == "O" and tablero[6] == "O") or (tablero[1] == "O" and tablero[4] == "O" and tablero[7] == "O") or (tablero[2] == "O" and tablero[5] == "O" and tablero[8] == "O"):
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste jugador " + nombre_jugador_2)

    elif (tablero[0] == "O" and tablero[4] == "O" and tablero[8] == "O") or (tablero[2] == "O" and tablero[4] == "O" and tablero[6] == "O"):
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste jugador " + nombre_jugador_2)

for i in range(0,9):
    tablero.append("N")

#BUTTONS
btn0 = Button(window, width=8, height=4, bg="#011A27", command=lambda: cambiar(0))
lista_btns.append(btn0)
btn0.place(x=50,y=50)
btn1 = Button(window, width=8, height=4, bg="#011A27", command=lambda: cambiar(1))
lista_btns.append(btn1)
btn1.place(x=150,y=50)
btn2 = Button(window, width=8, height=4, bg="#011A27",command=lambda: cambiar(2))
lista_btns.append(btn2)
btn2.place(x=250,y=50)
btn3 = Button(window, width=8, height=4, bg="#011A27", command=lambda: cambiar(3))
lista_btns.append(btn3)
btn3.place(x=50,y=150)
btn4 = Button(window, width=8, height=4, bg="#011A27", command=lambda: cambiar(4))
lista_btns.append(btn4)
btn4.place(x=150,y=150)
btn5 = Button(window, width=8, height=4, bg="#011A27", command=lambda: cambiar(5))
lista_btns.append(btn5)
btn5.place(x=250,y=150)
btn6 = Button(window, width=8, height=4,bg="#011A27", command=lambda: cambiar(6))
lista_btns.append(btn6)
btn6.place(x=50,y=250)
btn7 = Button(window, width=8, height=4, bg="#011A27", command=lambda: cambiar(7))
lista_btns.append(btn7)
btn7.place(x=150,y=250)
btn8 = Button(window, width=8, height=4,bg="#011A27", command=lambda: cambiar(8))
lista_btns.append(btn8)
btn8.place(x=250,y=250)

mostrar_turno_participante = Label(window, textvariable=turno_jugador).place(x=100, y=20)
iniciar_juego = Button(window, background="green", borderwidth=0,  fg="white", text="Iniciar juego", width=15, height=3,command=funcion_iniciar).place(x=130, y=350)

bloquear()

window.mainloop()