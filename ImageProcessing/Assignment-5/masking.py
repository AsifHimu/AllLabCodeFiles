import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path = 'nature.jpg'
    rgb = plt.imread(img_path)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    print(grayscale.shape)
    
    #mask = np.zeros(grayscale.shape,dtype=bool)
    #mask[0:4,0:4] = True
    #print(mask)
    
    row = grayscale.shape[0]
    col = grayscale.shape[1]
    mask = np.zeros((row, col), dtype=np.uint8)
    mask[100:500,200:400] = 255
    #print(mask)
    result = cv2.bitwise_and(grayscale,mask)
    
    plt.figure(figsize=(30, 30))
    plt.subplot(2, 2, 1)
    plt.title('RGB')
    plt.imshow(rgb)

    plt.subplot(2, 2, 2)
    plt.title('grayscale')
    plt.imshow(grayscale, cmap='gray')

    plt.subplot(2, 2, 3)
    plt.title('MaskedImage')
    plt.imshow(result, cmap='gray')
    plt.savefig('MaskedImage.jpg') 
    plt.show()
    

if __name__ == '__main__':
    main()
    