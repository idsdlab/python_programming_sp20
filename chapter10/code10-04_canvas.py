# from tkinter import *
# window = Tk()
#
#
# photo = PhotoImage(file='gif/dog.gif')
# width, height = photo.width(), photo.height()
# dimensions = "image size: %dx%d" % (photo.width(), photo.height())
# print(dimensions)
# # if canvas != None:
# #     canvas.destory()
#
# label = Label(window, text="Image")
# label.pack()
#
# canvas = Canvas(window, width=width, height=height)
# canvas.create_image((width/2), (height/2), image=photo, state="normal")
# canvas.pack()
#
# window.mainloop()

import time

from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=400, height=200)

canvas.pack()

canvas.create_polygon(10, 10, 10, 60, 50, 35)

for x in range(0, 60):
    canvas.move(1, 5, 0)

    tk.update()

    time.sleep(0.05)
