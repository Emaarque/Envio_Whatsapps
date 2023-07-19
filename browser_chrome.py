import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
'''
from selenium.webdriver.firefox.options import Options
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import OpenFirefox as of
import OpenChrome as oc

#driver=

#gechodriver = '/home/pc-user/Documentos/Registro/Whatsapp/geckodriver'
#gechodriver_log = '/home/pc-user/Documentos/Registro/Whatsapp/gecholog.txt'
#perfil_usuario = "/home/ia1/cv/Proyectos/Envio de Whatsapp/Envio de whatsapp para virologia/perfil firefox" 
'''opHeadless=of.FuncHeadless()
perfil_usuario=of.OpenPerfil()
gechodriver_log = of.OpenGecholog()
gechodriver = of.OpenGeckodriver()
perfil_usuariochrome=OpenPerfilChrome()'''
#gechodriver='/Users/Usuario/Documents/Registro/Version 2/geckodriver.txt'
#Hacer lo mismo con el resto
#service = ChromeService(executable_path="chromedriver")

#Chrome 
opHeadless=oc.FuncHeadless()
perfil_usuariochrome=oc.OpenPerfilChrome()

#esto para actualice solo
#service = ChromeService(executable_path=ChromeDriverManager().install())

#driver=webdriver.Chrome()

options = ChromeOptions()

#modificacion para el headless

#options.headless = True #opHeadless

options.add_argument('--headless')
options.add_argument("--window-size=1920,1080")

'''driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)'''
#options.add_argument('--profile-directory=Profile 1')
#options.add_argument("user-data-dir=C:\\Users\\Usuario\\AppData\\Local\\Google\\Chrome\\User Data\\") #Path to your chrome profile
options.add_argument("user-data-dir=C:\\Users\\Usuario\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")

browser = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
#browser.get('https://web.whatsapp.com/')


#Firefox propiedades
''' 
print(opHeadless)
option= "False"
options = Options()
options.headless = opHeadless
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_profile = webdriver.FirefoxProfile(perfil_usuario)
'''
#Driver Firefox
'''
browser = webdriver.Firefox(executable_path=gechodriver, options=options, capabilities=firefox_capabilities,
                                    service_log_path=gechodriver_log, firefox_profile=firefox_profile)
'''

def comprobar_whatsapp(browser):
    browser.get('https://web.whatsapp.com/')
    #probar haciendo ciclo while
    try:
        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.TAG_NAME,'canvas')))
        return False
    except Exception:
        return True

        

