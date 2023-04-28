import numpy as np


def nonMaxSuppress(img0, kernel_size=3):
    img0_padded = np.pad(img0, (kernel_size // 2, kernel_size // 2), 'constant')
    img1 = np.zeros_like(img0_padded)

    for i in range(kernel_size // 2, img0_padded.shape[0] - kernel_size // 2):
        for j in range(kernel_size // 2, img0_padded.shape[1] - kernel_size // 2):
            img1[i, j] = img0_padded[i, j] + 1 if img0_padded[i, j] >= np.amax(
                img0_padded[i - kernel_size // 2:i + kernel_size // 2 + 1,
                j - kernel_size // 2: j + kernel_size // 2 + 1]) else 0

    img_nms = img1[kernel_size // 2:img0_padded.shape[0] - kernel_size // 2,
              kernel_size // 2:img0_padded.shape[1] - kernel_size // 2]

    return img_nms
