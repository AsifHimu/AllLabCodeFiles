import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = 'dark.jpg'
    rgb = plt.imread(img_path)
    print(rgb.shape)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    print(grayscale.shape);
    
    row = grayscale.shape[0]
    col = grayscale.shape[1]
    val1 = cv2.calcHist([grayscale], [0], None, [256], [0, 256])
    
    right = grayscale.copy()
    Right = right + 60
    val2 = cv2.calcHist([Right], [0], None, [256], [0, 256])
    
    left = grayscale.copy()
    Left = left - 20
    val3 = cv2.calcHist([Left], [0], None, [256], [0, 256])
    
    #plotting
    plt.figure(figsize = (15,15))
    plt.subplot(2,4,1);
    plt.title('Original')
    plt.imshow(grayscale,cmap='gray')
    plt.subplot(2,4,2)
    plt.title('Original')
    plt.plot(val1)
    plt.subplot(2,4,3)
    plt.title('Moved Right')
    plt.imshow(Right,cmap='gray')
    plt.subplot(2,4,4)
    plt.title('Moved Right')
    plt.plot(val2)
    plt.subplot(2, 4, 5)
    plt.title('Moved Left')
    plt.imshow(Left, cmap='gray')
    plt.subplot(2, 4, 6)
    plt.title('Moved Left')
    plt.plot(val3)
    plt.savefig('intensity_change.jpg')
    plt.show()


if __name__ == '__main__':
    main()