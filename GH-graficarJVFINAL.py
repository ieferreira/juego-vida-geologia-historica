import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import csv
from scipy.signal import argrelextrema
from scipy.signal import savgol_filter

x = []
with open('hist946.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))


x = np.asarray(x)
x = savgol_filter(x, 201, 6)
maxima = argrelextrema(x, np.greater)
minima = argrelextrema(x, np.less)
print(len(maxima))
print(len(minima))
plt.plot(x, label='Cantidad de Celdas Vivas')
plt.xlabel('Tiempo en iteraciones (aprox 0.1 segundos)')
plt.ylabel('NUMERO DE CELDAS VIVAS')
plt.title('JUEGO DE LA VIDA - EXPERIMENTO PARA GEOLOGÍA HISTÓRICA 2020-2')
plt.legend()
plt.show()