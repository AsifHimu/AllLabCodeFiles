import matplotlib.pyplot as plt
import numpy as np
import cv2

def gaussian_filter(spatial_domain):
    m,n = spatial_domain.shape
    gauss = np.zeros((m,n),dtype=np.float32)
    d0 = 10
    for u in range(m):
        for v in range(n):
            D = np.sqrt((u - m/2) ** 2 + (v - n/2) ** 2)
            gauss[u][v] = np.exp((-D**2) / (2 * d0 * d0))
    return gauss

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    
    spatial_domain = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    freq_domain = np.fft.fft2(spatial_domain)
    freq_domain_shift = np.fft.fftshift(freq_domain)
    
    freq_domain_abs = 100 * np.log(np.abs(freq_domain))
    freq_domain_shift_abs = 100 * np.log(np.abs(freq_domain_shift))
    
    gauss = gaussian_filter(spatial_domain)
    
    gauss_shifted = freq_domain_shift * gauss
    gauss_shifted_abs = np.log(np.abs(gauss_shifted))
    G = np.fft.ifftshift(gauss_shifted)
    spatial_domain_filterd = np.abs(np.fft.ifft2(G))
    
    
    plt.subplot(2,3,1)
    plt.imshow(spatial_domain,cmap='gray')
    plt.title('spatial domain')
    
    plt.subplot(2, 3, 2)
    plt.imshow(freq_domain_shift_abs, cmap='gray')
    plt.title('frequency domain shifted')
    
    plt.subplot(2, 3, 3)
    plt.imshow(gauss, cmap='gray')
    plt.title('Gaussian filter')
    
    plt.subplot(2, 3, 4)
    plt.imshow(gauss_shifted_abs, cmap='gray')
    plt.title('freq_domain_shift * gauss')
    
    plt.subplot(2, 3, 5)
    plt.imshow(spatial_domain_filterd, cmap='gray')
    plt.title('Back to spatial domain')
    
    plt.show()
    
if __name__ == '__main__':
    main()