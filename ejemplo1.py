import tkinter as tk


class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_attributes('-zoomed', 1)
        self.root.grid_rowconfigure(0, weight=1, uniform="rows_g1")
        self.root.grid_rowconfigure(1, weight=5, uniform="rows_g1")
        self.root.grid_columnconfigure(0, weight=3,  uniform="cols_g1")
        self.root.grid_columnconfigure(1, weight=1,  uniform="cols_g1")

        fm1 = tk.Frame(self.root, bg='red')
        fm1.grid(row=0, column=0, columnspan=2, sticky='nsew')

        fm2 = tk.Frame(self.root, bg='blue')
        fm2.grid(row=1, column=0, sticky='nsew'),

        fm3 = tk.Frame(self.root, bg='green')
        fm3.grid(row=1, column=1, sticky='nsew')

        tk.Label(
            fm1, text='FRAME 1',  bg="red",  fg="white", font=("Courier", 20)
            ).pack(expand=True)
        tk.Label(
            fm2, text='FRAME 2',  bg="blue",  fg="white", font=("Courier", 20), 
            ).pack(expand=True)
        tk.Label(
            fm3, text='FRAME 3', bg="green",  fg="white", font=("Courier", 20)
            ).pack(expand=True)

    def mainloop(self):
        self.root.mainloop()


if __name__ == '__main__':
    ejemplo1 = App()
    ejemplo1.mainloop()