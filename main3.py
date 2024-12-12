from tkinter import * 
import random

root=Tk()
root.title("Spēle")
root.geometry("600x600")
#root.resizable(width=False,height=False)
root.iconbitmap('marsh.ico')

def change_color():
    colors = ['red','black','yellow']
    root.config(bg=random.choice(colors))
btn1=Button(root,text='Poga',command=change_color,font='Arial 20',activebackground='white',activeforeground='red',bg='blue')
btn1.place(y=60,x=300)
a=random(-10,10)
b=random(-10,10)
def move_image():
    global img_x,img_y
    img_x += b
    img_y += b
    l_logo.place(x=img_x,y=img_y) 

img_x,img_y = 50,50

img = PhotoImage(file='pnf.png')
l_logo = Label(root, image=img)
l_logo.place(x=img_x, y=img_y)

btn=Button(root,text="Parvietot attelu", command=move_image)
btn.pack(pady=20)

root.mainloop() 