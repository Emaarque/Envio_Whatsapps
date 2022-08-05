import sys
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import OpenFirefox as of

#gechodriver = '/home/pc-user/Documentos/Registro/Whatsapp/geckodriver'
#gechodriver_log = '/home/pc-user/Documentos/Registro/Whatsapp/gecholog.txt'
#perfil_usuario = "/home/ia1/cv/Proyectos/Envio de Whatsapp/Envio de whatsapp para virologia/perfil firefox" 
opHeadless=of.FuncHeadless()
perfil_usuario=of.OpenPerfil()
gechodriver_log = of.OpenGecholog()
gechodriver = of.OpenGeckodriver()
Webdriverbrowser =int(of.Webdriverbrowser()) 
#gechodriver='/Users/Usuario/Documents/Registro/Version 2/geckodriver.txt'




option= "False"
options = Options()
options.headless = opHeadless
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_profile = webdriver.FirefoxProfile(perfil_usuario)
browser = webdriver.Firefox(executable_path=gechodriver, options=options, capabilities=firefox_capabilities,
                                    service_log_path=gechodriver_log, firefox_profile=firefox_profile)


def comprobar_whatsapp(browser):
    browser.get('https://web.whatsapp.com/')
    try:
        WebDriverWait(browser, Webdriverbrowser).until(EC.presence_of_element_located((By.TAG_NAME,'canvas')))#90
        return False
    except Exception:
        return True
        

