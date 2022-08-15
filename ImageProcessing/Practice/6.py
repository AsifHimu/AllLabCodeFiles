import matplotlib.pyplot as plt
import cv2
import numpy as np
import random

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    print(gray.shape)
    
    row = gray.shape[0]
    col = gray.shape[1]
    img = gray.copy()
    
    pixel_num = random.randint(100,row*100+col*10)
    for i in range(pixel_num):
        y = random.randint(0,row-1)
        x = random.randint(0,col-1)
        img[y][x] = 255
    
    for i in range(pixel_num):
        y = random.randint(0,row-1)
        x = random.randint(0,col-1)
        img[y][x] = 0
    plt.subplot(2,1,1)
    plt.imshow(gray,cmap='gray')
    plt.subplot(2,1,2)
    plt.imshow(img,cmap='gray')
    plt.show()
    
    

if __name__ == '__main__':
    main()