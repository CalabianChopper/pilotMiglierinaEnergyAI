"""
Created on: 08/05/21 15:01

Last Update: 11/05/21 19:56

@authors: Eng Francesco Chiodo & PhD Pietro Hiram Guzzi
"""

#import necessary libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import plotly.express as px


#Read production energy CSV data
url1 = 'child1.csv'
d1 = pd.read_csv(url1)
#Print dataset dimension and first day (01/01/20) datas
print('Consumption dataset dimension')
print(d1.shape)
print('First 24 elements')
print(d1.head(24))
#Print description of all dataset values
print('Data description, mean, std ecc.')
print(d1.describe())


#Read other CSV data 
url2 = 'child2.csv'
d2 = pd.read_csv(url2)
url3 = 'child3.csv'
d3 = pd.read_csv(url3)
url4 = 'child4.csv'
d4 = pd.read_csv(url4)
url5 = 'nochild1.csv'
d5 = pd.read_csv(url5)
url6 = 'nochild2.csv'
d6 = pd.read_csv(url6)
url7 = 'nochild3.csv'
d7 = pd.read_csv(url7)
url8 = 'comm1.csv'
d8 = pd.read_csv(url8)
url9 = 'comm2.csv'
d9 = pd.read_csv(url9)
url10 = 'comm3.csv'
d10 = pd.read_csv(url10)
dati = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]
print('Tutti i dati sono stati caricati')


#Delete NaN row from the datasets
eliminaNaN1 = d1.dropna(axis = 0)
eliminaNaN2 = d2.dropna(axis = 0)
eliminaNaN3 = d3.dropna(axis = 0)
eliminaNaN4 = d4.dropna(axis = 0)
eliminaNaN5 = d5.dropna(axis = 0)
eliminaNaN6 = d6.dropna(axis = 0)
eliminaNaN7 = d7.dropna(axis = 0)
eliminaNaN8 = d8.dropna(axis = 0)
eliminaNaN9 = d9.dropna(axis = 0)
eliminaNaN10 = d10.dropna(axis = 0)
print ('Dati NaN eliminati correttamente')


#Data visualization with plot
plt.rcParams["figure.autolayout"] = True
d1.set_index('kw')
plt.show()

#Initialize KMeans object specifying the number of desired clusters
kmeans = KMeans(n_clusters=3)

# learning the clustering from the input date
kmeans.fit(d1, d2, d3, d4, d5, d6, d6, d7, d8, d9, d10)

# output the labels for the input data
print(kmeans.labels_)



