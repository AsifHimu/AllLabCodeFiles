import matplotlib.pyplot as plt
import cv2
import numpy as np


def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    
    laplacian = np.array([
        [0,-1,0],
        [-1,5,-1],
        [0,-1,0]
    ])
    sobel = np.array([
        [-1,0,1],
        [-2,0,2],
        [-1,0,1]
    ])
    img1 = cv2.filter2D(grayscale,-1,laplacian)
    img2 = cv2.filter2D(grayscale, -1, sobel)
    
    plt.subplot(1,2,1)
    plt.title('laplacian')
    plt.imshow(img1,cmap='gray')
    
    plt.subplot(1, 2, 2)
    plt.title('sobel')
    plt.imshow(img2, cmap='gray')
    
    plt.show()
if __name__ == '__main__':
    main()