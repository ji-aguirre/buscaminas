from tkinter import *
from comandos import Juego
import buscaminas

def apretar_boton():
	print("APRETE BOTON",event.x,event.y)
	



juego = Juego(10,10,15)
#juego.inicializar(10,10,15)

tablero = juego.tablero
botones_x = []
botones_y = []
#Create & Configure root 
root = Tk()
root.title("Buscaminas - Juan Aguirre")
root.resizable(100,100)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#Create & Configure frame 
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

tablero.mostrar_tablero

#Create a X x Y  (rows x columns) grid of buttons inside the frame
for row_index in range(tablero.alto):
    Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(tablero.largo):
        Grid.columnconfigure(frame, col_index, weight=1)
        btn = Button(frame,text=str(tablero.tablero[row_index][col_index]),command=apretar_boton) #create a button inside frame 
        btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)
        btn.bind("<Button-1>",apretar_boton)
        botones_x.append(btn.grid_info())
    botones_y.append(botones_x)

print(botones_y[0])
root.mainloop()