from pickletools import uint8
import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    row = gray.shape[0]
    col = gray.shape[1]
    
    img = np.ones((row,col),dtype=np.uint8)
    t1 = 90
    t2 = 150
    for i in range(row):
        for j in range(col):
            if(gray[i][j]>=t1 and gray[i][j]<=t2):
                img[i][j] = 100
            else:
                img[i][j] = 10
    
    print(img)
    plt.imshow(img,cmap='gray')
    plt.show()
    
if __name__ == '__main__':
    main()