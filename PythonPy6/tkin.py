from tkinter import *
def button_clicked():
    print ("Ты победил, Ура! Леша-хуй")
root = Tk()
button1 = Button(root,text='Уничтожь дракона с помощью могучего топора',width=50,height=5,bg='yellow',fg='magenta',font='colibri 14', command=button_clicked)
button1.pack()
root.mainloop()
