import numpy as np
import cv2  # For cv2.dilate function
from nonMaxSuppress import nonMaxSuppress
def myHoughLines(hough_accu, nLines):
    # YOUR CODE HERE
    # 按降序排列图像中的峰值
    print(hough_accu.shape)

    hough_accu = nonMaxSuppress(hough_accu, 29)
    indices = np.argsort(hough_accu.ravel())[::-1]

    # 找到前nLines个峰值
    indices = indices[:nLines]

    # 计算峰值在原图中的行和列坐标
    rhos, thetas = np.unravel_index(indices, hough_accu.shape)

    # 返回rho和theta值
    return rhos, thetas
