from ast import Break
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
import webbrowser
import time
import funciones_pct as fn
from browser import browser,comprobar_whatsapp
import OpenFirefox as of
import os
import sys  

root=Tk()
df=0
root.iconbitmap(r'whatsapp-polo-2.ico')
root.configure(bg='white')


def folderRetry2():
    valor=messagebox.askretrycancel("Carpeta no válida", "Error en el nombre del directorio. Directorio inválido.")
    if valor==True:
        OpenFolder()

def folderRetry(directorio):
    valor=messagebox.askretrycancel("Carpeta no válida", "No es posible abrir la carpeta "+ directorio +". Directorio inválido.")
    if valor==True:
        OpenFolder()
    

def OpenFolder():
    try:
        directorio=filedialog.askdirectory(title="Abrir Carpeta de Perfil de Firefox", initialdir="C:")
        of.SaveDir(directorio)
    except:
        folderRetry(directorio)

def exitApp():
    valor=messagebox.askokcancel("Salir", "¿Seguro que Desea Salir de la apicación?")
    if valor==True:
        CloseNavigator()
        root.destroy()

def windowRequest():
    messagebox.showinfo("Aviso","¡Hecho!")

def windowCodigoQR():
    valor=messagebox.showinfo("Aviso","Por favor, escanee el codigo QR en Firefox")
    OpenNavigator()
    sys.exit()

def windowRequestEnvios():
    messagebox.showinfo("Fin de los envios","¡Mensajes enviados Exitosamente!")

def License():
    messagebox.showinfo("Licencia","Aplicación software del Polo Científico Tecnológico")

def documentRetry(fichero, e):
    valor=messagebox.askretrycancel("Planilla no válida", "No es posible cargar el archivo "+ fichero +".\n Envio: " + str(e))
    if valor==True:
        OpenFile()
        

def OpenNavigator():
    webbrowser.open_new("https://web.whatsapp.com/")

def CloseNavigator():
    try:
        browser.close()
    except:
        pass

def OpenFile():
    global df
    try:
        fichero=filedialog.askopenfilename(title="Abrir planilla", initialdir="C:", filetypes=(("Archivos Excel","*.xlsx"),("Todos los archivos", "*.*")))
        df= fn.lectura_excel(fichero) 
        df= fn.formato_df(df) 
        windowRequest()
        my_text.delete(1.0, END)
        add_txt2(str(len(df))+" mensajes cargados \n")
    except Exception as e:
        documentRetry(fichero, e)


def codigoBoton():
    global df
    if df.empty != False:
        my_text.insert(INSERT, "No hay mensajes para enviar\n")
        return
        
    if comprobar_whatsapp(browser)==False:
        windowCodigoQR()
    
    for i in df.index:
        fn.envio_whatsapp(df, i)
        c=i+1
        my_text.insert(INSERT, "Mensaje "+str(c)+" "+df['Envío Telefono'][i]+"\n")
        bar(c, len(df))
        root.update() # allow window to catch up
        
    
    fn.guardar_excel(df)
    my_text.insert(INSERT, "¡Mensajes enviados!\n")
    windowRequestEnvios()
    

def on_closing():
    if messagebox.askokcancel("Cerrar", "¿Quieres cerrar la Aplicación Envio Whatsapp?"):
        CloseNavigator()
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

## titulo de la ventana
root.title("Envio de Whatsapps")

barMenu=Menu(root)
root.config(menu=barMenu)

archivoMenu=Menu(barMenu, tearoff=0)
archivoMenu.add_command(label="Cargar Carpeta Firefox", command=OpenFolder)
archivoMenu.add_command(label="Salir", command=exitApp)


ayudaMenu=Menu(barMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=License)


barMenu.add_cascade(label="Archivo", menu=archivoMenu)
barMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


root.geometry("650x400")


label1=Label(text="Buscar las planillas de archivo Excel.", bg='white')
label1.pack()


Button (root, text="Buscar Planilla", command=OpenFile).pack()

label1=Label(text="Enviar los mensajes por Whatsapp.", bg='white')

label1.pack()

botonEnvio = Button(root, text="Enviar Whatsapps", command=codigoBoton)
botonEnvio.pack()

    
def add_txt2 (text):
    my_text.insert(INSERT, text)

my_frame = Frame(root)
my_frame.pack(pady=10)

# Create scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)
my_text = Text(my_frame, width=40, height=10, yscrollcommand=text_scroll.set, undo=True)
my_text.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview)

def bar(i, long):
    cont=((i*100)/long)
    
    progress['value'] = cont
    #print(i)
    root.update_idletasks()

progress = Progressbar(root, orient = HORIZONTAL,
			length = 350, mode = 'determinate')
progress.pack(pady = 10)


root.mainloop()

