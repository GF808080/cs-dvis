# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 10:27:46 2016

@author: sentinel
"""

import pandas as pd
from bokeh.charts import Histogram
from bokeh.charts import defaults, vplot, hplot, show, output_file
import matplotlib.pyplot as plt

seattle = pd.read_csv('seattle_incidents_summer_2014.csv', parse_dates =[7,8,9])
sf = pd.read_csv('sanfrancisco_incidents_summer_2014.csv', parse_dates =[4])

"""
plot crimes
"""

seattle['Summarized Offense Description'].value_counts().plot(kind = 'bar')
plt.xticks(rotation=70)
plt.title('Seattle Crime: Summer 2014')

sf['Descript'].value_counts().plot(kind = 'bar')
plt.xticks(rotation = 70)
plt.title('San Fancisco Crime: Summer 2014')

"""
Crimes by day of week
"""
def day_map(daynumber):
    if daynumber == 0:
        return "Mon"
    elif daynumber == 1:
        return "Tues"
    elif daynumber == 2:
        return "Wed"
    elif daynumber == 3:
        return "Thurs"
    elif daynumber == 4:
        return "Fri"
    elif daynumber == 5:
        return "Sat"
    elif daynumber == 6:
        return "Sun"
seattle['DayOfWeek'] = seattle['Occurred Date or Date Range Start'].dt.dayofweek
seattle['DayOfWeek'] = seattle.DayOfWeek.apply(lambda x: day_map(x))
seattle.DayOfWeek.value_counts()

seattle['DayOfWeek'].value_counts().plot(kind = 'bar')
plt.xticks(rotation=70)
plt.title('Seattle Crimes By Day: Summer 2014')

sf['DayOfWeek'].value_counts().plot(kind = 'bar')
plt.xticks(rotation = 70)
plt.title('San Fancisco Crimes By Day: Summer 2014')


"""
characterize crimes
"""
theft = ['THEFT', 'STOLEN', 'FRAUD', 'COUNTERFEIT', 'PICPOCKET', 'BURGLARY', \
'SNATCH', 'EMBEZZLE', 'PROPERTY', 'BURGLARY']
 
weapons = ['WEAPON', 'FIREARM', 'GUN', 'KNIFE']

threatBehavior =['PROWL','THREATS', 'DSPUTE',  'CONDUCT', 'TRESPASS', \
'BEHAVIOR', "SUSPICIOUS"]

traffic = ['TRAFFIC']

sexual = ['PROSTITUTION', 'PORNOGRAPHY', 'INDECENT', 'SEXUAL', 'RAPE']

transactions = ['WARRANT', 'ORDER', 'REPORT', 'BIAS', 'FIREWORK', \
'OBSTRUCT', 'NUISANCE', 'CONDUCT', 'CODE', 'PAROLE']

OFelonies =['DUI', 'HOMICIDE', 'IMPRISONMENT', 'SERIOUS',\
 'ASSAULT', 'ABUSE']
 
def to_type(x):
    if x == 1:
        return 'theft'
    elif x ==2:
        return 'weapons'
    elif x == 3:
        return 'threatBehavior'
    elif x == 4:
        return 'traffic'
    elif x ==5:
        return 'sexual'
    elif x ==6:
        return 'transactions'
    elif x == 7:
        return 'OFelonies'
    else:
        return "other"
 
seattle['theft']=seattle['Summarized Offense Description'].str.contains("|".join(theft))*1
seattle['weapons']=seattle['Summarized Offense Description'].str.contains("|".join(weapons))*2
seattle['threatBehavior']=seattle['Summarized Offense Description'].str.contains("|".join(threatBehavior))*3
seattle['traffic']=seattle['Summarized Offense Description'].str.contains("|".join(traffic))*4
seattle['sexual']=seattle['Summarized Offense Description'].str.contains("|".join(sexual))*5
seattle['transactions']=seattle['Summarized Offense Description'].str.contains("|".join(transactions))*6
seattle['OFelonies']=seattle['Summarized Offense Description'].str.contains("|".join(OFelonies))*7
seattle['sumofallfears'] = seattle['theft']+seattle['weapons']+seattle['threatBehavior']+seattle['traffic']+seattle['sexual']+seattle['transactions']+seattle['OFelonies']
seattle['Other'] = seattle.sumofallfears.apply(lambda x: 8 if x == 0 else  0)
seattle['BroadCrimeCat'] =seattle['sumofallfears'] = seattle['theft']+seattle['weapons']+seattle['threatBehavior']+seattle['traffic']+seattle['sexual']+seattle['transactions']+seattle['OFelonies']+seattle['Other']
seattle['BroadCrimeCat'] = seattle.BroadCrimeCat.apply(lambda x: to_type(x))

sf['theft'] = sf.Category.str.contains("|".join(theft))*1
sf['weapons'] = sf.Category.str.contains("|".join(weapons))*2
sf['threatBehavior'] = sf.Category.str.contains("|".join(threatBehavior))*3
sf['traffic'] = sf.Category.str.contains("|".join(traffic))*4
sf['sexual'] = sf.Category.str.contains("|".join(sexual))*5
sf['transactions'] = sf.Category.str.contains("|".join(transactions))*6
sf['OFelonies'] = sf.Category.str.contains("|".join(OFelonies))*7

sf['sumofallfears'] = sf['theft']+sf['weapons']+sf['threatBehavior']+sf['traffic']+sf['sexual']+sf['transactions']+sf['OFelonies']
sf['Other'] =sf.sumofallfears.apply(lambda x: 8 if x == 0 else  0)
sf['BroadCrimeCat'] = sf['theft']+sf['weapons']+sf['threatBehavior']+sf['traffic']+sf['sexual']+sf['transactions']+sf['OFelonies']+sf['Other']
sf['BroadCrimeCat'] =sf['BroadCrimeCat'].apply(lambda x: to_type(x))
