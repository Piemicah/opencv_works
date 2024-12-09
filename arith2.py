import cv2
import numpy as np

img1=cv2.imread('messi.jpg')
logo=cv2.imread('logooriginal.png')


def mask_image(im,im2):
    h,w=im2.shape[:2]
    roi=im[:h,:w]
    im2Gray=cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(im2Gray, 38, 255, cv2.THRESH_OTSU)
    mask_inv = cv2.bitwise_not(mask)
    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask)

    # Take only region of logo from logo image.
    logo_fg = cv2.bitwise_and(im2,im2,mask = mask_inv)

    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg,logo_fg)
    im[0:h, 0:w ] = dst
    return im


img=mask_image(img1, logo)

cv2.imshow('fff',img)
#cv2.imshow('fff',logoGray)
cv2.waitKey()
cv2.destroyAllWindows()