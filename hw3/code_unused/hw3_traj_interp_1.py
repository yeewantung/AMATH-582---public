# This file interpolate the trajectory of an object within an interval for those frames with tracking points hidden
# import packages
import numpy as np

# (doesn't work)
def traj_interpolation(y, interval, trajx0, trajy0, centerx, centery, width, period, orientation = 'y'):
    '''
    Interpolation the trajectory of an object within an interval
    For those frames with tracking points hidden
    Repair kit to traj_track()
    Input:
        y: (NUMPY ARRAY) data of a set of images w/ background treatment
        interval = [start, end]: (List) interval of those frames with tracking points hidden
        trajx0: (NUMPY ARRAY) the original x-trajectory of the object
        trajy0: (NUMPY ARRAY) the original y-trajectory of the object
        centerx: x-position at center of the upper surface of the paint can in the middle of interval
        centery: y-position at center of the upper surface of the paint can in the middle of interval
        width: width of paint can (use negative width when rotating clockwise viewed from above)
        period: period for guessing
        orientation: ('x' or 'y') normal direction of paint can
    Output:
        trajx: (NUMPY ARRAY) the repaired x-trajectory of the object
        trajy: (NUMPY ARRAY) the repairedny-trajectory of the object
    '''
    # grab dimensions of data
    idx = y.shape # idx[0]: height, idx[1]: width
    start, end = interval
    tspan = end + 2 - start
    
    # justify the effectiveness of interval
    if (start < 0) or (end >= idx[-1]):
        print('Error: Interval exceeding possible values [%d, %d].' % (0, idx[-1]-1))
        return 0, 0
    elif tspan < 0:
        print('Error: Invalid interval. ')
        return 0, 0
    
    if len(idx) == 3: # video
        
        trajx = trajx0.copy()
        trajy = trajy0.copy()
        
        trajx_start = trajx[start - 1]
        trajx_end = trajx[end + 1]
        
        trajy_start = trajy[start - 1]
        trajy_end = trajy[end + 1]
        
        if orientation == 'x':
            
            # intermediate factor R
            R = (-2*width + trajy_end - trajy_start ) / (-width + centery - trajy_start )
            # phase
            phase = np.arctan( ( (np.cos(2*np.pi*tspan/period) - 1) - \
                                R*(np.cos(np.pi*tspan/period) - 1) ) / \
                              ( R*np.sin(np.pi*tspan/period) - np.sin(2*np.pi*tspan/period) ) )
            # depth of upper surface (assume x goes down and up in interval)
            depth = abs( centerx - trajx_start - (trajx_end - trajx_start) / R)
            # x-amplitude of oscillation
            Ax = (trajx_end - trajx_start) / (np.sin(2*np.pi*tspan/period + phase) - np.sin(phase))
            # y-amplitude of oscillation
            Ay = (-2*width + trajy_end - trajy_start ) / (np.sin(2*np.pi*tspan/period + phase) - np.sin(phase))
            # initial x-position of center
            xc = trajx_start - width - Ax * np.sin(phase)
            # initial y-position of center
            yc = trajy_start - Ay * np.sin(phase)
            
            # interpolation
            for i in range(start, end+1): # i: frame number
                trajx[i] = xc + Ax * np.sin(2*np.pi*(i-start+1)/period + phase) - depth * np.sin(np.pi*(i-start+1)/tspan)
                trajy[i] = yc + Ay * np.sin(2*np.pi*(i-start+1)/period + phase) - width * np.cos(np.pi*(i-start+1)/tspan)
            
        elif orientation == 'y':
            
            # intermediate factor R
            R = (2*width + trajx_end - trajx_start) / (width + centerx - trajx_start)
            # phase
            phase = np.arctan( ( (np.cos(2*np.pi*tspan/period) - 1) - \
                                R*(np.cos(np.pi*tspan/period) - 1) ) / \
                              ( R*np.sin(np.pi*tspan/period) - np.sin(2*np.pi*tspan/period) ) )
            # depth of upper surface (assume y goes down and up in interval)
            depth = abs(centery - trajy_start - (trajy_end - trajy_start) / R)
            # x-amplitude of oscillation
            Ax = (2*width + trajx_end - trajx_start) / (np.sin(2*np.pi*tspan/period + phase) - np.sin(phase))
            # y-amplitude of oscillation
            Ay = (trajy_end - trajy_start) / (np.sin(2*np.pi*tspan/period + phase) - np.sin(phase))
            # initial x-position of center
            xc = trajx_start - width - Ax * np.sin(phase)
            # initial y-position of center
            yc = trajy_start - Ay * np.sin(phase)
            
            # interpolation
            for i in range(start, end+1): # i: frame number
                trajx[i] = xc + Ax * np.sin(2*np.pi*(i-start+1)/period + phase) + width * np.cos(np.pi*(i-start+1)/tspan)
                trajy[i] = yc + Ay * np.sin(2*np.pi*(i-start+1)/period + phase) - depth * np.sin(np.pi*(i-start+1)/tspan)
        
        else:
            print('Error: Invalid orientation of paint can. ')
            return 0, 0
        
    else:
        trajx = 0
        trajy = 0
        print('Error: Wrong dimensions. Input data must be a video to interpolate. ')
    
    return trajx, trajy