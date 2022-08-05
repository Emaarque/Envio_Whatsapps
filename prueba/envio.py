from funciones import *
#from prueba_polo import *
from browser import browser,comprobar_whatsapp

df= lectura_excel() #lee el excel
print("paso0")
df= formato_df(df) # conviente las FECHAs, elimina letras de los telefonos y agrega la columna envios
print("paso1")
comprobar_whatsapp(browser)
print("paso2")
df = envio_whatsapp(df) # envia los whatsapp

guardar_excel(df) #guarda el excel con los RESULTADOs en carpeta covid en escritorio

try:
    browser.close()
except:
    pass