#!/usr/bin/env python

"""
plotting.py

Plot high-pass filtered d18O

SHSH <sandy.herho@email.ucr.edu>
08/26/23
"""

# import libs & settings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 700
plt.style.use("ggplot")

# read data
df = pd.read_csv("../../data/processed_data/muna_high_pass_stack.csv")

# plot
plt.plot(df["year"], df["median"], color="green");
plt.fill_between(df["year"], df["lower"], df["upper"], alpha=.25, color='green')
x = [1670]
y = [0]
plt.errorbar(x,y, yerr=0.32, fmt="o", color="k", capsize=4)
plt.xlabel('time [years CE]', size=16);
plt.ylabel('$\delta^{18}$O anomaly [‰, VSMOW]', size=16);
plt.tight_layout();
plt.savefig("../../figs/fig3.png")
