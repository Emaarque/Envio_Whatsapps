import pandas as pd
from datetime import datetime
from send_mjs import send_msj
from browser import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


#fichero="Prueba 1.xlsx"

def lectura_excel(fichero):
    df= pd.read_excel(fichero)
    
    return df

def agrega_caracteristica(df):
    for i in df.index:
        if len(df['Telefono'][i])==6:
            df['Telefono'][i]= '2392'+df['Telefono'][i]
            
    return df

def formato_df(df):
    df['Telefono']= df['Telefono'].astype('str')
    df['Edad']= df['Edad'].astype('str')
    df['Edad']= df['Edad'].replace('\D.*','',regex=True)
    df['Telefono']= df['Telefono'].replace('-','',regex=True)
    df['Telefono']= df['Telefono'].replace('\D.*','',regex=True)
    df['Telefono']= df['Telefono'].replace('^15','',regex=True)
    df['Telefono']= df['Telefono'].replace('^0','',regex=True)
    df['Telefono']= df['Telefono'].replace('[a-zA-Z]','',regex=True)
    df['Telefono']= df['Telefono'].replace(' ','',regex=True)
    
    df['Mensaje']= df['Mensaje'].replace('Nombre','{Nombre}',regex=True)
    df['Mensaje']= df['Mensaje'].replace('Categoria','{Categoria}',regex=True)
    df['Mensaje']= df['Mensaje'].replace('Edad','{Edad}',regex=True)
    df['Mensaje']= df['Mensaje'].replace('Fecha','{Fecha}',regex=True)
        
    
    
    #df= agrega_caracteristica(df)
    df['Envío Telefono']= 'NO ENVIADO'
    
    return df

def envio(msg, df, i):
    if (pd.isnull(df['Telefono'][i]) == True) or (len(df['Telefono'][i])== 0):
        #df.loc[:, (i, 'Envío Telefono')] = 'NO ENVIADO'
        #df['Envío Telefono'][i]= 'NO ENVIADO'
        df.loc[i,'Envío Telefono']= 'NO ENVIADO'
    
    else:
        try:
            telefono = '+549'+str(df['Telefono'][i])
            send_msj(msg,telefono,df,i,browser)
        except:
                pass
            
        
def envio_whatsapp(df, i):
    txt = df['Mensaje'][i]
    msg=txt.format(Nombre=df['Nombre'][i], Fecha=df['Fecha'][i], Edad=df['Edad'][i], Categoria=df['Categoria'][i]) 
    envio(msg, df, i)
    

def guardar_excel(df):
    folder='Envios/'
    time = datetime.now()
    t= time.strftime("%Y-%m-%d %H-%M-%S")
    df['Mensaje']= df['Mensaje'].replace('{Nombre}','Nombre',regex=True)
    df['Mensaje']= df['Mensaje'].replace('{Categoria}','Categoria',regex=True)
    df['Mensaje']= df['Mensaje'].replace('{Edad}','Edad',regex=True)
    df['Mensaje']= df['Mensaje'].replace('{Fecha}','Fecha',regex=True)
        
    df.to_excel(folder+'Enviados '+t+'.xlsx', sheet_name='Enviados')