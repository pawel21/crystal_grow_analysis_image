import fnmatch
import matplotlib.pyplot as plt
import numpy as np
import os
from skimage.feature import canny
from scipy import misc
from scipy.ndimage import label
from scipy.ndimage import center_of_mass
from scipy.spatial import distance


list_file = os.listdir('.')
list_tif_file = []
for f in list_file:
    print(f)
    if fnmatch.fnmatch(f, '*.tif'):
        list_tif_file.append(f)

img = misc.imread(list_tif_file[0], mode='L')

fig, ax1 = plt.subplots()
threshold = np.mean(img)
img[img < threshold] = 0
img[img >= threshold] = 1
ax1.imshow(img)

def plots_image():
    fig1, axes = plt.subplots()

plt.show()