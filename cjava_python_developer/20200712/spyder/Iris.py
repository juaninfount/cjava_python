# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:54:14 2020

Base de datos de flores iris


@author: jnieto
"""

import  numpy as np
import pandas as pd

iris = pd.read_csv('datasets_19_420_Iris.csv')
print(iris.head())
# sepalo: base del caliz de la flor
# petalo: parte de una flor
    
iris = iris.drop('Id',axis=1)

# analizamos los datos 
print('Información del dataset')
print(iris.info()) #tipos de datos usados
print(iris.describe()) # describir datos
print(iris.groupby('Species').size()) # describir datos

import matplotlib.pyplot as plt

fig = iris[iris.Species == 'Iris-setosa'].plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', color='blue', label='Setosa')
iris[iris.Species == 'Iris-versicolor'].plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', color='green', label='Versicolor', ax=fig)
iris[iris.Species == 'Iris-virginica'].plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', color='red', label='Virginica', ax=fig)

fig.set_xlabel('Sepalo - Longitud')
fig.set_ylabel('Sepalo - Ancho')
fig.set_title('Grafica 1')
plt.show()

fig = iris[iris.Species == 'Iris-setosa'].plot(kind='scatter', x='PetalLengthCm', y='PetalWidthCm', color='blue', label='Setosa')
iris[iris.Species == 'Iris-versicolor'].plot(kind='scatter', x='PetalLengthCm', y='PetalWidthCm', color='green', label='Versicolor', ax=fig)
iris[iris.Species == 'Iris-virginica'].plot(kind='scatter', x='PetalLengthCm', y='PetalWidthCm', color='red', label='Virginica', ax=fig)
fig.set_xlabel('Pétalo - Longitud')
fig.set_ylabel('Pétalo - Ancho')
fig.set_title('Pétalo Longitud vs Ancho')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression # modelo lineal
from sklearn.svm import SVC  # modelo de soporte de vectores
from sklearn.neighbors import KNeighborsClassifier  # 
from sklearn.tree import DecisionTreeClassifier 

X = np.array(iris.drop(['Species'],1))
Y = np.array(iris['Species']) # sirve para el target

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)

# modelo de regresion logistica
alg = LogisticRegression()
alg.fit(X_train,Y_train)   # entrenamiento
Y_pred = alg.predict(X_test) # prediccion
print(alg.score(X_train, Y_train)) 

# Modelo de maquinas de vectores de soporte
alg = SVC()
alg.fit(X_train, Y_train)
Y_pred = alg.predict(X_test)
print(alg.score(X_train, Y_train))

# modelo de vecinos mas cercanos
alg = KNeighborsClassifier(n_neighbors=5)
alg.fit(X_train, Y_train)
Y_pred = alg.predict(X_test)
print(alg.score(X_train, Y_train))

# modelo de arboles de decision
alg = DecisionTreeClassifier()
alg.fit(X_train, Y_train)
Y_pred = alg.predict(X_test)
print(alg.score(X_train, Y_train))


