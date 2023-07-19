from tkinter import *
from tkinter.ttk import Progressbar

root=Tk()

###progress bar 

def bar(i):
    progress.start()
    long=20
    cont=((i*100)/long)
    progress['value'] = cont
    root.update_idletasks()

'''
dato=0
def MuestraAvance(dato1):
    global dato
    dato=dato+1
    Label(root, text=dato1, bg='white').pack()
'''   

progress = Progressbar(root, orient = HORIZONTAL,
			length = 350, mode = 'determinate')
progress.pack(pady = 10)

#bar(1)
#botonEnvio = Button(root, text="Enviar Whatsapps", command=MuestraAvance)
#botonEnvio.pack()

root.mainloop()