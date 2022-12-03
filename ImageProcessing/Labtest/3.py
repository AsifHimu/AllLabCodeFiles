import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    
    #point detection
    kernel1 = np.array([
        [-1,-1,-1],
        [-1,8,-1],
        [-1,-1,-1]
    ])
    img1 = cv2.filter2D(grayscale,-1,kernel1)
    
    #diagonal edge detection
    kernel2 = np.array([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]
    ])
    img2 = cv2.filter2D(grayscale,-1,kernel2)
    
    #antidiagonal edge detection
    kernel3 = np.array([
        [-2, -1, 0],
        [-1, 0, 1],
        [0, 1, 2]
    ])
    img3 = cv2.filter2D(grayscale,-1,kernel3)
    
    #horizontal edge detection
    kernel4 = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])
    img4 = cv2.filter2D(grayscale,-1,kernel4)
    
    #vertical edge detection
    kernel5 = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    img5 = cv2.filter2D(grayscale,-1,kernel5)
    
    plt.subplot(2,3,1)
    plt.title('Point')
    plt.imshow(img1,cmap='gray')
    
    plt.subplot(2, 3, 2)
    plt.title('Diagonal')
    plt.imshow(img2, cmap='gray')
    
    plt.subplot(2, 3, 3)
    plt.title('Anti Diagonal')
    plt.imshow(img3, cmap='gray')
    
    plt.subplot(2, 3, 4)
    plt.title('Horizontal')
    plt.imshow(img4, cmap='gray')
    
    plt.subplot(2, 3, 5)
    plt.title('Vertical')
    plt.imshow(img5, cmap='gray')
    
    plt.show()
if __name__ == '__main__':
    main()