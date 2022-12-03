import matplotlib.pyplot as plt
import numpy as np
import cv2

def checkgray(red,green,blue):
    gr = 0.299 * red + 0.587 * green + 0.114 * blue
    plt.subplot(1,1,1)
    plt.imshow(gr,cmap='gray')
    plt.show()

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    #print(rgb.shape)
    red = rgb[:, :, 0]
    green = rgb[:, :, 1]
    blue = rgb[:, :, 2]
    #print(red.shape)

    
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    #print(grayscale.shape)
    th,binary = cv2.threshold(grayscale,125,255,cv2.THRESH_BINARY)
    #print(binary.shape)
    r = cv2.calcHist([red],[0],None,[256],[0,256])
    g = cv2.calcHist([green],[0],None,[256],[0,256])
    b = cv2.calcHist([blue],[0],None,[256],[0,256])
    gray = cv2.calcHist([grayscale],[0],None,[256],[0,256])
    bin = cv2.calcHist([binary],[0],None,[256],[0,256])
    
    #plotting
    plt.figure(figsize=(25, 25))
    
    plt.subplot(2,5,1)
    plt.title('RED')
    plt.imshow(red,cmap='gray')
    
    plt.subplot(2,5,2)
    plt.title('RedHist')
    plt.plot(r)
    
    plt.subplot(2, 5, 3)
    plt.title('GREEN')
    plt.imshow(green, cmap='gray')
    
    plt.subplot(2, 5, 4)
    plt.title('GreenHist')
    plt.plot(g)
    
    plt.subplot(2, 5, 5)
    plt.title('BLUE')
    plt.imshow(blue, cmap='gray')
    
    plt.subplot(2, 5, 6)
    plt.title('BlueHist')
    plt.plot(b)
    
    plt.subplot(2, 5, 7)
    plt.title('Grayscale')
    plt.imshow(grayscale, cmap='gray')

    plt.subplot(2, 5, 8)
    plt.title('GrayHist')
    plt.plot(gray)
    
    plt.subplot(2, 5, 9)
    plt.title('BINARY')
    plt.imshow(binary, cmap='gray')

    plt.subplot(2, 5, 10)
    plt.title('BinaryHist')
    plt.plot(bin)
    
    
    
    plt.show()
    
    #checkgray(red, green, blue)

if __name__ == '__main__':
    main()