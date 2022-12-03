import matplotlib.pyplot as plt
import numpy as np
import cv2
import random

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    th,binary1 = cv2.threshold(grayscale,125,255,cv2.THRESH_BINARY)
    binary2 = np.array([
        [1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 0]
    ],dtype=np.uint8)
    kernel = np.array([
        [0,1,0],
        [1,1,1],
        [0,1,0]
    ],dtype=np.uint8)
    
    erosion1 = cv2.erode(binary1,kernel,iterations=1)
    dialation1 = cv2.dilate(binary1,kernel,iterations=1)
    opening1 = cv2.morphologyEx(binary1,cv2.MORPH_OPEN,kernel)
    closing1 = cv2.morphologyEx(binary1,cv2.MORPH_CLOSE,kernel)
    
    erosion2 = cv2.erode(binary2,kernel,iterations=1)
    dialation2 = cv2.dilate(binary2,kernel,iterations=1)
    opening2 = cv2.morphologyEx(binary2,cv2.MORPH_OPEN,kernel)
    closing2 = cv2.morphologyEx(binary2,cv2.MORPH_CLOSE,kernel)    
    
    plt.subplot(3, 4, 1)
    plt.title('Binaryimage1')
    plt.imshow(binary1,cmap='gray')
    
    plt.subplot(3, 4, 2) 
    plt.title('Erosion')
    plt.imshow(erosion1, cmap='gray')
    
    plt.subplot(3, 4, 3)
    plt.title('Dialation')
    plt.imshow(dialation1, cmap='gray')
    
    plt.subplot(3, 4, 4)
    plt.title('Opening')
    plt.imshow(opening1, cmap='gray')
       
    plt.subplot(3, 4, 5)
    plt.title('Closing')
    plt.imshow(closing1,cmap='gray')
    
    plt.subplot(3, 4, 6)
    plt.title('Binaryimage2')
    plt.imshow(binary2, cmap='gray')
    
    plt.subplot(3, 4, 7)
    plt.title('Erosion')
    plt.imshow(erosion2, cmap='gray')
    
    plt.subplot(3, 4, 8)
    plt.title('Dialation')
    plt.imshow(dialation2, cmap='gray')
    
    plt.subplot(3, 4, 9)
    plt.title('Opening')
    plt.imshow(opening2, cmap='gray')
    
    plt.subplot(3, 4, 10)
    plt.title('Closing')
    plt.imshow(closing2, cmap='gray')
    
    plt.show()
if __name__ == '__main__':
    main()