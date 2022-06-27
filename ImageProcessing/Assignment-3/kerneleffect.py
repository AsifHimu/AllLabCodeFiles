import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = 'nature.jpg'
    rgb = plt.imread(img_path)
    print(rgb.shape)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    print(grayscale.shape)
    
    #kernel1
    kernel1 = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    processed_img1 = cv2.filter2D(grayscale, -1, kernel1)
    #print('Kernel1: {}'.format(kernel1))
    print('Kernel1: ')
    print(kernel1)
    #kernel2
    kernel2 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    processed_img2 = cv2.filter2D(grayscale, -1, kernel2)
    print('Kernel2: {}'.format(kernel2))
    #kernel3
    kernel3 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    processed_img3 = cv2.filter2D(grayscale, -1, kernel3)
    print('Kernel3: {}'.format(kernel3))
    #kernel4
    kernel4 = np.ones((3, 3), dtype=np.float32) * 3 / 7
    processed_img4 = cv2.filter2D(grayscale, -1, kernel4)
    print('Kernel4: {}'.format(kernel4))
    #kernel5
    kernel5 = np.ones((3, 3), dtype=np.float32) * 11 / 7
    processed_img5 = cv2.filter2D(grayscale, -1, kernel5)
    print('Kernel5: {}'.format(kernel5))
    #kernel6
    kernel6 = np.array([[5, -1, 6], [3, 1, 4], [8, -1, 4]])
    processed_img6 = cv2.filter2D(grayscale, -1, kernel6)
    print('Kernel6: {}'.format(kernel6))
    
    #plotting
    plt.figure(figsize=(35, 35))
    plt.subplot(2,4,1)
    plt.title('RGB')
    plt.imshow(rgb)
    
    plt.subplot(2, 4, 2)
    plt.title('grayscale')
    plt.imshow(grayscale,cmap='gray')
    
    plt.subplot(2, 4, 3)
    plt.title('kernel1')
    plt.imshow(processed_img1, cmap='gray')
    
    plt.subplot(2, 4, 4)
    plt.title('kernel2')
    plt.imshow(processed_img2, cmap='gray')
    
    plt.subplot(2, 4, 5)
    plt.title('kernel3')
    plt.imshow(processed_img3, cmap='gray')
    
    plt.subplot(2, 4, 6)
    plt.title('kernel4')
    plt.imshow(processed_img4, cmap='gray')
    
    plt.subplot(2, 4, 7)
    plt.title('kernel5')
    plt.imshow(processed_img5, cmap='gray')
    
    plt.subplot(2, 4, 8)
    plt.title('kernel6')
    plt.imshow(processed_img6, cmap='gray')
    plt.savefig('finalfigure')
    plt.show()
    
if __name__ == '__main__':
    main()
    