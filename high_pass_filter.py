import numpy as np
from scipy import ndimage
import numpy as np

def high_pass_filter(data):
    k = np.array([[-1, 2, -2, 2, -1],
                  [2, -6, 8, -6, 2],
                  [-2, 8, -12, 8, -2],
                  [2, -6, 8, -6, 2],
                  [-1, 2, -2, 2, -1]])
    kernel = (1 / 12) * k
    highpass_5x5 = ndimage.convolve(data, kernel)
    return highpass_5x5









