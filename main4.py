from tkinter import *

root=Tk()
root.title("Spēle")
root.geometry("600x600")
#root.resizable(width=False,height=False)
root.iconbitmap('marsh.ico')

def in_count():
    global count
    count += 1
    label.config(text=f"Klikskini: {count}")

count = 0

label=Label(root,text=f"Klikskini: {count}",font='Arial 20')
label.pack(pady=20)

btn=Button(root,text="Klikskini mani!",font='Arial 20', command=in_count)
btn.pack()

root.mainloop() 