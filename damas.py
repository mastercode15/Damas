from tkinter import*
from tkinter import messagebox
tk=Tk()
ventana=Tk()
canvas=Canvas(tk, width=645, height=645)
canvas.pack()
canvas.create_rectangle(5,5,80,640)
canvas.create_rectangle(160,5,80,640)
canvas.create_rectangle(240,5,80,640)
canvas.create_rectangle(320,5,80,640)
canvas.create_rectangle(400,5,80,640)
canvas.create_rectangle(480,5,80,640)
canvas.create_rectangle(560,5,80,640)
canvas.create_rectangle(640,5,80,640)

canvas.create_rectangle(5,5,640,80)
canvas.create_rectangle(5,160,640,80)
canvas.create_rectangle(5,240,640,80)
canvas.create_rectangle(5,320,640,80)
canvas.create_rectangle(5,400,640,80)
canvas.create_rectangle(5,480,640,80)
canvas.create_rectangle(5,560,640,80)
canvas.create_rectangle(5,640,640,80)

        #crear fichas de jugador 1
        #columna 1
canvas.create_oval(10, 10, 75, 75, fill="black", tag="ficha")
canvas.pack=canvas.create_oval(10, 235,75,165, fill="black", tag="ficha")
canvas.pack=canvas.create_oval(10, 395,75,325, fill="black", tag="ficha")
canvas.pack=canvas.create_oval(10, 555,75,485, fill="black", tag="ficha")

        #columna 2
canvas.pack=canvas.create_oval(155, 155, 85, 85, fill="black", tag="ficha")
canvas.pack=canvas.create_oval(155, 315, 85, 245, fill="black", tag="ficha")
canvas.pack=canvas.create_oval(155, 475, 85, 405, fill="black", tag="ficha")
canvas.pack=canvas.create_oval(155, 635, 85, 565, fill="black", tag="ficha")

        #columna 3
canvas.pack=canvas.create_oval(235, 10, 165, 75, fill="black", tag="ficha")
canvas.pack=canvas.create_oval(235, 235, 165, 165, fill="black", tag="ficha")
canvas.pack=canvas.create_oval(235, 395, 165, 325, fill="black", tag="ficha")
canvas.pack=canvas.create_oval(235, 555, 165, 485, fill="black", tag="ficha")
        
        #crear fichas de jugador 2

        #columna 1

canvas.pack=canvas.create_oval(635, 315, 565, 245, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(635, 475, 565, 405, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(635, 635, 565, 565, fill="brown", tag="ficha")

                #columna 2
canvas.pack=canvas.create_oval(485, 10, 555, 75, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(485, 235,555, 165, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(485, 395,555,325, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(485, 555,555,485, fill="brown", tag="ficha")

        #columna 3
canvas.pack=canvas.create_oval(405, 155, 475, 85, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(405, 315, 475, 245, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(405, 475, 475, 405, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(405, 635, 475, 565, fill="brown", tag="ficha")

seleccionar=Canvas(ventana, width=400, height=200)
etiqueta=Label(ventana, text="Introduce el numero de ficha que deseas mover", font=("Times New Roman",14)).place(x=15,y=10)
cuadrotexto=Entry(ventana).place(x=25, y=40)

seleccionar.pack()

x,y=25,15;
def move(event):
    global x,y
    if(x<640):
        if event.keysym=="Up":
                canvas.move(28,80,-80)
                y=y-80
                x=x+240
                canvas.delete
                
        elif event.keysym=="Down":
                canvas.move(28,80,80)
                y=y+80
                x=x+80

canvas.bind_all('<KeyPress-Up>', move)
canvas.bind_all('<KeyPress-Down>', move)




tk.mainloop()
