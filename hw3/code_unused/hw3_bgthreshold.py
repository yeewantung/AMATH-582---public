# This file subtracts background from image/video by thresholding. 
# import packages
import numpy as np

# background thresholding
def bg_threshold(y):
    '''
    Subtract background by thresholding
    y: (NUMPY ARRAY) data of a set of images
    '''
    
    # grab dimensions of data
    idx = y.shape
    if len(idx) == 2: # image
        thres = y.mean()
        yn = y.copy()
        yn[yn <= thres] = 0
        
    elif len(idx) == 3: # video
        
        yn = np.zeros(idx)
        # set elements to zero if below threshold
        for i in range(idx[-1]):
            item = y[:,:,i].copy()
            thres = item.mean() # set up threshold
            item[item <= thres] = 0
            yn[:,:,i] = item.copy()
        
    else:
        yn = y
        print('Error: Wrong dimensions. Input data must be a video or image in grayscale.')
        
    return yn