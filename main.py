from tkinter import *
root=Tk()
root.geometry('600x600')
root.resizable(width=False,height=False)
root.iconbitmap("marsh.ico")
root['bg']='red'
def click():
    print('Sveiciens! ')
btn=Button(root,text='Poga',command=click,font='Arial 20',activebackground='white',activeforeground='red',bg='grean')
btn.pack()

#label1=Label(root,text='wow',font='Arial 20',bg='grean')
#label1.place(x=100, y=50)

img=PhotoImage(file='tuc.jpg')
l_LOGO=Label(root,image=img)
l_LOGO.place(x=10,y=350)
root.mainloop() 