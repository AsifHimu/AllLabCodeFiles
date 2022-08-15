import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    print(gray.shape)
    
    #kernel = np.array([[167,133,111],[144,140,135],[159,154,148]],dtype=np.int8)
    
    def imageslice(image,pos):
        row = image.shape[0]
        col = image.shape[1]
        slice = image.copy()
        for i in range(row):
            for j in range(col):
                slice[i][j] = image[i][j] & pos
        return slice
    
    title_set = ['1stbit','2ndbit','3rdbit','4thbit','5thbit','6thbit','7thbit','8thbit']
    p = 1
    for i in range(len(title_set)):
        plt.subplot(3,3,i+1)
        plt.title(title_set[i])
        if(i == 0):
            p = 1
        else:
            p = p * 2 
        val = imageslice(gray,p)
        plt.imshow(val,cmap='gray')
    
    plt.show()
        
    
    
    
    
if __name__ == '__main__':
    main()
    