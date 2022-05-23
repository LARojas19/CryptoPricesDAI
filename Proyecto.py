# -*- coding: utf-8 -*-
"""
Created on Thu May 19 12:06:36 2022

@author: dai
"""
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
datos=pd.read_csv('D:\DAI\Proyecto\crypto_prices.csv')
nuevo = datos.sort_values('Unnamed: 0', ascending=False)
valores = nuevo.groupby(['ticker'])
dicTicker={}




"""
1. ¿Qué precio máximo alcanzó cada criptomoneda?
# ya
2. ¿Qué precio va tomando por día tal criptomoneda?
# ya casi
3. ¿Cuál es la criptomoneda que se ha mantenido por varios días al mismo precio?

4. ¿Cuáles son las fechas que se han extraído mayor número de monedas?
# cambiar?
5. ¿Cuál es la criptomoneda que ha tenido un precio más alto en el mercado?

6. ¿Cuál es la criptomoneda que ha tenido un precio más bajo en el mercado?

7. ¿Qué moneda ha tenido una mejor tendencia en el mercado?

8. ¿Cuál es el precio de cada moneda desde su primer registro hasta su último?
(Pueden ser los años que estuvo activo en el mercado)
# deberia salir
9. ¿Cuántas monedas salieron por moneda en cada criptomoneda?
# cambiarla
10. ¿Cuál es el precio promedio por cada mes de tal criptomoneda?
# ya
11. ¿Valía la pena invertir con tal moneda?
# ya casi
12. ¿Cuál es la tendencia de las criptomonedas por año?
# ya casi
"""


#%%
# print(datos.columns)

valores = nuevo.groupby(['ticker'])
print(valores)
for tick,ticker in valores:
    print(tick)
    print(ticker)
# print(preciosCripto)

#%%
"1. ¿Qué precio máximo alcanzó cada criptomoneda?"

def muestrameMaxPrecioCripto():
    max = datos.groupby('ticker')['High'].max().sort_values(ascending=False)
    max[3:20].plot(kind = "bar")

muestrameMaxPrecioCripto()
#%%
"2. ¿Con qué precio empiezan tal cripto moneda? ¿Qué precio va tomando por día?"

def graficameCripto(nombreCripto):
    valores = nuevo.groupby(['ticker'])
    for tick, ticker in valores:
        if tick == nombreCripto:
            preciosCripto = ticker['Close']
    print(preciosCripto.)
    # plt.plot(range(),preciosCripto, 'r')
    plt.xlabel('Dias')
    plt.ylabel('Precio')
    plt.title('Comportamiento de la criptomoneda: ' + nombreCripto)

graficameCripto('BTC')

#%%
def graficameCripto(nombreCripto):
    valores = nuevo.groupby(['ticker'])
    for tick, ticker in valores:
        if tick == nombreCripto:
            preciosCripto = ticker
    preciosCripto = preciosCripto['Close']
    nuevoD = pd.DataFrame(preciosCripto).to_numpy()
    
    print(type(nuevoD))
    plt.plot(nuevoD, 'r')
    plt.xlabel('Dias')
    plt.ylabel('Precio')
    plt.title('Comportamiento de la criptomoneda: ' + nombreCripto)

graficameCripto('BTC')
#%%
"4. ¿Cuáles son las fechas que se han extraído mayor número de monedas?"
aVer=datos.groupby('Date')['Volume'].sum().sort_values(ascending=False)
print(aVer.head(1))




#%%
"9. ¿Cuántas monedas salieron en promedio por cada criptomoneda?"






#%%
"10. ¿Cuál es el precio promedio por cada mes de tal criptomoneda en tal año?"


def promedioAho (aho, nombreCripto,datos):
    valores = datos.groupby('ticker')
    for tick, ticker in valores:
        if (tick == nombreCripto):
            nuevoC = ticker
    criptoDatos = nuevoC[['Date', 'High']]
    
    meses={}
    datos = criptoDatos.to_numpy()
    for i in range(len(datos)):
        fecha = datos[i][0]
        valor = datos[i][1]
        if fecha[8:] == aho:
            print('entre')
            try:
                if(meses[fecha[0:3]] != 0):
                    meses[fecha[0:3]].update(valor)
            except:
                meses[fecha[0:3]] = valor
    print(meses)
    
promedioAho(2021,'CANDY',datos)




#%%10
"10. ¿Cuál es el precio promedio por cada mes de tal criptomoneda en tal año?"
def noCero(arr):
    if arr[0]!=0:
        return arr[1]/arr[0]
    else:
        return 'na'


def promedioAho (aho, nombreCripto,datos):
    valores = datos.groupby('ticker')
    for tick, ticker in valores:
        if (tick == nombreCripto):
            nuevoC = ticker
    criptoDatos = nuevoC[['Date', 'Close']]
    
    # meses={}
    meses={'Jan':[0,0],
            'Feb':[0,0],
            'Mar':[0,0],
            'Apr':[0,0],
            'May':[0,0],
            'Jun':[0,0],
            'Jul':[0,0],
            'Aug':[0,0],
            'Sep':[0,0],
            'Oct':[0,0],
            'Nov':[0,0],
            'Dec':[0,0]}
    datosN = criptoDatos.to_numpy()
    for i in range(len(datosN)):
        fecha = datosN[i][0]
        # print(fecha)
        valor = datosN[i][1]
        if fecha[8:] == str(aho):
            meses[fecha[0:3]][0]=meses[fecha[0:3]][0] + 1 
            meses[fecha[0:3]][1]=meses[fecha[0:3]][1] + valor
    mesesProm= [noCero(meses[i]) for i in meses.keys()]
    graf = pd.DataFrame(mesesProm,meses.keys())
    # print(graf)
    # graf.plot(kind='scatter')
    print(mesesProm)
    
    
promedioAho(2022,'BTC',datos)


#%% 
"11. ¿Valía la pena invertir con tal moneda?"

def valiaLaPenaInvertir(nombreCripto):
    valores = datos.groupby(['ticker'])
    for tick, ticker in valores:
        if tick == nombreCripto:
            promC =  ticker['Open'].mean()
            promedioCripto = (ticker['High'] + ticker['Open'] + ticker['Low'])/3  
    dfProm = pd.DataFrame(promedioCripto)
    arr = dfProm.to_numpy()
    cont = 0
    for i in arr:
        if i > promC:
            cont+=1
    print(cont)       
    print(len(arr)/2)
    return cont > (len(arr)/2)
    

print(valiaLaPenaInvertir('BTC'))



#%%
















