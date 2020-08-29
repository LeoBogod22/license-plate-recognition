import matplotlib.pyplot as plt
import cv2

#import imutils

import numpy as np
from PIL import Image
from PIL import ImageEnhance
from skimage import color, data, restoration
from scipy.signal import convolve2d
import pytesseract
import PIL.ImageOps
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
img = cv2.imread('f.jpg',cv2.IMREAD_COLOR)
img = cv2.resize(img, (600,400) )
threshold = 180 # to be determined
_, img_binarized = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
pil_img = Image.fromarray(img_binarized)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 13, 15, 15)

edged = cv2.Canny(gray, 30, 200)
thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)
#contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#contours = imutils.grab_contours(contours)
contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None

gaussian_blur_license_plate = cv2.GaussianBlur(
    img, (5, 5), 0)

for c in contours:

    peri = cv2.arcLength(c, True)
    approx =    rect = cv2.minAreaRect(c)

    if len(approx) == 4:
        screenCnt = approx
        break

if screenCnt is None:
    detected = 0
    print ("No contour detected")
else:
     detected = 1

if detected == 1:
    cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

mask = np.zeros(gray.shape,np.uint8)
new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
new_image = cv2.bitwise_and(img,img,mask=mask)

(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx+1, topy:bottomy+1]

text = pytesseract.image_to_string(Cropped, config='--psm 11')
print("programming_fever's License Plate Recognition\n")
print("Detected license plate Number is:",text)
img = cv2.resize(img,(500,300))

Cropped = cv2.resize(Cropped,(400,200))


im = Image.fromarray(Cropped)
im.save('test.png')


image = Image.open('test.png')
enh_bri = ImageEnhance.Brightness(image )
brightness = 1.0
image_brightened = enh_bri.enhance(brightness)


imwhole = np.array(image_brightened)


cv2.imshow('car',img)
cv2.imshow('Cropped',imwhole)

cv2.waitKey(0)
cv2.destroyAllWindows()
