import matplotlib.pyplot as plt
import cv2
import numpy as np


def main():
    img_path = 'imu.jpg'
    r = plt.imread(img_path)
    
    #plt.figure(figsize=(10, 10))
    #plt.subplot(2,1,1)
    #plt.title('Original')
    #plt.imshow(r)
    
    gray = cv2.cvtColor(r, cv2.COLOR_RGB2GRAY)   
    row = gray.shape[0]
    col = gray.shape[1]
    s = np.zeros((row, col), dtype=np.uint8)
    
    #plt.subplot(1,1,1)
    #plt.title('Grayscale')
    #plt.imshow(gray,cmap='gray')

    T1 = 100
    T2 = 200
    #condition1
    for i in range(row):
        for j in range(col):
            if(gray[i][j] >= T1 and gray[i][j] <= T2):
                s[i][j] = 100
            else:
                s[i][j] = 10
                
    #plt.subplot(2, 3, 2)
    #plt.title('Processed1')
    #plt.imshow(s,cmap='gray')
    #condition2
    s = np.zeros((row, col), dtype=np.uint8)
    for i in range(row):
        for j in range(col):
            if(gray[i][j] >= T1 and gray[i][j] <= T2):
                s[i][j] = 100
            else:
                s[i][j] = gray[i][j]
    
    #plt.subplot(1, 1, 1)
    #plt.title('Processed2')
    #plt.imshow(s, cmap='gray')
    
    #condition3
    c = 2
    s = c * np.log(1 + gray)
    
    #plt.subplot(1, 1, 1)
    #plt.title('Processed3')
    #plt.imshow(s, cmap='gray') 
  
    #conditon4
    eps = 0.0000001
    p = 5 
    s = c * ((gray + eps) ** p)
       
    plt.subplot(1, 1, 1)
    plt.title('Processed4')
    plt.imshow(s, cmap='gray')
    plt.savefig('Prcessedfigure')
    
    plt.show() 

if __name__ == '__main__':
	main()
