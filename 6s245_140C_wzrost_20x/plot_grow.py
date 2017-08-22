import matplotlib.pyplot as plt
import numpy as np

from scipy.optimize import curve_fit

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


def poly1(x, a, b):
    return a*x + b


radius1 = [65.3, 75.5, 95.5, 108.47, 128, 140, 160]
time = [5.32, 301.78, 601.95, 901.98, 1200.60, 1500.76, 1800.96]
time = np.array(time)/60.0
plt.plot(time, radius1, 'bo', markersize=15)


popt, pcov = curve_fit(poly1, time, radius1)
a = popt[0]
b = popt[1]
error = np.abs(np.diag(pcov) ** 0.5)
da = error[0]
db = error[1]
x = np.linspace(0, 32, 200)
y = a*x + b
plt.plot(x, y, 'r-')
plt.grid(True)
plt.xlabel("czas [min]")
plt.ylabel("promień [$\mu$m]")
plt.show()
