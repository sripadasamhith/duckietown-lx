from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    
    res = np.zeros(shape=shape, dtype="float32") # lower & upper bounds
    posX = shape[0] - 1
    posY = shape[1] /2
    maxDist = 400

    for i in range(shape[0]):
        for j in range(shape[1]):
            dist = np.sqrt((i - posX) **2 + (j - posY) **2)
            cappedDist = min(dist, maxDist)
            if j < posY:
                res[i,j] = maxDist - cappedDist
            else:
                res[i,j] = cappedDist - maxDist
    
    # # custom function below between ------
    
    # # res[120:, 0:100] = 0.75
    # # res[150:, 40:80] = 0.3 # 
    # # res[150:, 80:160] = 0.5
    # # res[150:, 160:240] = 0.8
    # res[150:, :320] = 0.85
    # res[480:, 320:] = 0 # [400:,:]
    


    # # ------------------------------------

    
    # # these are random values
    # # res[100:150, 100:150] = 0 # 1
    # # res[300:, 200:] = 0 # 1
    # # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32") # lower & upper bounds
    posX = shape[0] - 1
    posY = shape[1] /2
    maxDist = 400

    for i in range(shape[0]):
        for j in range(shape[1]):
            dist = np.sqrt((i - posX) **2 + (j - posY) **2)
            cappedDist = min(dist, maxDist)
            if j < posY:
                res[i,j] = maxDist - cappedDist
            else:
                res[i,j] = cappedDist - maxDist
    

    # # these are random values
    # # res[100:150, 100:300] = 0 # -1

    # # res[150:, 320:420] = -0.75
    # # res[150:, 400:480] = -0.8
    # # res[150:, 480:560] = -0.5
    # # res[150:, 560:600] = -0.3
    # res[150:, 320:540] = -0.85
    # res[480:100, :320] = 0 # 0


    # ---
    return res
