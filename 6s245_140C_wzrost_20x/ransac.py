import matplotlib.pyplot as plt
from skimage import exposure, color, feature, filters, io, measure, morphology, restoration, segmentation, util

image = io.imread('155c012t1.tif')


f, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 10))
gamma_low_val = 1.5
gamma_low = exposure.adjust_gamma(image, gamma=gamma_low_val)
#image = filters.gaussian(image, multichannel=False, sigma=4)
edges = feature.canny(color.rgb2gray(image>88), sigma=3)
ax1.imshow(edges, cmap='gray');
ax2.imshow(image>88)
plt.show()
