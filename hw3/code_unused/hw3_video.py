# This file generates video of bucket's motion from the data
# import packages
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

# load data from file
cam = loadmat('datasets/cam1_1.mat')['vidFrames1_1']
idx = cam.shape

plt.figure(1)

for i in range(idx[3]):
    plt.imshow(cam[:,:,:,i])
    plt.pause(0.001)
    
plt.show()