#!/usr/bin/env python
"""
fig1.py

Plot map of study location

SHSH <sandy.herho@email.ucr.edu>
08/28/23
"""
# import libs & settings
import pandas as pd
import matplotlib.pyplot as plt
import pygmt
import warnings
plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = [20, 10]
warnings.filterwarnings("ignore")

# plot map
fig = pygmt.Figure()
fig.basemap(region=[93, 143, -20, 20], projection="M15c", frame=True)
fig.coast(land="black", water="skyblue")
fig.plot(x=123, y=-5.3, style="c0.4c", cmap="red", pen="black")
fig.savefig("../figs/fig1.png", dpi=700)
