from selenium import webdriver
from time import sleep
#from browser import browser,comprobar_whatsapp
from browser_chrome import browser,comprobar_whatsapp

'''driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')'''
'''driver = webdriver.Firefox(
    executable_path='C:\Proyectos\Repositorios\Envio Wpp Polo\geckodriver.exe')'''

comprobar_whatsapp(browser)


#name = input('Enter the name of user or group : ')
num = '+5492396575139' 
text1 = 'hola mundo' 
#name = "GRUPO"
#filepath = input('Enter your filepath (images/video): ')
#filepath="C:\Proyectos\Repositorios\Envio Wpp Polo\whatsapp-polo 2.png"



    
filepath='C:/Users/Usuario/Desktop/Envio Whatsapp/Version 4/309077423_1175075699742215_5535042022284426909_n.jpg'
#input('Enter anything after scanning QR code')

#user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(name))

#user = browser.find_element('xpath','//span[@title = "{}"]'.format(name))

#user.click()

#browser.get('https://web.whatsapp.com/send?phone=' + num + '&text=' + text1) 

#attachment_box = browser.find_element_by_xpath('//div[@title = "Attach"]')
#sleep(30)
#attachment_box = browser.find_element('xpath','//div[@title = "Attach"]')

def envio_image(filepath):
    attachment_box = browser.find_element('xpath','//div[@title = "Adjuntar"]')
    attachment_box.click()
    #image_box = browser.find_element_by_xpath(
    #    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box = browser.find_element(
        'xpath',
        '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(filepath)
    sleep(3)

envio_image()
#send_button = browser.find_element_by_xpath('//span[@data-icon="send-light"]')
#send_button = browser.find_element('xpath','//span[@data-icon="send-light"]')
send_button = browser.find_element('xpath','//span[@data-icon="send"]')
send_button.click()