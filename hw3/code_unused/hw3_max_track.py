# import packages
import numpy as np
import matplotlib.pyplot as plt

def max_track(y):
    '''
    Extract the trajectory of an object, by finding maximum intensity in each image
    y: (NUMPY ARRAY) data of a set of images w/ background treatment
    Return value
    trajx: (NUMPY ARRAY) (Dim: frames*1) the x-trajectory of the object
    trajy: (NUMPY ARRAY) (Dim: frames*1) the y-trajectory of the object
    '''
    # grab dimensions of data
    idx = y.shape # idx[0]: height, idx[1]: width
    
    if len(idx) == 2: # image
        
        max_idx = np.unravel_index(y.argmax(), idx)
        trajx = max_idx[1]
        trajy = max_idx[0]
        
    elif len(idx) == 3: # video
        
        trajx = np.zeros((idx[-1],1))
        trajy = np.zeros((idx[-1],1))
        
        for i in range(idx[-1]): # i: frame number
            
            max_idx = np.unravel_index(y[:,:,i].argmax(), idx[:-1])
            trajx[i] = max_idx[1] # Note: the order is reversed for image
            trajy[i] = max_idx[0]
        
    else:
        trajx = 0
        trajy = 0
        print('Error: Wrong dimensions. Input data must be a video or image in grayscale. ')
    
    return trajx, trajy