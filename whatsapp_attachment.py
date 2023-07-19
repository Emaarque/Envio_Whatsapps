from selenium import webdriver
from time import sleep
from browser import browser,comprobar_whatsapp

'''driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')'''
'''driver = webdriver.Firefox(
    executable_path='C:\Proyectos\Repositorios\Envio Wpp Polo\geckodriver.exe')'''

comprobar_whatsapp(browser)

name = input('Enter the name of user or group : ')
#filepath = input('Enter your filepath (images/video): ')
filepath="C:\Proyectos\Repositorios\Envio Wpp Polo\whatsapp-polo 2.png"
input('Enter anything after scanning QR code')

user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

attachment_box = browser.find_element_by_xpath('//div[@title = "Attach"]')
attachment_box.click()

image_box = browser.find_element_by_xpath(
    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)

sleep(3)

send_button = browser.find_element_by_xpath('//span[@data-icon="send-light"]')
send_button.click()