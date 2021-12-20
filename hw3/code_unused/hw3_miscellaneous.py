# import packages
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

# load RGB original file for test
cam11 = loadmat('datasets/cam1_1.mat')['vidFrames1_1']

# determine the order of R,G,B channels
test = np.zeros(cam11[:,:,0,4].shape, dtype = np.uint8)
test2 = np.array([test, cam11[:,:,1,4], test])
test2 = np.moveaxis(test2, 0, -1)
plt.figure(1)
plt.imshow(test2)
plt.show()

# Conclusion: The order of channels of data is confirmed to be RGB.