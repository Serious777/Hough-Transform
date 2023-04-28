import numpy as np


def myHoughTransform(img_threshold, rhoRes, thetaRes):
    # YOUR CODE HERE

    height, width = img_threshold.shape
    maxRho = np.sqrt(width ** 2 + height ** 2)  # 最大rho值，即对角线的长度
    numRho = int(np.ceil(maxRho / rhoRes))  # 根据rhoRes计算rho的数量
    numTheta = int(np.ceil(2 * np.pi / thetaRes))  # 根据thetaRes计算theta的数量
    rhoScale = np.linspace(0, maxRho, numRho)  # 生成rho的取值范围
    thetaScale = np.linspace(0, 2 * np.pi, numTheta, endpoint=False)  # 生成theta的取值范围，不包括2*pi
    img_hough = np.zeros((numRho, numTheta))  # 初始化Hough变换累加器

    for y in range(height):
        for x in range(width):
            if img_threshold[y, x] > 0:  # 对边缘像素进行处理
                for j in range(numTheta):
                    theta = thetaScale[j]
                    rho = x * np.cos(theta) + y * np.sin(theta)  # 计算当前边缘像素的rho值
                    if rho >= 0:
                        i = int(rho / rhoRes)  # 计算rho对应的索引
                        img_hough[i, j] += 1  # 在累加器中进行投票

    return img_hough, rhoScale, thetaScale
