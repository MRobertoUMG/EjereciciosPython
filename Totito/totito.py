from tkinter import *
from tkinter import messagebox
from tkinter  import  simpledialog

window = Tk()

#CUSTOMING FRAME
#window.configure(background='212529')
window.geometry("370x500")
window.title("TOTITO ;)")

turno = 0
nombre_jugador_1 = ""
nombre_jugador_2 = ""
lista_btns = []
tablero = []
turno_jugador = StringVar()

for i in range(0,9):
    tablero.append("N")

#BUTTONS
btn0 = Button(window, width=8, height=4) #command=command(0))
lista_btns.append(btn0)
btn0.place(x=50,y=50)
btn1 = Button(window, width=8, height=4) #command=command(0))
lista_btns.append(btn1)
btn1.place(x=150,y=50)
btn2 = Button(window, width=8, height=4) #command=command(0))
lista_btns.append(btn2)
btn2.place(x=250,y=50)
btn3 = Button(window, width=8, height=4) #command=command(0))
lista_btns.append(btn3)
btn3.place(x=50,y=150)
btn4 = Button(window, width=8, height=4) #command=command(0))
lista_btns.append(btn4)
btn4.place(x=150,y=150)
btn5 = Button(window, width=8, height=4) #command=command(0))
lista_btns.append(btn5)
btn5.place(x=250,y=150)
btn6 = Button(window, width=8, height=4) #command=command(0))
lista_btns.append(btn6)
btn6.place(x=50,y=250)
btn7 = Button(window, width=8, height=4) #command=command(0))
lista_btns.append(btn7)
btn7.place(x=150,y=250)
btn8 = Button(window, width=8, height=4) #command=command(0))
lista_btns.append(btn8)
btn8.place(x=250,y=250)

mostrar_turno_participante = Label(window, textvariable=turno_jugador).place(x=100, y=20)
iniciar_juego = Button(window, background="green", borderwidth=0, fg="white", text="Iniciar juego", width=15, height=3).place(x=130, y=350)

window.mainloop()