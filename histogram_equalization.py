import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure as ex
import imageio
import sys

def he_algorithm(img):
    # Histogram Equalization
    if(len(img.shape)==2):      #gray
        outImg = ex.equalize_hist(img[:,:])*255 
    elif(len(img.shape)==3):    #RGB
        outImg = np.zeros((img.shape[0],img.shape[1],3))
        for channel in range(img.shape[2]):
            outImg[:, :, channel] = ex.equalize_hist(img[:, :, channel])*255

    outImg[outImg>255] = 255
    outImg[outImg<0] = 0
    # Return the output image
    return outImg.astype(np.uint8)

def he(filename):
    img_name = filename
    img = imageio.imread(uri=img_name)
    result = he_algorithm(img)
    # returns the np.array of the output image
    return result
    # plt.imshow(result)
    # plt.show()

def main():
    img_name = sys.argv[1]
    img = imageio.imread(img_name)
    result = he_algorithm(img)
    plt.imshow(result)
    plt.show()

if __name__ == '__main__':
    he("input.jpg")