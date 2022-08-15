import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    print(gray.shape)
    row = gray.shape[0]
    col = gray.shape[1]
    
    mask = np.zeros((row,col),dtype=np.uint8)
    mask[100:200,200:300] = 255
    
    result = cv2.bitwise_and(gray,mask)
    
    plt.subplot(2,1,1)
    plt.title('gray')
    plt.imshow(gray,cmap='gray')
    plt.subplot(2,1,2)
    plt.title('mask')
    plt.imshow(result,cmap='gray')
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()
    