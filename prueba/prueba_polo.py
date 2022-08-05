import pandas as pd
from datetime import datetime
from send_mjs import send_msj#,send_msj2 
from browser import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#from Envio_de_Whatsapps import bar
#from Envio_de_Whatsapps import MuestraAvance

#fichero="Prueba 1.xlsx"

def lectura_excel(fichero):
    print("paso lectura")
    df= pd.read_excel(fichero)
    #df['Telefono']= df['Telefono'].astype(str)
    print(df['Telefono'])

    #df['CEL']= df['CEL'].astype(str)
    ''' try:
        df['FECHA']=df['FECHA'].dt.strftime('%Y/%m/%d')
        #print("paso por fecha")
    except:
        print("no paso")'''
    return df

def agrega_caracteristica(df):
    for i in df.index:
        if len(df['Telefono'][i])==6:
            df['Telefono'][i]= '2392'+df['Telefono'][i]
        #if len(df['CEL'][i])==6:
        #    df['CEL'][i]= '2392'+df['CEL'][i]
    return df

def formato_df(df):
    '''
    df['TEL']= df['TEL'].replace('-','',regex=True)
    df['TEL']= df['TEL'].replace('\D.*','',regex=True)
    df['TEL']= df['TEL'].replace('^15','',regex=True)
    df['TEL']= df['TEL'].replace('^0','',regex=True)
    df['TEL']= df['TEL'].replace('[a-zA-Z]','',regex=T
    rue)
    df['TEL']= df['TEL'].replace(' ','',regex=True)'''
    
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
        
    df['Telefono']= df['Telefono'].astype('str')
    
    #df= agrega_caracteristica(df)
    df['Envío Telefono']= 'NO ENVIADO'
    print(df['Envío Telefono'])
    #df['Envío CEL']= 'NO ENVIADO'
    return df

def envio(msg, df, i):
    if (pd.isnull(df['Telefono'][i]) == True) or (len(df['Telefono'][i])== 0):
        df['Envío Telefono'][i]= 'NO ENVIADO'
    
    else:
        try:
            telefono = '+549'+str(df['Telefono'][i])
            send_msj(msg,telefono,df,i,browser)
        except:
                pass
            

#Ejemplo 
def envio_msg(df):
    #df = formato_df(df)
    #df = pd.read_excel("Prueba 1.xlsx", sheet_name='Hoja1')
    print(df)
    
    #msg= df['Mensaje'].astype(str)
    #print(msg)
    #msg=msg.replace('NOMBRE','Emanuel',regex=True)    
    #print(msg)
    
    txt ="{nombre} Cursos de impresion 3D en el Polo Cientifico Tecnologico para"
     
    for i in df.index:
        txt = df['Mensaje'][i]
        #new_msg = msg.replace('NOMBRE',df['PACIENTE'][i])
        msg=txt.format(Nombre=df['Nombre'][i], Fecha=df['Fecha'][i], Edad=df['Edad'][i], Categoria=df['Categoria'][i]) 
        print(msg)
        envio(msg, df, i)
    return df

#lectura_excel(fichero)
#envio_msg(formato_df(lectura_excel()))

#modificar Telefono
'''
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
            '''
            
'''       
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
            pass'''

positivo_final = '''
Deberá comunicarse con su médico de cabecera para su seguimiento médico.'''


def envio_whatsapp(df):
    #df = formato_df(df)
    '''for i in df.index:
        txt=str(df['Mensaje'][i])
        #positivo = 'Ud. *' + str(df['PACIENTE'][i])+'* , DNI: *' + str(df['DNI'][i]) + '* se realizó la prueba para COVID-19 siendo su resultado *' + str(df['RESULTADO'][i]).upper() + '*.' + positivo_final
        #negativo= 'Ud. *' + str(df['PACIENTE'][i])+'*, DNI: *' + str(df['DNI'][i]) + '* se realizó la prueba para COVID-19 siendo su resultado *' + str(df['RESULTADO'][i]).upper() + '*.'
        
        #txt ="{nombre} Cursos de impresion 3D en el Polo Cientifico Tecnologico para {edad}, {fecha}"
        #msg=txt.format(nombre=df['Nombre'][i], Fecha=df['Fecha'][i], edad=df['Edad'][i], fecha=df['Fecha'][i], email=df['Email'][i], Categoria=df['Categoria'][i])
        
        #envio1(msg,df,i)
        envio_msg(df,i)
        
        #envio1(positivo,negativo,df,i)
        
        #envio2(positivo,negativo,df,i)
        print(str(i) + ' de ' + str(len(df)))
        #bar(int(i),int(len(df)))
        #MuestraAvance(int(i))'''
    envio_msg(df)
    return df

def guardar_excel(df):
    folder='Envios/'
    time = datetime.now()
    t= time.strftime("%Y-%m-%d %H-%M-%S")
    df['Mensaje']= df['Mensaje'].replace('{Nombre}','Nombre',regex=True)
    df['Mensaje']= df['Mensaje'].replace('{Categoria}','Categoria',regex=True)
    df['Mensaje']= df['Mensaje'].replace('{Edad}','Edad',regex=True)
    df['Mensaje']= df['Mensaje'].replace('{Fecha}','Fecha',regex=True)
        
    df.to_excel(folder+'Enviados '+t+'.xlsx', sheet_name='Enviados')