# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 12:57:12 2020

@author: jnieto
"""

import  numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression # modelo lineal
from sklearn.svm import SVC  # modelo de soporte de vectores
from sklearn.neighbors import KNeighborsClassifier  # 
from sklearn.tree import DecisionTreeClassifier 

###################### importando data #######################
df_test  = pd.read_csv('test.csv')
df_train = pd.read_csv('train.csv')

# primeras lineas de los dataframes
print(df_test.head())
print(df_train.head())

#Verifico la cantidad de datos que hay en los dataset
print('Cantidad de datos:')
print(df_train.shape)
print(df_test.shape)

#Verifico el tipo de datos contenida en ambos dataset
print('Tipos de datos:')
print(df_train.info())
print(df_test.info())

#Verifico los datos faltantes de los dataset
print('Datos faltantes:')
print(pd.isnull(df_train).sum())
print(pd.isnull(df_test).sum())

#Verifico las estadísticas del dataset
print('Estadísticas del dataset:')
print(df_train.describe())
print(df_test.describe())

#Cambio los datos de sexos en números
df_train['Sex'].replace(['female','male'],[0,1],inplace=True)
df_test['Sex'].replace(['female','male'],[0,1],inplace=True)

#Cambio los datos de embarque en números
df_train['Embarked'].replace(['Q','S', 'C'],[0,1,2],inplace=True)
df_test['Embarked'].replace(['Q','S', 'C'],[0,1,2],inplace=True)

#Reemplazo los datos faltantes en la edad por la media de esta columna
print(df_train["Age"].mean()) # media de la edad
print(df_test["Age"].mean())

promedio = 30 # los NAN de edades reemplazar por promedios
df_train['Age'] = df_train['Age'].replace(np.nan, promedio)
df_test['Age'] = df_test['Age'].replace(np.nan, promedio)

#Creo varios grupos de acuerdo a bandas de las edades
#Bandas: 0-8, 9-15, 16-18, 19-25, 26-40, 41-60, 61-100
bins = [0, 8, 15, 18, 25, 40, 60, 100]
names = ['1', '2', '3', '4', '5', '6', '7']
df_train['Age'] = pd.cut(df_train['Age'], bins, labels = names)
df_test['Age']  = pd.cut( df_test['Age'], bins, labels = names)

# Se elimina la columna de "Cabin" ya que tiene muchos datos perdidos
df_train.drop(['Cabin'], axis = 1, inplace=True)
df_test.drop(['Cabin'], axis = 1, inplace=True)

# eliminar columnas innecesarias para el calculo
#Elimino las columnas que considero que no son necesarias para el analisis
df_train = df_train.drop(['PassengerId','Name','Ticket'], axis=1)
df_test = df_test.drop(['Name','Ticket'], axis=1)

#Se elimina las filas con los datos perdidos
df_train.dropna(axis=0, how='any', inplace=True)
df_test.dropna(axis=0, how='any', inplace=True)

#Verifico los datos
print(pd.isnull(df_train).sum())
print(pd.isnull(df_test).sum())

# despues de procesar data
print(df_train.shape)
print(df_test.shape)
print(df_test.head())
print(df_train.head())

#Separo la columna con la información de los sobrevivientes
X = np.array(df_train.drop(['Survived'], 1)) # {0 or ‘index’, 1 or ‘columns’}
Y = np.array(df_train['Survived'])

#Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

##Regresión logística
logreg = LogisticRegression()
logreg.fit(X_train, Y_train)
Y_pred = logreg.predict(X_test)
print('Precisión Regresión Logística:')
print(logreg.score(X_train, Y_train))

# Precision por maquina de vectores
svc = SVC()
svc.fit(X_train, Y_train)
Y = pred = svc.predict(X_test)
print('Precision por soporte de vectores')
print(svc.score(X_train, Y_train))

##K neighbors
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
print('Precisión Vecinos más Cercanos:')
print(knn.score(X_train, Y_train))

##########PREDICCIÓN UTILIZANDO LOS MODELOS##########
ids = df_test['PassengerId']

## Regresion lineal

prediccion_lin =  linear_model.LinearRegression(df_test.drop('PassengerId', axis = 1))
out_knn = pd.DataFrame({'PassengerId':ids, 'Survived':prediccion_lin })
print('Regresion lineal')
print(out_knn.head())

## Predicción Regresión Logística
prediccion_logreg = logreg.predict(df_test.drop('PassengerId', axis=1))
out_logreg = pd.DataFrame({ 'PassengerId' : ids, 'Survived': prediccion_logreg })
print('Predicción Regresión Logística:')
print(out_logreg.head())

## Support Vector Machines
prediccion_svc = svc.predict(df_test.drop('PassengerId', axis=1))
out_svc = pd.DataFrame({ 'PassengerId' : ids, 'Survived': prediccion_svc })
print('Predicción Soporte de Vectores:')
print(out_svc.head())

## K neighbors
prediccion_knn = knn.predict(df_test.drop('PassengerId', axis=1))
out_knn = pd.DataFrame({ 'PassengerId' : ids, 'Survived': prediccion_knn })
print('Predicción Vecinos más Cercanos:')
print(out_knn.head())