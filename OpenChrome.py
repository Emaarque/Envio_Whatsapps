import os
#from queue import Empty
from genericpath import exists, isdir, isfile


def CompruebaNombre():
    file=open("config/Datos_Chrome.dat","r")
    fichero=file.read()
    file.close()    
    if "Chrome" in fichero:         
        return True
    else:
        return False
        
def FuncHeadless():
    file=open("config/opHeadless.dat")
    fichero=file.read()
    file.close()
    bool(fichero)
    return fichero
    
def Webdriverbrowser():
    file=open("config/Webdriverbrowser.dat")
    fichero=file.read()
    file.close()
    return fichero

def OpenPerfilChrome():
    file=open("config/Datos_Chrome.dat")
    fichero=file.read()
    print(fichero)
    file.close()
    return fichero

print(CompruebaNombre())
