import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    print(rgb.shape)
    
    red = rgb[:,:,0]
    green = rgb[:,:,1]
    blue = rgb[:,:,2]
    
    #print(red)
    #print(green)
    #print(blue)
    
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    #print('grayscale array')
    #print(gray)
    
    th,bin = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
    #print(bin)
    print(th)
    '''
    #plotting different images
    img_set = [rgb,red,green,blue,gray,bin]
    title_set = ['RGB','RED','GREEN','BLUE','GRAY','BINARY']
    plt.figure(figsize=(20,20))
    for i in range(len(img_set)):
        img = img_set[i]
        val = len(img)
        plt.subplot(2,3,i+1)
        if(val == 3):
            plt.title(title_set[i])
            plt.imshow(img)
        else:
            plt.title(title_set[i])
            plt.imshow(img,cmap='gray')
    plt.show()
    '''
    #plotting histogram
    img_set = [red, green, blue, gray, bin]
    title_set = ['RED', 'GREEN', 'BLUE', 'GRAY', 'BINARY']
    plt.figure(figsize=(20, 20))
    for i in range(len(img_set)):
        img = img_set[i]
        plt.subplot(2,3,i+1)
        plt.title(title_set[i])
        #plt.hist(img.ravel(),256,[0,256])
        val = cv2.calcHist([img],[0],None,[256],[0,256])
        plt.plot(val)
        
    plt.savefig('opencv_hist.jpg')
    plt.show()
if __name__ == '__main__':
    main()
    