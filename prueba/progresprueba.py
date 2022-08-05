# importing tkinter module
from tkinter import * 
from tkinter.ttk import *
import time

# creating tkinter window
root = Tk()

# Progress bar widget


#progress=Progressbar(maximum=10)
# Function responsible for the updation
# of the progress bar value
def bar(i, long):
    cont=((i*100)/long)
    
    progress['value'] = cont
    print(i)
    root.update_idletasks()

progress = Progressbar(root, orient = HORIZONTAL,
			length = 350, mode = 'determinate')

#

def fun():
    progress.pack(pady = 10)
    long=20
    for i in range(0, long+1):
            bar(i,long)
            time.sleep(1)

# This button will initialize
# the progress bar
Button(root, text = 'Start', command = fun).pack(pady = 10)

# infinite loop
mainloop()
