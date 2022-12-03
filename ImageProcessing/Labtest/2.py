import matplotlib.pyplot as plt
import numpy as np
import cv2

def func1(grayscale):
    row = grayscale.shape[0]
    col = grayscale.shape[0]
    img1 = np.ones((row, col), dtype=np.uint8)
    for i in range(row):
        for j in range(col):
            img1[i][j] = 255 - grayscale[i][j]
    
    return img1

def func2(grayscale):
    row = grayscale.shape[0]
    col = grayscale.shape[0]
    img2 = np.ones((row, col), dtype=np.uint8)
    t1 = 50
    t2 = 150

    for i in range(row):
        for j in range(col):
            if(grayscale[i][j] >= t1 and grayscale[i][j] <= t2):
                img2[i][j] = 200
            else:
                img2[i][j] = grayscale[i][j]
    
    return img2

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    
    im1 = func1(grayscale)
    im2 = func2(grayscale)
    plt.subplot(1,2,1)
    plt.imshow(im1,cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(im2,cmap='gray')
    
    plt.show()
        
if __name__ == '__main__':
    main()