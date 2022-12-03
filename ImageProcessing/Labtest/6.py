import matplotlib.pyplot as plt
import numpy as np
import cv2
import random

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    
    row = grayscale.shape[0]
    col = grayscale.shape[1]
    new_img = grayscale.copy()
    
    rand_value = random.randint(100,row*100+col*20)
    for i in range(rand_value):
        y = random.randint(0,row-1)
        x = random.randint(0,col-1)
        new_img[y][x] = 255
    
    for i in range(rand_value):
        y = random.randint(0, row-1)
        x = random.randint(0, col-1)
        new_img[y][x] = 0
        
    #averaging filter
    kernel = np.array([
        [1/25,1/25,1/25,1/25,1/25],
        [1/25,1/25,1/25,1/25,1/25],
        [1/25,1/25,1/25,1/25,1/25],
        [1/25,1/25,1/25,1/25,1/25],
        [1/25,1/25,1/25,1/25,1/25]
    ],dtype=np.float32)
    filter1 = cv2.filter2D(new_img,-1,kernel)
    #filter1 = cv2.blur(new_img,(5,5))
    
    #median filter
    filter2 = cv2.medianBlur(new_img,3)
    
    #plotting
    plt.subplot(2,2,1)
    plt.title('Grayscale')
    plt.imshow(grayscale,cmap='gray')
    
    plt.subplot(2,2,2)
    plt.title('with salt pepper')
    plt.imshow(new_img,cmap='gray')
    
    plt.subplot(2, 2, 3)
    plt.title('with average filter')
    plt.imshow(filter1, cmap='gray')
    
    plt.subplot(2, 2, 4)
    plt.title('with median filter')
    plt.imshow(filter2, cmap='gray')
    
    plt.show()
if __name__ == '__main__':
    main()