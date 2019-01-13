import sys
import cv2
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#import custom modules
sys.path.append('../src/utils/')
from general_utils import *




def main():
    jprint("Using Tensorflow v" + tf.__version__)
    jprint("Using Opencv v" + cv2.__version__)
    img = cv2.imread('../../images/wei-wang.JPG')
    jprint(type(img))
    resized_image = cv2.resize(img, (1000, 1000))
    jprint(resized_image.shape)
    cv2.imshow('Image', resized_image)
    cv2.waitKey(5000)







if __name__ == '__main__':
    main()
