from ast import main
import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    source_img = np.array([
        [1,1,0,1,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,1,0,1,0,0,0,1],
        [0,0,1,0,1,0,1,0],
        [0,0,0,1,1,1,0,0],
        [0,1,0,0,1,0,1,0],
        [0,0,1,1,1,1,0,0]
    ],dtype=np.uint8)
    
    struct_elem = np.array([
        [0,1,0],
        [1,1,1],
        [0,1,0]
    ],dtype=np.uint8)
    
    erosion = cv2.erode(source_img, struct_elem, iterations=1)
    dialation = cv2.dilate(source_img, struct_elem, iterations=1)
    opening = cv2.morphologyEx(source_img, cv2.MORPH_OPEN, struct_elem)
    closing = cv2.morphologyEx(source_img, cv2.MORPH_CLOSE, struct_elem)
    #img = cv2.copyMakeBorder(struct_elem, 1, 1, 1, 1, cv2.BORDER_CONSTANT,(0,0,0))
    #print(img)
    plt.subplot(2,3,1)
    plt.title('Binary')
    plt.imshow(source_img,cmap='gray')
    
    plt.subplot(2, 3, 2)
    plt.title('erosion')
    plt.imshow(erosion, cmap='gray')
    
    plt.subplot(2, 3, 3)
    plt.title('dialation')
    plt.imshow(dialation, cmap='gray')
    
    plt.subplot(2, 3, 4)
    plt.title('opening')
    plt.imshow(opening, cmap='gray')
    
    plt.subplot(2, 3, 5)
    plt.title('closing')
    plt.imshow(closing, cmap='gray')
    
    plt.show()
if __name__ == '__main__':
    main()