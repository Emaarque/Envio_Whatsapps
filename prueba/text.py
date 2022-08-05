from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Codemy.com - Learn To Code!')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x350")

# Read only r  
# Read and Write r+  (beginning of file)
# Write Only w   (over-written)
# Write and Read w+  (over written)
# Append Only a  (end of file)
# Append and Read a+  (end of file)

def add_txt ():
    my_text.insert(INSERT, "Hola mundo \n")
    


my_frame = Frame(root)
my_frame.pack(pady=10)

# Create scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)
my_text = Text(my_frame, width=40, height=10, font=("Helvetica", 16), yscrollcommand=text_scroll.set, undo=True)
my_text.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview)

add_button = Button(root, text="Add Text", command=add_txt)
add_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack()



root.mainloop()