import matplotlib.pyplot as plt
import cv2
import numpy as np


def erosion(img,kernel):
    row,col = img.shape
    r = 2
    c = 2
    cutoff = np.sum(kernel) * 255
    new_img = np.zeros((row-r,col-c),dtype=np.uint8)
    for i in range(row - r):
        for j in range(col - c):
            temp = np.sum(np.multiply(img[i:3+i,j:3+j],kernel))
            if(temp == cutoff):
                new_img[i][j] = 255
    return new_img

def dialation(img,kernel):
    row,col = img.shape
    r = 2
    c = 2
    cutoff = 255
    new_img = np.zeros((row-r,col-c),dtype=np.uint8)
    for i in range(row - r):
        for j in range(col - c):
            temp = np.sum(np.multiply(img[i:3+i,j:3+j],kernel))
            if(temp >= cutoff):
                new_img[i][j] = 255
    return new_img

def opening(img,kernel):
    img1 = erosion(img,kernel)
    new_img = dialation(img1,kernel)
    return new_img

def closing(img,kernel):
    img1 = dialation(img,kernel)
    new_img = erosion(img1,kernel)
    return new_img

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    print(rgb.shape)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    _,binary = cv2.threshold(grayscale,115,255,cv2.THRESH_BINARY)
    
    kernel = np.array([[0,1,0],[1,1,1],[0,1,0]],dtype=np.uint8)
    
    plt.subplot(2, 3, 1)
    plt.title('Binary')
    plt.imshow(binary, cmap='gray')

    plt.subplot(2, 3, 2)
    plt.title('erosion')
    erode = erosion(binary,kernel)
    plt.imshow(erode, cmap='gray')

    plt.subplot(2, 3, 3)
    plt.title('dialation')
    dialate = dialation(binary,kernel)
    plt.imshow(dialate, cmap='gray')

    plt.subplot(2, 3, 4)
    plt.title('opening')
    open = opening(binary,kernel)
    plt.imshow(open, cmap='gray')

    plt.subplot(2, 3, 5)
    plt.title('closing')
    close = closing(binary,kernel)
    plt.imshow(close, cmap='gray')

    plt.show()

if __name__ == '__main__':
    main()