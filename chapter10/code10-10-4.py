from tkinter import *
window = Tk()
window.geometry("600x600")

btnList = [None] * 3

for i in range(0, 3):
    btnList[i] = Button(window, text="버튼" + str(i+1))

for btn in btnList:
    btn.pack(side=TOP, padx=10, pady=10, ipadx=100, ipady=5)

window.mainloop()
