import matplotlib.pyplot as plt
import cv2
import numpy as np


def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

    laplacian = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    img1 = cv2.filter2D(gray, -1, laplacian)

    #sobel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]) #horizontal_edge
    sobel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]) #vertical_edge
    img2 = cv2.filter2D(gray, -1, sobel)

    plt.subplot(2, 1, 1)
    plt.imshow(img1, cmap='gray')
    plt.subplot(2, 1, 2)
    plt.imshow(img2, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()
