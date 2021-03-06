from tkinter import *
from time import *
# import GIF.cheat_sheet

fnameList = [
    "jeju1.gif",
    "jeju2.gif",
    "jeju3.gif",
    "jeju4.gif",
    "jeju5.gif",
    "jeju6.gif",
    "jeju7.gif",
    "jeju8.gif",
    "jeju9.gif"
]

photoList = [None] * 9
num = 0

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    fname = "gif/" + fnameList[num]
    photo = PhotoImage(file=fname)
    pLabel.configure(image=photo)
    pLabel.image = photo
    pfnameLabel.configure(text=fname)

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8

    fname = "gif/" + fnameList[num]
    photo = PhotoImage(file=fname)
    pLabel.configure(image=photo)
    pLabel.image = photo
    pfnameLabel.configure(text=fname)


window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text=">> 이후", command=clickNext)

photo = PhotoImage(file="gif/" + fnameList[0])
pLabel = Label(window, image=photo)
pfnameLabel = Label(window, text="gif/" + fnameList[0])

btnPrev.place(x=250, y=10)
pfnameLabel.place(x=325, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)

window.mainloop()


