import pandas as pd
from string import Template
import time

'''
name="Bob"
variable="name"
text='Hey, $'+variable+"!"
print(text)
t = Template(text)
print(t.substitute(name=name))
#par="name=name"
text2="Hey {name}, there's a error!"
print(format.text2)
'''
name="Emanuel"

#text3='Hello, %s'
#prueba=text3 % name 
fichero="Prueba 1.xlsx"
df=pd.read_excel(fichero)
name2= "Nombre"
text3= "Hola, Nombre"
wrd= "Mi"
df2= pd.DataFrame({'Nombre': ['Mi nombre es Nombre', 'Yamila', 'Gonza', 'Emanuel'],
                   'Apellido': ['Arque', 'Toledo', 'Recoulat','Cresut']})

prueba= 'a'
#df2['Nombre'][0]=df2['Nombre'][0].replace(df2['Nombre'][0], name)

#print(df2['Nombre'][0].replace(df2.columns.values[0], df2[df2.columns.values[0]][1]).replace(wrd,df2[df2.columns.values[0]][2]))
print(df)

#forma 1 optimizada
tiempoInicod1 = time.time()
for i in df.index:
    print(df[df.columns.values[5]][i].replace(df.columns.values[0], str(df[df.columns.values[0]][i]))
        .replace(df.columns.values[1], str(df[df.columns.values[1]][i]))
        .replace(df.columns.values[2], str(df[df.columns.values[2]][i]))
        .replace(df.columns.values[3], str(df[df.columns.values[3]][i]))
        .replace(df.columns.values[4], str(df[df.columns.values[4]][i])))
        #.replace(df.columns.values[5], str(df[df.columns.values[5]][i])))


tiempoFincod1= time.time()
print("Forma 1: ",tiempoFincod1-tiempoInicod1) 
#forma 2 sin limite de campo


tiempoInicod2 = time.time()
for i in df.index:
    for j in range(len(df.columns.values)):
        #df[df.columns.values[5]][i]= df[df.columns.values[5]][i].replace(df.columns.values[j], str(df[df.columns.values[j]][i]))
        df.loc[i,'Mensaje']= df['Mensaje'][i].replace(df.columns.values[j], str(df[df.columns.values[j]][i]))
    print(df['Mensaje'][i])           
    #print(msg)
        #.replace(df.columns.values[5], str(df[df.columns.values[5]][i])))
tiempoFincod2= time.time()


print("Forma 1: ",tiempoFincod1-tiempoInicod1) 
print("Forma 2: ",tiempoFincod2-tiempoInicod2)
#print(df)
#print(df[df.columns.values[5]][0])
#print(df2)
#templ_string = 'Hey $name, there is a'
#Template(templ_string).substitute(name=name)



'''
fichero="Prueba 1.xlsx"
df1= pd.read_excel(fichero)

df2= pd.DataFrame({'Nombre': ['Mi nombre es Emanuel', 'Yamila', 'Gonza', 'Emanuel'],
                   'Apellido': ['Arque', 'Toledo', 'Recoulat','Cresut']})

print(df2)'''

'''
nombre="Emanuel"
apellido="Arque"
df2['Nombre']= df2['Nombre'].replace(nombre,apellido,regex=True, inplace=True)
print(df)'''

#print(df2['Nombre'][0].find("Emanuel"))


