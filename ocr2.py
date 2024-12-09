import cv2 as cv 
import pytesseract as ps 

ps.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv.imread('advert.jpg')

img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

ht,wt = img.shape[:2]

boxes = ps.image_to_boxes(img_rgb)

for box in boxes.splitlines():
    box = box.split()
    
    (text,x,y,w,h) = (box[0], int(box[1]), int(box[2]), int(box[3]), int(box[4]))
    cv.rectangle(img, (x,ht-y), (w,ht-h), (0,0,255))
    
    #display each letter on top of each
    cv.putText(img, text, (x,ht-y-30), cv.FONT_HERSHEY_PLAIN, 2, (255,0,0),2)

cv.imshow("image", img)
cv.waitKey()
