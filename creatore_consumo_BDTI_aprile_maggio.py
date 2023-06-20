# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 17:01:22 2021

@author: Chiodo Francesco
Project: BDTI Pilot Miglierina Consumption Data
creator 01/05/21-30/06/21
"""

import csv
import random

mese = 1
giorno = 1
ora = 0

with open('comm3.csv', mode='w') as csv_file:
    fieldnames = ['month', 'day', 'hour', 'kw']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    for mese in range(4, 6):
        if (mese == 4):
            giorno_max = 32
        else:
            giorno_max = 31
        for giorno in range (1, giorno_max):
            for ora in range (0, 24):
                if ora in range (0, 7):
                    kw = 3.000 + (1.500)*random.random()
                elif ora in range(7, 12):
                    kw = 6.00 + (2.000)*random.random()
                elif ora in range (12, 14):
                    kw = 3.000 + (1.500)*random.random()
                elif ora in range (14, 19):
                    kw = 6.00 + (2.000)*random.random()
                elif ora in range (19, 23):
                    kw = 3.000 + (1.500)*random.random()
                else: 
                    kw = 3.000 + (1.500)*random.random()
                writer.writerow({'month': mese, 'day': giorno, 'hour': ora, 'kw': kw})
            ora = ora + 1
        giorno = giorno + 1
    mese = mese + 1
     