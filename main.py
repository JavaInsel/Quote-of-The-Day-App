import tkinter as tk

window = tk.Tk()
window.geometry("500x300")
window.maxsize(500,300)


window.title("Pomodoro")

initialValue = 0

textVar = tk.StringVar()
textVar.set(initialValue)

def addNum():
    global initialValue
    initialValue = initialValue + 1
    textVar.set(initialValue)

def minNum():
     global initialValue
     if initialValue > 0:
        initialValue = initialValue - 1
        textVar.set(initialValue)

def countdown():
    global initialValue
    initialValue = initialValue - 1
    textVar.set(initialValue)
    window.after(1000,countdown)


lbl_minute_titel = tk.Label(window, text="Minute", width=15, borderwidth=2, relief="raised")
lbl_minute_titel.grid(row=0, column=0,columnspan=3)

btn_minus = tk.Button(window, text='-', width=5,command=minNum)
btn_minus.grid(row=1, column=0)

lbl_minute = tk.Label(window, textvariable=textVar, width=5)
lbl_minute.grid(row=1, column=1)

btn_plus = tk.Button(window, text='+', width=5, command=addNum)
btn_plus.grid(row=1,column=2)

btn_start = tk.Button(window, text='start', width=5, command=countdown)
btn_start.grid(row=2,column=1)


window.mainloop()

