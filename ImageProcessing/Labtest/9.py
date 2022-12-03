import matplotlib.pyplot as plt
import numpy as np
import cv2

def erosion(matrix,kernel):
    row = matrix.shape[0]
    col = matrix.shape[1]
    r = 2
    c = 2
    new_img = np.zeros((row-r,col-c),dtype=np.uint8)
    val = np.sum(kernel) * 255
    for i in range(row - r):
        for j in range(col - c):
            temp = np.sum(np.multiply(matrix[i:3+i,j:3+j],kernel))
            if temp == val:
                new_img[i][j] = 255
                
    return new_img

def dilation(matrix,kernel):
    row = matrix.shape[0]
    col = matrix.shape[1]
    r = 2
    c = 2
    new_img = np.zeros((row-r,col-c),dtype=np.uint8)
    val = 255
    for i in range(row - r):
        for j in range(col - c):
            temp = np.sum(np.multiply(matrix[i:3+i,j:3+j],kernel))
            if temp >= val:
                new_img[i][j] = 255
                
    return new_img

def opening(img,kernel):
    img1 = erosion(img,kernel)
    new_img = dilation(img1,kernel)
    return new_img

def closing(img,kernel):
    img1 = dilation(img,kernel)
    new_img = erosion(img1,kernel)
    return new_img
    
def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    th,binary = cv2.threshold(grayscale,125,255,cv2.THRESH_BINARY)
    kernel = np.array([
        [0,1,0],
        [1,1,1],
        [0,1,0]
    ],dtype=np.uint8)
    
    plt.subplot(2, 3, 1)
    plt.title('Binary')
    plt.imshow(binary, cmap='gray')

    plt.subplot(2, 3, 2)
    plt.title('erosion')
    erode = erosion(binary, kernel)
    plt.imshow(erode, cmap='gray')

    plt.subplot(2, 3, 3)
    plt.title('dialation')
    dialate = dilation(binary, kernel)
    plt.imshow(dialate, cmap='gray')

    plt.subplot(2, 3, 4)
    plt.title('opening')
    open = opening(binary, kernel)
    plt.imshow(open, cmap='gray')

    plt.subplot(2, 3, 5)
    plt.title('closing')
    close = closing(binary, kernel)
    plt.imshow(close, cmap='gray')

    plt.show()
    
if __name__ == '__main__':
    main()