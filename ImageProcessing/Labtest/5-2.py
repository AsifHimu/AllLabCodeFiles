import matplotlib.pyplot as plt
import numpy as np
import cv2

def imageslice(matrix,position):
    row = matrix.shape[0]
    col = matrix.shape[1]
    slice = matrix.copy()
    for i in range(row):
        for j in range(col):
            slice[i][j] = matrix[i][j] & position
    
    return slice

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    
    '''
    title_set = ['1stbit','2ndbit','3rdbit','4thbit','5thbit','6thbit','7thbit','8thbit']
    p = 1
    for i in range(len(title_set)):
        plt.subplot(2,4,i+1)
        plt.title(title_set[i])
        if i == 0:
            p = 1
        else:
            p = p * 2 
        val = imageslice(grayscale,p)
        plt.imshow(val,cmap='gray')
    '''
    plt.subplot(1,2,1)
    plt.title('6th bit')
    val1 = imageslice(grayscale,32)
    plt.imshow(val1,cmap='gray')
    
    plt.subplot(1,2,2)
    plt.title('7th bit')
    val2 = imageslice(grayscale,64)
    plt.imshow(val2,cmap='gray')
    
    plt.show()
if __name__ == '__main__':
    main()