from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
import time
import webbrowser
import funciones_pct as fn
#from browser import browser,comprobar_whatsapp
from browser_chrome import browser, comprobar_whatsapp
import OpenFirefox as of
#import attachment as at
import os
import sys 

root=Tk()
df=0
imagePath=0
root.configure(bg='white')
# Creamos frame principal
FrameMain= Frame(root, bg='white')
# Posicionamos frame en ventana principal
FrameMain.pack(expand=True)

# configure the grid
#root.columnconfigure([0,1,2], weight=0)

#root.rowconfigure([0,1], weight=1)
#root.rowconfigure(1, weight=1)
#root.columnconfigure(1, weight=3)


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
    valor=messagebox.askretrycancel("Planilla no válida", "No es posible cargar el archivo "+ fichero +". \n Envio: "+ str(e))
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

def codigoImagen():
    global imagePath
    try:
        imagePath=filedialog.askopenfilename(title="Abrir Imagen", initialdir="C:", filetypes=(("Archivos JPG","*.jpg"),("Archivos PNG","*.png"),("Todos los archivos", "*.*"))) 
        #df= fn.formato_df(df) 
        windowRequest()
        my_text.insert(INSERT, "Cargada imagen\n"+imagePath)
        #print(imagePath)
        #Label(FrameMenu, text=imagePath, bg='white').pack()
    except:
        documentRetry(imagePath)

def codigoBoton():
    global df, imagePath
    
    print(imagePath)
    if df.empty != False:
        my_text.insert(INSERT, "No hay mensajes para enviar\n")
        return
    
    if comprobar_whatsapp(browser)==False:
        windowCodigoQR()
    #Label(root, text="Listo para enviar mensajes.", bg='white').pack()'''
    
    if imagePath != 0:
        print("Hay imagen")
        for i in df.index:
            fn.envio_whatsapp_image(df, i, imagePath)
            c=i+1
            my_text.insert(INSERT, "Mensaje "+str(c)+" "+df['Envío Telefono'][i]+"\n")
            bar(c, len(df))
            root.update() # allow window to catch up
    
    else:
        for i in df.index:
            fn.envio_whatsapp(df, i)
            c=i+1
            my_text.insert(INSERT, "Mensaje "+str(c)+" "+df['Envío Telefono'][i]+"\n")
            bar(c, len(df))
            root.update() # allow window to catch up
    '''
    for i in df.index:
            fn.envio_whatsapp_image(df, i, imagePath)
            c=i+1
            my_text.insert(INSERT, "Mensaje "+str(c)+" "+df['Envío Telefono'][i]+"\n")
            bar(c, len(df))
            root.update() # allow window to catch up'''
        
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


root.geometry("850x600")

FrameMenu = Frame(FrameMain, bg='white')
#FrameText.grid(padx=10, pady=10, ipadx=10, ipady=5, column=0, row=7, columnspan=2)
FrameMenu.pack(expand=True)

labelPlanilla=Label(FrameMenu, text="Buscar las planillas de archivo Excel.", bg='white')
BotonPlanilla= Button(FrameMenu, text="Buscar Planilla", command=OpenFile)

labelImagen=Label(FrameMenu, text="Buscar la imagen que se quiera subir.", bg='white')
botonImagen = Button(FrameMenu, text="Subir imagen", command=codigoImagen)

labelEnvio=Label(FrameMenu, text="Enviar las deteccion de covid por Whatsapp.", bg='white')
botonEnvio = Button(FrameMenu, text="Enviar Whatsapps", width=40,command=codigoBoton)


'''
labelPlanilla.grid(pady=10, column=0, row=0)

BotonPlanilla.grid( padx=20, column=1, row=0)

labelImagen.grid(pady=10, column=0, row=3)
botonImagen.grid(column=1, row=3)

labelEnvio.grid(column=0, row=5, columnspan=2)

botonEnvio.grid(padx=10, pady=10,column=0, row=6, columnspan=2)
'''
labelPlanilla.grid(row=0, column=0, padx=5, pady=10)

BotonPlanilla.grid(row=0, column=1, padx=5, pady=10, ipadx=10, ipady=5)

labelImagen.grid(row=1, column=0, padx=5, pady=10)
botonImagen.grid( row=1, column=1, padx=5, pady=10, ipadx=10, ipady=5)

labelEnvio.grid(row=2, column=0, padx=5, pady=10, columnspan=2)
botonEnvio.grid(padx=10, pady=10, ipadx=10, ipady=5, column=0, row=6, columnspan=2)

def add_txt2 (text):
    my_text.insert(INSERT, text)

FrameText = Frame(FrameMain, bg='white')
#FrameText.grid(padx=10, pady=10, ipadx=10, ipady=5, column=0, row=7, columnspan=2)
FrameText.pack(expand=True)
# Create scrollbar
text_scroll = Scrollbar(FrameText)
text_scroll.pack(side=RIGHT, fill=Y)
my_text = Text(FrameText, width=60, height=20, yscrollcommand=text_scroll.set, undo=True)
my_text.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview)

def bar(i, long):
    cont=((i*100)/long)
    
    progress['value'] = cont
    #print(i)
    root.update_idletasks()

progress = Progressbar(FrameMain, orient = HORIZONTAL,
			length = 450, mode = 'determinate')
progress.pack(padx=10, pady=10, ipadx=10, ipady=5)


'''
labelPlanilla.grid(column=0, row=0)

BotonPlanilla.grid(pady=10, column=0, row=1 )

labelImagen.grid(column=0, row=3,padx=10)
botonImagen.grid(pady=10,column=0, row=4)

labelEnvio.grid(column=0, row=5)

botonEnvio.grid(pady=10,column=0, row=6)
'''

'''
labelPlanilla.pack(pady=10)
BotonPlanilla.pack(pady=0)

labelImagen.pack(pady=10)
botonImagen.pack(pady=0)

labelEnvio.pack(pady=10)
botonEnvio.pack(pady=0)
'''

root.mainloop()

