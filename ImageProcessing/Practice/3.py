import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    
    kernel1 = np.array([[0,-1,0],[-1,8,-1],[0,-1,0]])
    img1 = cv2.filter2D(gray,-1,kernel1)
    
    kernel2 = np.ones((3,3),dtype=np.uint8) * 3 / 9
    img2 = cv2.filter2D(gray,-1,kernel2)
    
    plt.subplot(2,1,1)
    plt.imshow(img1,cmap='gray')
    plt.subplot(2,1,2)
    plt.imshow(img2,cmap='gray')
    plt.show()
    
if __name__ == '__main__':
    main()