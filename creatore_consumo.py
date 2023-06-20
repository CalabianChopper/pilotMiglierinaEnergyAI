# -*- coding: utf-8 -*-
"""
Created on Tue May 11 18:09:05 2021

@author: user
"""

import csv
import random

mese = 1
giorno = 1
ora = 0
#frigo_a = 0.828
#frigo_b = 0.835
#lavatrice_a = 0.820
#luci = 0.012
#lavastoviglie = 0.780

with open('esempio_di_consumo.csv', mode='w') as csv_file:
    fieldnames = ['month', 'day', 'hour', 'kw']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for mese in range(1, 13):
        if (mese == 2):
            giorno_max = 29
        elif (mese == 11 or mese == 4 or mese == 6 or mese == 9):
            giorno_max = 31
        else:
            giorno_max = 32
        for giorno in range (1, giorno_max):
            for ora in range (0, 24):
                if ora in range (0, 8):
                    kw = 1.600 + (0.100)*random.random()
                elif ora in range(8, 10):
                    kw = 1.650 + (0.150)*random.random()
                elif ora in range (10, 14):
                    kw = 1.600 + (0.100)*random.random()
                elif ora in range (14, 15):
                    kw = 1.800 + (0.400)*random.random()
                elif ora in range (15, 21):
                    kw = 1.600 + (0.100)*random.random()
                elif ora in range (21, 23):
                    kw = 3.000 + (0.400)*random.random()
                else: 
                    kw = 1.600 + (0.100)*random.random()
                writer.writerow({'month': mese, 'day': giorno, 'hour': ora, 'kw': kw})
            ora = ora + 1
        giorno = giorno + 1
    mese = mese + 1
