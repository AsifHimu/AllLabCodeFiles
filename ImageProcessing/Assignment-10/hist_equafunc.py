import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path = 'village1.jpg'
    rgb = plt.imread(img_path)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    grayhist = cv2.calcHist([grayscale],[0],None,[256],[0,256])
    
    L = 256
    row,col = grayscale.shape
    imgsize = row * col
    
    cdf = grayhist.cumsum()
    cdf_min = cdf.min()
    
    eqimg = np.zeros((row,col),dtype=np.uint8)
    for x in range(row):
        for y in range(col):
            eqimg[x][y] = ((cdf[grayscale[x][y]] - cdf_min) / (imgsize - cdf_min)) * (L-1)
            
    eqimghist = cv2.calcHist([eqimg],[0],None,[256],[0,256])
    
    plt.subplot(2,2,1)
    plt.title('Grayscale')
    plt.imshow(grayscale,cmap='gray')
    
    plt.subplot(2, 2, 2)
    plt.title('GrayHist')
    plt.plot(grayhist)
    
    plt.subplot(2, 2, 3)
    plt.title('Equalizedimage')
    plt.imshow(eqimg, cmap='gray')
    
    plt.subplot(2, 2, 4)
    plt.title('EqualizedimageHist')
    plt.plot(eqimghist)
    
    plt.show()
if __name__ == '__main__':
    main()