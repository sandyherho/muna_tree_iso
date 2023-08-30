#!/usr/bin/env python

"""
ks_test.py

KS test

SHSH <sandy.herho@ucr.edu>
08/26/23
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp

# Set plot settings
plt.rcParams["figure.dpi"] = 700
plt.style.use('ggplot')

# Function to perform KS test and print results
def perform_ks_test(pre, post, label):
    test = ks_2samp(pre, post)
    print(f"=== {label} ===")
    print(f"Dmax = {test[0]:.3f}")
    print(f"p-value = {test[1]:.3f}")
    print("===============================")
    return test

# Read data
df = pd.read_csv("../../data/processed_data/PhydaNino34_high_pass.csv").set_index("year")
df.head()


# Calculate and print KS test for two time periods
pre = df.loc["1680":"1850"]["nino34"].dropna().to_numpy()
post = df.loc["1850":]["nino34"].dropna().to_numpy()
perform_ks_test(pre, post, "1680 - 1849 vs 1850 - 1995")

x_pre = np.sort(pre)
y_pre = 1. * np.arange(len(pre)) / (len(pre) - 1)
x_post = np.sort(post)
y_post = 1. * np.arange(len(post)) / (len(post) - 1)

# Plotting the ECDF for fig4a with improved layout
plt.plot(x_pre, y_pre, label= 'Pre-Industrial (1680 - 1849)', color="#3f4ce0")
plt.plot(x_post, y_post, label='Post-Industrial (1850 - 1995)', color="#eb4034")
plt.ylabel('Empirical CDFs', fontsize='16')
plt.xlabel("Niño 3.4 SST index anomaly", fontsize=16)
plt.legend()
plt.tight_layout()  # Adjust the layout for a tighter plot

# Save fig5a with labels visible
plt.savefig('../../figs/fig5a.png', dpi=700, bbox_inches='tight')


# Calculate and print KS test for multiple time periods
pre_periods = [
    df.loc[f"{1695 + i * 25}":f"{1719 + i * 25}"]["nino34"].dropna().to_numpy()
    for i in range(11)
]
post = df.loc["1970":]["nino34"].dropna().to_numpy()

for i, pre_period in enumerate(pre_periods):
    label = f"{1695 + i * 25} - {1719 + i * 25} vs 1970 - 1995"
    perform_ks_test(pre_period, post, label)

# Improved color choices for plotting
colors = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
    "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "red"
]

# Plotting with adjusted figure size and layoutL
fig, ax = plt.subplots(figsize=(10, 6))

for i, pre_period in enumerate(pre_periods):
    label = f"{1695 + i * 25} - {1719 + i * 25}"
    x = np.sort(pre_period)
    y = 1. * np.arange(len(pre_period)) / (len(pre_period) - 1)
    ax.plot(x, y, label=f'Pre-Industrial ({label})', color=colors[i])

x_post = np.sort(post)
y_post = 1. * np.arange(len(post)) / (len(post) - 1)
ax.plot(x_post, y_post, label='Post-Industrial (1970 - 1995)', color="red")

ax.set_ylabel('Empirical CDFs', fontsize=16)
ax.set_xlabel("Niño 3.4 SST index anomaly""Niño 3.4 SST index anomaly", fontsize=16)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.savefig('../../figs/fig5b.png', dpi=700, bbox_inches='tight')
