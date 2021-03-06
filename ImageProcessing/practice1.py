from cv2 import THRESH_BINARY
import matplotlib.pyplot as plt
import cv2

def main():
    img_path = 'himu.jpg'
    rgb = plt.imread(img_path)
    print("RGB shape = ",rgb.shape)
    
    red = rgb[:, :, 0]
    green = rgb[:, :, 1]
    blue = rgb[:, :, 2]
    
    print("Red shape = ",red.shape)
    print("Green shape = ",green.shape)
    print("Blue shape = ",blue.shape)
    
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    print("Grayscale shape = ",grayscale.shape);
    
    _, binary = cv2.threshold(grayscale, 50, 255, cv2.THRESH_BINARY)
    print("Binary shape = ",binary.shape)
    
    """
    plt.figure(figsize = (15,15))
    
    plt.subplot(2, 3, 1)
    plt.title('rgb')
    plt.imshow(rgb)
    
    plt.subplot(2, 3, 2)
    plt.title('red')
    plt.imshow(red, cmap='gray')
    
    plt.subplot(2, 3, 3)
    plt.title('green')
    plt.imshow(green, cmap='gray')
    
    plt.subplot(2, 3, 4)
    plt.title('blue')
    plt.imshow(blue, cmap='gray')
    
    plt.subplot(2, 3, 5)
    plt.title('grayscale')
    plt.imshow(grayscale, cmap='gray')
    
    plt.subplot(2, 3, 6)
    plt.title('binary')
    plt.imshow(binary, cmap='gray')
    plt.savefig('fig1')
    plt.show()
    """
    
    """
    plt.figure(figsize=(15, 15))  
    plt.subplot(2,3,1)
    plt.title('red')
    plt.hist(red.ravel(),256,[0,256]);
    
    plt.subplot(2, 3, 2)
    plt.title('green')
    plt.hist(green.ravel(), 256, [0, 256])
    
    plt.subplot(2, 3, 3)
    plt.title('blue')
    plt.hist(blue.ravel(), 256, [0, 256])
    
    plt.subplot(2, 3, 4)
    plt.title('grayscale')
    plt.hist(grayscale.ravel(), 256, [0, 256])
    
    plt.subplot(2, 3, 5)
    plt.title('binary')
    plt.hist(binary.ravel(), 256, [0, 256])
    plt.savefig('fig2')
    plt.show() 
    """
    img_set = [rgb,red,green,blue,grayscale,binary]
    title_set = ['rgb','red','green','blue','grayscale','binary']
    
    plt.figure(figsize=(15, 15))
    for i in range(6):
        img = img_set[i]
        plt.subplot(2,3,i+1)
        plt.title(title_set[i])
        cnt = len(img.shape)
        if(cnt == 3):
            plt.imshow(img_set[i])
        else:
            plt.imshow(img_set[i],cmap='gray')
    plt.show()
    
    plt.figure(figsize=(15, 15))
    for i in range(6):
        img = img_set[i]
        plt.subplot(2, 3, i+1)
        plt.title(title_set[i])
        plt.hist(img_set[i].ravel(), 256, [0, 256])
    plt.show()
                
if __name__ == '__main__':
    main()
    