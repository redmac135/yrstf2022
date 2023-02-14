import cv2 as cv
from PIL import Image
from pytesseract import pytesseract

camera = cv.VideoCapture(0)
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
tmp_img_path = "test.jpg"

pytesseract.tesseract_cmd=path_to_tesseract

while True:
    _, image = camera.read()
    cv.imshow('Image to Text', image)
    if cv.waitKey(1) & 0xFF==ord('s'):
        cv.imwrite(tmp_img_path, image)
        break

camera.release()
cv.destroyAllWindows()

text = pytesseract.image_to_string(Image.open(tmp_img_path))
print(text)