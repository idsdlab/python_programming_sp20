from tkinter import *
window = Tk()

photo1 = PhotoImage(file='gif/dog.gif')
label1 = Label(window, image=photo1)

photo2 = PhotoImage(file='gif/cat.gif')
label2 = Label(window, image=photo2)

# -side
LEFT='left'
TOP='top'
RIGHT='right'
BOTTOM='bottom'

label1.pack(side=LEFT)
label2.pack()

window.mainloop()

