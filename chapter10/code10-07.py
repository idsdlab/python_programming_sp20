import tkinter
import tkinter.messagebox

window = tkinter.Tk()


def myFunc():
    if chk.get() == 0:
        tkinter.messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else:
        tkinter.messagebox.showinfo("", "체크버튼이 켜졌어요.")


chk = tkinter.IntVar()
cb1 = tkinter.Checkbutton(window, text="클릭하세요", variable=chk, command=myFunc)
cb1.pack()

window.mainloop()

