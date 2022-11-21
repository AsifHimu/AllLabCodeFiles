import numpy as np
import matplotlib.pyplot as plt
import cv2

def conv(mat,ker):
    row = mat.shape[0]
    col = mat.shape[1]
    
    #r = kernel.shape[0] // 2
    #c = kernel.shape[1] // 2
    #r = r * 2
    #c = c * 2
    r = 2
    c = 2
    
    new_img = np.zeros((row - r,col - c),dtype=np.uint8)
    for i in range(row - r):
        for j in range(col - c):
            temp = np.sum(np.multiply(mat[i:3+i,j:3+j],ker))
            if(temp > 255):
                new_img[i][j] = 255
            elif(temp < 0):
                new_img[i][j] = 0
            else:
                new_img[i][j] = temp
        
    return new_img

def main():
    img_path = 'image_RGB.jpg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    #kernel = np.ones((3,3)) / 9
    conv1 = cv2.filter2D(gray,-1,kernel)
    conv2 = conv(gray,kernel)
    
    plt.subplot(1,2,1)
    plt.title('Neighbourhood processing cv2')
    plt.imshow(conv1,cmap='gray')
    
    plt.subplot(1, 2, 2)
    plt.title('Neighbourhood processing manually')
    plt.imshow(conv2, cmap='gray')
    
    plt.show()
    
    

if __name__ == '__main__':
    main()