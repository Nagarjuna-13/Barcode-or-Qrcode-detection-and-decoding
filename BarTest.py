import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

""" This code helps us in finding the Barcode or Qrcode from a given image 
 it gives all the properties of barcode or Qrcode such as data,type of code,position in image,shape of code"""
img=cv.imshow('')
code=decode(img)
print(code)

###############################################


#This code helps us to find all the Barcodes or Qrcode from the given image
img=cv.imshow('')
code=decode(img)
print(code)
for barcode in decode(img):
    print(barcode.data)
    myData=barcode.data.decode('utf-8')
    print(myData)