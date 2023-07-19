import os
#from queue import Empty
from genericpath import exists, isdir, isfile


def FuncXpath():
    file=open("config/xpath.dat")
    fichero=file.read()
    file.close()
    return fichero

def FuncTimeAfterEnvio():
    file=open("config/TimeAfterEnvio.dat")
    fichero=file.read()
    file.close()
    return fichero

def WebdriverSms():
    file=open("config/WebdriverSms.dat")
    fichero=file.read()
    file.close()
    return fichero
    
def Webdriverbrowser():
    file=open("config/Webdriverbrowser.dat")
    fichero=file.read()
    file.close()
    return fichero

def prueba():
    file=open("config/prueba.dat")
    fichero=file.read()
    print(fichero)
    file.close()
    return fichero
