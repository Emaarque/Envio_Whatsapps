from urllib.parse import quote
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from OpenFirefox import FuncTimeAfterEnvio, FuncXpath, WebdriverSms

TimeAfterEnvio=FuncTimeAfterEnvio()
xpath=FuncXpath()
WebdriverSms=int(WebdriverSms())
TimeAfterEnvio=int(TimeAfterEnvio)

def send_msj(text,num,df,i,browser):
    text1=quote(text)
    browser.get('https://web.whatsapp.com/send?phone=' + num + '&text=' + text1)
    #input_xpath = '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
    #input_xpath = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
    #input_xpath = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p'
    input_xpath = xpath
    try:
        input_box = WebDriverWait(browser, WebdriverSms).until(EC.presence_of_element_located((By.XPATH, input_xpath)))#90, 20
        input_box.send_keys(Keys.ENTER)
        time.sleep(TimeAfterEnvio)
        input_box.send_keys(Keys.ENTER)
        #df['Envío Telefono'][i]= 'Enviado'
        #df.loc[:, ('Envío Telefono')] = 'Enviado'
        df.loc[i,'Envío Telefono']= 'Enviado'
    except:
        #df.loc[:, ('Envío Telefono')] = 'NO ENVIADO'
        #df['Envío Telefono'][i]= 'NO ENVIADO'
        df.loc[i,'Envío Telefono']= 'NO ENVIADO'

def send_msj_img(text,num,filepath,df,i,browser):
    text1=quote(text)
    print("llego send_msj")
    
    browser.get('https://web.whatsapp.com/send?phone=' + num + '&text=' + text1)
    time.sleep(15)
    attachment_box = browser.find_element('xpath','//div[@title = "Adjuntar"]')
    attachment_box.click()
    time.sleep(5)
    
    image_box = browser.find_element(
        'xpath',
        '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    #time.sleep(5)
    image_box.send_keys(filepath)
    
    #input_xpath = '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
    #input_xpath = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
    #input_xpath = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p'
    input_xpath = xpath
    
    
    #image_box = browser.find_element_by_xpath(
    #    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    
    time.sleep(1)
    try:
        input_box = WebDriverWait(browser, WebdriverSms).until(EC.presence_of_element_located((By.XPATH, input_xpath)))#90, 20
        '''
        input_box.send_keys(Keys.ENTER)
        time.sleep(TimeAfterEnvio)
        input_box.send_keys(Keys.ENTER)
        '''
        send_button = browser.find_element('xpath','//span[@data-icon="send"]')
        send_button.click()
        time.sleep(5)
        #input_box.send_keys(Keys.ENTER)
        #df['Envío Telefono'][i]= 'Enviado'
        #df.loc[:, ('Envío Telefono')] = 'Enviado'
        df.loc[i,'Envío Telefono']= 'Enviado'
        
    except:
        #df.loc[:, ('Envío Telefono')] = 'NO ENVIADO'
        #df['Envío Telefono'][i]= 'NO ENVIADO'
        df.loc[i,'Envío Telefono']= 'NO ENVIADO'







      