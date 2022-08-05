from tkinter import *
import time

root = Tk()

count =0
def counter():
  global count
  while(count<100):
      Label(root, text=count).pack()
      root.update() # allow window to catch up
      time.sleep(2)
      count += 1

count = counter()
root.mainloop()