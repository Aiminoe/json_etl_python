# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

from ast import Break
import json
from re import X
from threading import BrokenBarrierError
import requests
import numpy as np

import matplotlib.pyplot as plt

def extraer (url):
    response = requests.get(url)
    data = response.json()
    return data

def filtro_data(extraer):
    data = extraer(url)
    
    x = []
    y = []
    n = 0

    for k in range(1, 11):
        for user in data:
            if user['userId'] == k:
                if user['completed'] == True:
                    n += 1
            if user['userId'] not in x:
                x.append(user['userId'])
        y.append(n)
        n = 0

    return (x, y)
             

def graficar(filtro_data):
    x,y = filtro_data(extraer)
    fig = plt.figure()
    fig.suptitle('Titulos', fontsize=16)
    ax = fig.add_subplot()
    ax.bar(x, y)
    ax.set_ylabel('Titulos')
    ax.set_xlabel('userId')
    ax.legend()
    plt.show()          



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    extraer(url)
    filtro_data(extraer)
    
    graficar(filtro_data)

    



   
    print("FIN")

    

        