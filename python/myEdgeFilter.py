import numpy as np
import math
from scipy import signal  # For signal.gaussian function

from myImageFilter import myImageFilter

def myEdgeFilter(img0, sigma):
    # YOUR CODE HERE
    g = signal.gaussian(2 * math.ceil(3 * sigma) + 1, std=sigma)
    h_gaussian = np.outer(g, g)
    img_smooth = myImageFilter(img0, h_gaussian)
    sobel_y = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    sobel_x = np.array([[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]])
    img_x = myImageFilter(img_smooth, sobel_x)
    img_y = myImageFilter(img_smooth, sobel_y)

    # 计算梯度幅度和角度
    gradient_magnitude = np.sqrt(img_x**2 + img_y**2)
    gradient_angle = np.arctan2(img_y, img_x) * 180 / np.pi

    # 非最大抑制
    img1 = np.zeros_like(img0)
    gradient_angle = np.degrees(gradient_angle)
    for i in range(img0.shape[0] - 1):
        for j in range(img0.shape[1] - 1):
            angle = gradient_angle[i, j]
            if angle < 0:
                angle += 180
            if (angle >= 0 and angle < 22.5) or (angle >= 157.5 and angle <= 180):
                q = gradient_magnitude[i, j+1]
                r = gradient_magnitude[i, j-1]
            elif angle >= 22.5 and angle < 67.5:
                q = gradient_magnitude[i+1, j-1]
                r = gradient_magnitude[i-1, j+1]
            elif angle >= 67.5 and angle < 112.5:
                q = gradient_magnitude[i+1, j]
                r = gradient_magnitude[i-1, j]
            else:
                q = gradient_magnitude[i-1, j-1]
                r = gradient_magnitude[i+1, j+1]
            if gradient_magnitude[i, j] >= q and gradient_magnitude[i, j] >= r:
                img1[i, j] = gradient_magnitude[i, j]

    return img1