import os
#from queue import Empty
from genericpath import exists, isdir, isfile


def CompruebaNombre():
    file=open("config/Datos Firefox.dat","r")
    fichero=file.read()
    file.close()    
    if "Perfil firefox" in fichero:         
        return True
    else:
        return False
        
def FuncHeadless():
    file=open("config/opHeadless.dat")
    fichero=file.read()
    file.close()
    bool(fichero)
    return fichero

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

def OpenPerfil():
    file=open("config/Datos_Firefox.dat")
    fichero=file.read()
    file.close()
    return fichero

def OpenGecholog():
    file=open("config/Datos_gecholog.dat")
    fichero=file.read()
    file.close()
    return fichero

def OpenGeckodriver():
    file=open("config/Datos_geckodriver.dat")
    fichero=file.read()
    file.close()
    return fichero

def SaveDir(FirefoxPath):
    file=open("config/Datos_Firefox.dat","w")
    file.write(FirefoxPath)
    file.close()


#OpenGeckodriver()