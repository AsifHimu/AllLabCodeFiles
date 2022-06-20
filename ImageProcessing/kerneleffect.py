from cv2 import imshow
import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = 'horse.jpg'
    rgb = plt.imread(img_path)
    print(rgb.shape)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

    plt.figure(figsize=(40,40))
    plt.subplot(3,3,1)
    plt.title("grayscale")
    plt.imshow(grayscale,cmap="gray")
    
    def imgSlice(img,bitPosition):
        r,c = img.shape
        slice_img = img.copy()
        for i in range(r):
            for j in range(c):
                slice_img[i,j]=img[i,j] & bitPosition
        return slice_img

    
    second_bit = imgSlice(grayscale,1)
    plt.subplot(3,3,2)
    plt.title("first bit")
    plt.imshow(second_bit,cmap='gray')

    second_bit = imgSlice(grayscale,2)
    plt.subplot(3,3,3)
    plt.title("second bit")
    plt.imshow(second_bit,cmap='gray')

    third_bit = imgSlice(grayscale,4)
    plt.subplot(3,3,4)
    plt.title("third bit")
    plt.imshow(third_bit,cmap='gray')


    fourth_bit = imgSlice(grayscale,8)
    plt.subplot(3,3,5)
    plt.title("fourth bit")
    plt.imshow(fourth_bit,cmap='gray')

    fifth_bit = imgSlice(grayscale,16)
    plt.subplot(3,3,6)
    plt.title("fifth bit")
    plt.imshow(fifth_bit,cmap='gray')

    sixth_bit = imgSlice(grayscale,32)
    plt.subplot(3,3,7)
    plt.title("sixth bit")
    plt.imshow(sixth_bit,cmap='gray')

    seventh_bit = imgSlice(grayscale,64)
    plt.subplot(3,3,8)
    plt.title("seventh bit")
    plt.imshow(seventh_bit,cmap='gray')

    eighth_bit = imgSlice(grayscale,128)
    plt.subplot(3,3,9)
    plt.title("eighth bit")
    plt.imshow(eighth_bit,cmap='gray')
    plt.show()
   
if __name__ == '__main__':
    main()
    