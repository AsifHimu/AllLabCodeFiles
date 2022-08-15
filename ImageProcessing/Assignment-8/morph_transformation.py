import matplotlib.pyplot as plt
import numpy as np
import cv2
def main():
    img_path = 'img1.jpg'
    rgb = plt.imread(img_path)
    print(rgb.shape)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_BGR2GRAY)  
    _,binary = cv2.threshold(grayscale,120,255,cv2.THRESH_BINARY)
    
    kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    kernel3 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    #kernel1
    erosion1 = cv2.erode(binary,kernel1,iterations = 1)
    dialation1 = cv2.dilate(binary, kernel1, iterations=1)
    opening1 = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel1)
    closing1 = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel1)
    
    #kernel2
    erosion2 = cv2.erode(binary, kernel2, iterations=1)
    dialation2 = cv2.dilate(binary, kernel2, iterations=1)
    opening2 = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel2)
    closing2 = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel2)
    
    #kernel3
    erosion3 = cv2.erode(binary, kernel3, iterations=1)
    dialation3 = cv2.dilate(binary, kernel3, iterations=1)
    opening3 = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel3)
    closing3 = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel3)
    
    plt.figure(figsize = (30, 30))
    plt.subplot(3,5,1)
    plt.title('BINARY')
    plt.imshow(binary,cmap='gray')
    
    plt.subplot(3,5,2)
    plt.title('kernel1(erosion)')
    plt.imshow(erosion1,cmap='gray')
    
    plt.subplot(3, 5, 3)
    plt.title('kernel1(dialation)')
    plt.imshow(dialation1, cmap='gray')
    
    plt.subplot(3, 5, 4)
    plt.title('kernel1(opening)')
    plt.imshow(opening1, cmap='gray')
    
    plt.subplot(3, 5, 5)
    plt.title('kernel1(closing)')
    plt.imshow(closing1, cmap='gray')
    
    plt.subplot(3, 5, 6)
    plt.title('kernel2(erosion)')
    plt.imshow(erosion2, cmap='gray')

    plt.subplot(3, 5, 7)
    plt.title('kernel2(dialation)')
    plt.imshow(dialation2, cmap='gray')

    plt.subplot(3, 5, 8)
    plt.title('kernel2(opening)')
    plt.imshow(opening2, cmap='gray')

    plt.subplot(3, 5, 9)
    plt.title('kernel2(closing)')
    plt.imshow(closing2, cmap='gray')
    
    plt.subplot(3, 5, 10)
    plt.title('kernel3(erosion)')
    plt.imshow(erosion3, cmap='gray')

    plt.subplot(3, 5, 11)
    plt.title('kernel3(dialation)')
    plt.imshow(dialation3, cmap='gray')

    plt.subplot(3, 5, 12)
    plt.title('kernel3(opening)')
    plt.imshow(opening3, cmap='gray')

    plt.subplot(3, 5, 13)
    plt.title('kernel3(closing)')
    plt.imshow(closing3, cmap='gray')
    plt.savefig('morph_transform.jpg')
    plt.show() 
        
if __name__ == '__main__':
    main()
        
    