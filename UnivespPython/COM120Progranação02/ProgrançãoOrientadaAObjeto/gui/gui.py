"""from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage(file='tenor.gif').subsample(5)
hello = Label(master=root, text='hello word!')
imagem = Label(master=root, image=photo)
imagem.pack(side=TOP)
hello.pack(side=BOTTOM)
"""

"""from tkinter import Tk, Label, PhotoImage, RAISED
root = Tk()
labels = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],['*', '0', '#']]
for r in range(4):
    for c in range(3):
        label = Label(root, relief=RAISED, padx=15, pady=5, text=labels[r][c])
        label.grid(row=r, column=c)
root.mainloop()
"""

'''from tkinter import Tk, Label, Button
from tkinter.messagebox import showinfo
from time import strftime, localtime

def clica():
    tempo = strftime('Dia: %d %b %y\nTempo %H:%M:%S%p', localtime())
    showinfo(message=tempo)


root = Tk()
button = Button(root, text='Clique', command=clica)
button.pack()
root.mainloop()'''


from tkinter import Tk, Button, Label, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime

'''
não funciona!!!!!!

def clicked():
    global entry
    date = entry.get()
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    showinfo(message='{} foi uma {}'.format(date, weekday))


root = Tk()
label = Label(root, text='Digite uma data:')
label.grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)
button = Button(root, text='Clique', command=clicked())
button.grid(row=1, column=0, columnspan=2)
root.mainloop()'''