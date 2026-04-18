import matplotlib.pyplot as plt
from config.region import BBOX

def plot_heatmap(ds, var="FWI", bbox=BBOX):
    plt.figure(figuresize=(8, 8))
    ds[var].plot(cmap="inferno")
    plt.title(f"{var} Heatmap")
    plt.show()