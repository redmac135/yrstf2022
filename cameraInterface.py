import cv2 as cv
from pytesseract import pytesseract

camera = cv.VideoCapture(0)
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
tmp_img_path = "test.jpg"

pytesseract.tesseract_cmd=path_to_tesseract

threshold = 127
detection = False

def __draw_label(img, text, pos, bg_color):
   font_face = cv.FONT_HERSHEY_SIMPLEX
   scale = 0.7
   color = (0, 0, 0)
   thickness = cv.FILLED
   margin = 2
   txt_size = cv.getTextSize(text, font_face, scale, thickness)

   end_x = pos[0] + txt_size[0][0] + margin
   end_y = pos[1] - txt_size[0][1] - margin

   cv.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
   cv.putText(img, text, pos, font_face, scale, color, 1, cv.LINE_AA)

def __draw_highlight_char(frame, box, imgH):
    x,y,w,h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv.rectangle(frame, (x, imgH - y), (w, imgH - h), (0,0,255), 3)

while True:
    # get the camera imput
    ret, frame = camera.read()
    imgH, imgW, _ = frame.shape
    x1, y1, w1, h1 = 0, 0, imgH, imgW

    # Raw Logic
    rawframe = frame.copy()
    if detection:
        rawboxes = pytesseract.image_to_boxes(rawframe)
        for box in rawboxes.splitlines():
            box = box.split(" ")
            __draw_highlight_char(rawframe, box, imgH)
    cv.imshow('Raw Input', rawframe)

    # Black and White Logic
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteFrame) = cv.threshold(grayFrame, threshold, 255, cv.THRESH_BINARY)
    if detection:
        blackAndWhiteboxes = pytesseract.image_to_boxes(blackAndWhiteFrame)
        for box in blackAndWhiteboxes.splitlines():
            box = box.split(" ")
            __draw_highlight_char(blackAndWhiteFrame, box, imgH)
    __draw_label(blackAndWhiteFrame, str(threshold), (0, 20), (255,0,0))
    cv.imshow('Black and White', blackAndWhiteFrame)

    if cv.waitKey(1) == ord('a'):
        threshold += 5
    if cv.waitKey(1) == ord('d'):
        threshold -= 5

    # Toggle Detection
    if cv.waitKey(1) == 32:
        detection = not detection

    if cv.waitKey(1) == ord('s'):
        text = pytesseract.image_to_string(rawframe)
        print(text)

    # When Esc key hit, break
    if cv.waitKey(1) == 27:
        break

camera.release()
cv.destroyAllWindows()