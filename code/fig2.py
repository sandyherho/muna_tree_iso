#!/usr/bin/env python
"""
fig2.py

Plotting 3 raw d18O ts into a single panel

SHSH <sandy.herho@ucr.edu>
08/26/23
"""

# import libs & settings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 700
plt.style.use("ggplot")

# read data
tg01c = pd.read_csv("../data/raw_data/cleantg01c.csv")[["date", "o18"]]
tg11a = pd.read_csv("../data/raw_data/cleantg11a.csv")[["date", "o18"]]
mun63 = pd.read_csv("../data/raw_data/cleanmun63.csv")[["date", "o18"]]

# descriptive stats
## each series
median = [tg01c["o18"].quantile(.5), tg11a["o18"].quantile(.5), mun63["o18"].quantile(.5)]
median = np.array(median).round(2)
print("median of each series: ", median)

tg01c_ci = tg01c["o18"].quantile([2.5/100, 97.5/100]).to_numpy()
tg11a_ci = tg11a["o18"].quantile([2.5/100, 97.5/100]).to_numpy()
mun63_ci = mun63["o18"].quantile([2.5/100, 97.5/100]).to_numpy()
ci = np.vstack([tg01c_ci, tg11a_ci, mun63_ci]).round(2)
print("ci of each series: ", ci)

## anomaly
var_tg01c = tg01c["o18"].to_numpy() - tg01c["o18"].mean()
var_tg11a = tg11a["o18"].to_numpy() - tg11a["o18"].mean()
var_mun63 = mun63["o18"].to_numpy() - mun63["o18"].mean()

med_var = np.round(np.array([np.median(var_tg01c), np.median(var_tg11a), np.median(var_mun63)]), 2)
print("median of anomaly: ", med_var)

upper = np.array([np.percentile(var_tg01c, 97.5), np.percentile(var_tg11a, 97.5), np.percentile(var_mun63, 97.5)]).round(2)
lower = np.array([np.percentile(var_tg01c, 2.5), np.percentile(var_tg11a, 2.5), np.percentile(var_mun63, 2.5)]).round(2)
print("upper ci anomaly: ", upper)
print("lower ci anomaly: ", lower)

plt.plot(tg01c["date"], tg01c["o18"], color="#eb4034",
        ls="--", label="tg01c", alpha=0.85);
plt.plot(tg11a["date"], tg11a["o18"], color="#31b561",
         ls="--", label="tg11a", alpha=0.85);
plt.plot(mun63["date"], mun63["o18"], color="#23529e", 
         ls="--", label="mun6.3", alpha=0.85);
x = [1663]
y = [27.33]
plt.errorbar(x,y, yerr=0.8, fmt="o", color="k", capsize=4)
plt.ylabel("$\delta^{18}$O [‰, VSMOW]", size=16);
plt.xlabel("time [years CE]", size=16);
plt.ylim(18, 33);
plt.xlim(1650, 2000);
plt.legend();
plt.savefig("../figs/fig2.png");
