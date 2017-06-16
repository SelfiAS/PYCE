from tkinter import *

app = Tk()
app.title("Game")
app.geometry("650x450")

block = PhotoImage("textures/Blocks/abstractTile_13")

block = Label(app, image=block).pack()

app.mainloop()
