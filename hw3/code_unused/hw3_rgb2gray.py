# This file converts a RGB image/video to grayscale. 
# import packages
import numpy as np

def rgb2gray(y):
    '''
    Turn RGB image/video into grayscale
    y: (NUMPY ARRAY) datasets for image/video
    '''
    
    # grab dimensions of data
    idx = y.shape
    
    # weights of RGB channel
    weight = np.array([0.2989, 0.5870, 0.1140])
    
    # determine whether image or video
    if len(idx) == 4: # video
        temp = np.array([np.dot(y[:,:,:,i], weight) for i in range(idx[-1])])
        yg = np.moveaxis(temp, 0, -1) # make the position consistent
        
    elif len(idx) ==3: # image
        yg = np.dot(y, weight)
        
    else:
        yg = y
        print('Error: Wrong dimensions. Input data must be a video or image w/ RGB channels.')
    
    yg = yg.astype(int)
    return yg

def loaddata(filename, variable = None):
    '''
    Load .mat file and turn it into grayscale
    filename: (STRING) file name of .mat file
    variable: (STRING) specific variable name to import in .mat file
    '''
    
    # load mat
    if variable == None:
        data = loadmat(filename)
    else:
        data = loadmat(filename)[variable]
    
    # turn data into grayscale
    data_gray = rgb2gray(data)
    
    return data_gray