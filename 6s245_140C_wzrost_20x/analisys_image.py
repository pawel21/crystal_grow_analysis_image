import matplotlib.pyplot as plt
import numpy as np
from skimage.feature import canny
from scipy import misc
from scipy.ndimage import label
from scipy.ndimage import center_of_mass
from scipy.spatial import distance

from skimage.feature import corner_fast, corner_peaks, corner_orientations

img1 = misc.imread("155c012t5.tif", mode='L')

def find_radius(img):
    labels, num_features = label(img)
    location = (center_of_mass(img, labels, 1))
    print ("Object {} center of mass at {}".format(1,location))
    center_1_x, center_1_y = location1[1], location1[0]
    edges = canny(img1, sigma=8.8)

    corner_response = corner_fast(edges, threshold=0.5)
    corner_pos = corner_peaks(corner_response)

fig, axes = plt.subplots(ncols=2, figsize=(8, 4.5))
ax = axes.ravel()
ax[0] = plt.subplot(1, 2, 1)
ax[1] = plt.subplot(1, 2, 2)

ax[0].imshow(img1)
ax[0].plot(center_1_x, center_1_y, 'r^', markersize=20)
radius_array = np.zeros(len(corner_pos))

for k in range(0, len(corner_pos)):
    y, x = corner_pos[k]
    ax[0].plot(x, y, 'ro', markersize=15)
    print("x={}, y={}".format(x, y))
    radius1 = distance.euclidean((center_1_x, center_1_y), (x, y))
    radius1_um = radius1/5.66
    print("r_1 = {} um".format(radius1_um))
    radius_array[k] = radius1_um

ax[1].imshow(edges)
print(np.mean(radius_array))
print(np.std(radius_array))
plt.show()
