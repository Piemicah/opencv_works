import pytesseract
import cv2 as cv 

img= cv.imread('cell.JPG')
rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)

ih,iw=img.shape[:2]

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#img_str= pytesseract.image_to_string(rgb)
img_box = pytesseract.image_to_boxes(rgb)

boxes = img_box.splitlines()

for box in boxes:
    box=box.split()
    
    (text,x,y,w,h)=box[0],int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv.rectangle(img, (x,ih-y), (w,ih-h), (255,0,0))
    cv.putText(img, text,(x,ih-y+20), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0),2)
cv.imshow("hhhh", img)
cv.waitKey()
