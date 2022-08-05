import pandas as pd
from datetime import datetime
from send_mjs import send_msj1,send_msj2 
from browser import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from Envio_de_Whatsapps import bar
#from Envio_de_Whatsapps import MuestraAvance
fichero="turnos 12 enero.xlsx"
def lectura_excel():
    df= pd.read_excel(fichero)
    df['TEL']= df['TEL'].astype(str)
    df['CEL']= df['CEL'].astype(str)
    try:
        df['FECHA']=df['FECHA'].dt.strftime('%Y/%m/%d')
        #print("paso por fecha")
    except:
        print("no paso")
    return df

def agrega_caracteristica(df):
    for i in df.index:
        if len(df['TEL'][i])==6:
            df['TEL'][i]= '2392'+df['TEL'][i]
        if len(df['CEL'][i])==6:
            df['CEL'][i]= '2392'+df['CEL'][i]
    return df

def formato_df(df):
    df['TEL']= df['TEL'].replace('-','',regex=True)
    df['TEL']= df['TEL'].replace('\D.*','',regex=True)
    df['TEL']= df['TEL'].replace('^15','',regex=True)
    df['TEL']= df['TEL'].replace('^0','',regex=True)
    df['TEL']= df['TEL'].replace('[a-zA-Z]','',regex=True)
    df['TEL']= df['TEL'].replace(' ','',regex=True)
    
    
    df['CEL']= df['CEL'].replace('-','',regex=True)
    df['CEL']= df['CEL'].replace('\D.*','',regex=True)
    df['CEL']= df['CEL'].replace('^15','',regex=True)
    df['CEL']= df['CEL'].replace('^0','',regex=True)
    df['CEL']= df['CEL'].replace('[a-zA-Z]','',regex=True)
    df['CEL']= df['CEL'].replace(' ','',regex=True)
    df['TEL']= df['TEL'].astype('str')
    df['CEL']= df['CEL'].astype('str')
    
    df= agrega_caracteristica(df)
    df['Envío TEL']= 'NO ENVIADO'
    df['Envío CEL']= 'NO ENVIADO'
    return df



def envio1(positivo, negativo, df, i):
    if (pd.isnull(df['TEL'][i]) == True) or (len(df['TEL'][i])== 0):
        df['Envío TEL'][i]= 'NO ENVIADO'
    else:
        try:
            telefono1 = '+549'+str(df['TEL'][i])
            if ('no' in (df['RESULTADO'][i].lower())) or ('negativo' in (df['RESULTADO'][i].lower())):
                send_msj1(negativo,telefono1,df,i,browser)
                
            else:
                send_msj1(positivo,telefono1,df,i,browser)
                
        except:
            pass
def envio2(positivo, negativo, df, i):
   if (pd.isnull(df['CEL'][i]) == True) or (len(df['CEL'][i])== 0):
       df['Envío CEL'][i]= 'NO ENVIADO'
   else:
        try:
            telefono2 = '+549'+str(df['CEL'][i])
            if ('no' in (df['RESULTADO'][i].lower())) or ('negativo' in (df['RESULTADO'][i].lower())):
                send_msj2(negativo,telefono2,df,i,browser)
            else:
                send_msj2(positivo,telefono2,df,i,browser)
        except:
            pass

positivo_final = '''
Deberá comunicarse con su médico de cabecera para su seguimiento médico.'''


def envio_whatsapp(df):
    df = formato_df(df)
    for i in df.index:
        positivo = 'Ud. *' + str(df['PACIENTE'][i])+'* , DNI: *' + str(df['DNI'][i]) + '* se realizó la prueba para COVID-19 siendo su resultado *' + str(df['RESULTADO'][i]).upper() + '*.' + positivo_final
        negativo= 'Ud. *' + str(df['PACIENTE'][i])+'*, DNI: *' + str(df['DNI'][i]) + '* se realizó la prueba para COVID-19 siendo su resultado *' + str(df['RESULTADO'][i]).upper() + '*.'
        envio1(positivo,negativo,df,i)
        envio2(positivo,negativo,df,i)
        print(str(i) + ' de ' + str(len(df)))
        #bar(int(i),int(len(df)))
        #MuestraAvance(int(i))
    return df

def guardar_excel(df):
    folder='Envios/'
    time = datetime.now()
    t= time.strftime("%Y-%m-%d %H-%M-%S")
    df.to_excel(folder+'Enviados '+t+'.xlsx', sheet_name='Enviados')