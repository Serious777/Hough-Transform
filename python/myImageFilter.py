import numpy as np
import cv2

def myImageFilter(img0, h):
    # YOUR CODE HERE
    # 卷积核翻转
    h = np.flipud(np.fliplr(h))
    # 获取卷积核维度
    h_rows, h_cols = h.shape[:2]
    # 全0填充 确保图像尺寸不受影响
    img0_padded = np.pad(img0, ((h_rows//2, h_rows//2), (h_cols//2, h_cols//2)), 'edge')
    img1 = np.zeros_like(img0_padded)

    # 卷积 图像卷积结果位于卷积区域中心
    for i in range(h_rows//2, img0_padded.shape[0]-h_rows//2):
        for j in range(h_cols//2, img0_padded.shape[1]-h_cols//2):
            img1[i, j] = np.sum(h * img0_padded[i-h_rows//2:i+h_rows//2+1, j-h_cols//2:j+h_cols//2+1])

    # 截取图像中心结果
    img_result = img1[h_rows//2:img0_padded.shape[0]-h_rows//2, h_cols//2:img0_padded.shape[1]-h_cols//2]
    return img_result


