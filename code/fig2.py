#!/usr/bin/env python

"""
fig2.py

Create ts stackplot for 3 cores

SHSH <sandy.herho@email.ucr.edu>
08/25/23
"""

# import libs & settings
import pyleoclim as pyleo
import pandas as pd
import matplotlib.pyplot as plt
import warnings
plt.rcParams['figure.figsize'] = [20, 15]
plt.rcParams["figure.dpi"] = 700
warnings.filterwarnings("ignore")


# read data
df1 = pd.read_csv("../data/raw_data/cleantg01c.csv") 
df2 = pd.read_csv("../data/raw_data/cleantg11a.csv")
df3 = pd.read_csv("../data/raw_data/cleanmun63.csv")

# create mts pyleo obj
tg01c = pyleo.Series(time =  df1['date'], value = df1["o18"],
                  time_name = 'Year', value_name = '$\delta^{18}$O of tg01c',
                  time_unit = 'CE', value_unit = '‰, VSMOW')

tg11a = pyleo.Series(time =  df2['date'], value = df2["o18"],
                  time_name = 'Year', value_name = '$\delta^{18}$O of tg11a',
                  time_unit = 'CE', value_unit = '‰, VSMOW')

mun63 = pyleo.Series(time =  df3['date'], value = df3["o18"],
                  time_name = 'Year', value_name = '$\delta^{18}$O of mun63',
                  time_unit = 'CE', value_unit = '‰, VSMOW')

mun = pyleo.MultipleSeries([tg01c, tg11a, mun63], name="Muna $\delta^{18}O_c$ time series")

# savefig
mun.stackplot()
plot = plt.gcf()
plot.savefig("../figs/fig2.png")