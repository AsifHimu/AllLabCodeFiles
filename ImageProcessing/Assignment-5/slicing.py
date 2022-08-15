import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    print(grayscale.shape)
    
    def imageslice(img,bitPosition):
        row,col = img.shape
        slice = img.copy()
        for i in range(row):
            for j in range(col):
                slice[i,j]=img[i,j] & bitPosition
        return slice
    
    #plotting
    plt.figure(figsize=(50, 50))
    plt.subplot(3, 3, 1)
    plt.title('Grayscale')
    plt.imshow(grayscale,cmap='gray')
    
    first_bit = imageslice(grayscale,1)
    plt.subplot(3,3,2)
    plt.title('1stBit')
    plt.imshow(first_bit,cmap='gray')
    
    second_bit = imageslice(grayscale, 2)
    plt.subplot(3, 3, 3)
    plt.title('2ndBit')
    plt.imshow(second_bit, cmap='gray')
    
    third_bit = imageslice(grayscale, 4)
    plt.subplot(3, 3, 4)
    plt.title('3rdBit')
    plt.imshow(third_bit, cmap='gray')
    
    fourth_bit = imageslice(grayscale, 8)
    plt.subplot(3, 3, 5)
    plt.title('4thBit')
    plt.imshow(fourth_bit, cmap='gray')
    
    fifth_bit = imageslice(grayscale, 16)
    plt.subplot(3, 3, 6)
    plt.title('5thBit')
    plt.imshow(fifth_bit, cmap='gray')
    
    sixth_bit = imageslice(grayscale, 32)
    plt.subplot(3, 3, 7)
    plt.title('6thBit')
    plt.imshow(sixth_bit, cmap='gray')
    
    seventh_bit = imageslice(grayscale, 64)
    plt.subplot(3, 3, 8)
    plt.title('7thBit')
    plt.imshow(seventh_bit, cmap='gray')
    
    eighth_bit = imageslice(grayscale, 128)
    plt.subplot(3, 3, 9)
    plt.title('8thBit')
    plt.imshow(eighth_bit, cmap='gray')
    plt.savefig('slicedfigure.jpg')
    plt.show()

if __name__ == '__main__':
    main()
    