from tkinter import *

def bill():
	root.withdraw()
	import rock

def setprice():
	root.withdraw()
	import tic
root=Tk()
root.state('zoomed')
root.resizable(width=False,height=False)
l=Label(root,font=('arial',40,'bold'),text="GAME-HUB",fg="Steel Blue",bd=10,anchor='w')
l.pack()

b1=Button(root,bd=16,fg="black",font=('arial',16,'bold'),width=20,text="Rock Paper Scissor",bg="powder blue",command=bill)
b1.place(x=500,y=100)

b2=Button(root,bd=16,fg="black",font=('arial',16,'bold'),width=20,text="Tic Tac Toe",bg="powder blue",command=setprice)
b2.place(x=500,y=200)

root.mainloop()
