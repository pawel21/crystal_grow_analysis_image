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


radius1 = [154.2, 166.6, 180.03, 192.7]
time = [4.71, 241.33, 481.58, 721.57]
time = np.array(time)/60.0
plt.errorbar(time, radius1, yerr=[2.9, 4.9, 4.2, 5.2], fmt='o',
 markersize=15)


popt, pcov = curve_fit(poly1, time, radius1)
a = popt[0]
b = popt[1]
error = np.abs(np.diag(pcov) ** 0.5)
da = error[0]
db = error[1]
x = np.linspace(0, 730/60.0, 200)
y = a*x + b
plt.plot(x, y, 'r-')
plt.grid(True)
plt.xlabel("czas [min]")
plt.ylabel("promień [$\mu$m]")
plt.show()
