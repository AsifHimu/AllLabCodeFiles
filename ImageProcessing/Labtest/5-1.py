import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    row = grayscale.shape[0]
    col = grayscale.shape[1]
    
    mask = np.zeros((row,col),dtype=np.uint8)
    
    #mask[200:400,300:500] = 255
    for i in range(200,400):
        for j in range(300,500):
            mask[i][j] = 255
    val = cv2.bitwise_and(mask,grayscale)
    
    plt.subplot(1,2,1)
    plt.title('MainImage')
    plt.imshow(grayscale,cmap='gray')
    
    plt.subplot(1, 2, 2)
    plt.title('MaskedImage')
    plt.imshow(val, cmap='gray')
    
    plt.show()
if __name__ == '__main__':
    main()