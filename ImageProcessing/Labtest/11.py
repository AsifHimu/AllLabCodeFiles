import matplotlib.pyplot as plt
import numpy as np
import cv2

def gaussian_filter(spatial_domain):
    m = spatial_domain.shape[0]
    n = spatial_domain.shape[1]
    gauss = np.zeros((m,n),dtype=np.float32)
    d0 = 10
    for u in range(m):
        for v in range(n):
            D = np.sqrt((u - m/2) ** 2 + (v - n/2) ** 2)
            gauss[u][v] = np.exp((-D**2) / (2*d0*d0))
    return gauss
    
def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    
    saptial_domain = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    freq_domain = np.fft.fft2(saptial_domain)
    freq_domain_shift = np.fft.fftshift(freq_domain)
    #freq_domain_shift_abs = 100 * np.log(np.abs(freq_domain_shift))
    
    gauss = gaussian_filter(saptial_domain)
    gauss_shifted = freq_domain_shift * gauss
    #gauss_shifted_abs = np.log(np.abs(gauss_shifted))
    G = np.fft.ifftshift(gauss_shifted)
    saptial_domain_filtered = np.abs(np.fft.ifft2(G))
    
    plt.subplot(1,1,1)
    plt.imshow(saptial_domain_filtered,cmap='gray')
    plt.show()
        
    
if __name__ == '__main__':
    main()