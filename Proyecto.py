import tkinter

# Crea la ventana y se asocia con la variable
v = tkinter.Tk()



# crea los widgets
d = tkinter.Canvas(v, bg="blue", width=1024, height=768)
boton1 = tkinter.Button(v,text="Start")
boton2 = tkinter.Button(v,text="Starrt")


# mustra los widgets
d.pack()
boton1.pack()

# carga una imagen
filename = tkinter.PhotoImage(file='fondo.png')



v.mainloop()
