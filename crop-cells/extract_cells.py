import cv2
import imutils
from imutils import contours as cont
import numpy as np

def imshow(title, image, width=800):
    cv2.imshow(title, imutils.resize(image, width=width))
    cv2.waitKey(0)


def threshold(image, invert=False):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Thresholding the image
    thresh, img_bin = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # Invert the image
    if invert: img_bin = 255-img_bin
    return img_bin

def morph(img_bin, kernel, iterations=3):
    img_temp = cv2.erode(img_bin, kernel, iterations=iterations)
    img_lines = cv2.dilate(img_temp, kernel, iterations=iterations)
    return img_lines

def find_boxes(image):
    #convert binary image
    img_bin = threshold(image, invert=True)

    # Defining a kernel length
    kernel_length = np.array(img_bin).shape[1]//40

    # A verticle kernel of (1 X kernel_length), to detect all the verticle lines.
    verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
    # A horizontal kernel of (kernel_length X 1), to detect all the horizontal lines.
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))

    verticle_lines = morph(img_bin, verticle_kernel)
    horizontal_lines = morph(img_bin, horizontal_kernel)
    boxes = cv2.add(verticle_lines, horizontal_lines)

    return boxes

def over_draw_boxes(img_bin):
    minLineLength=100
    lines = cv2.HoughLinesP(image=img_bin,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)
    for i in range(lines.shape[0]):
        cv2.line(img_bin, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (255, 255, 255), 2, cv2.LINE_AA)

    return img_bin



img = cv2.imread("input1.jpg")
#img = cv2.imread("input2.png")

#resizing image
img = imutils.resize(img, width=2564)
img_original = img.copy()

boxes = find_boxes(img)
boxes = over_draw_boxes(boxes)


contours, _ = cv2.findContours(boxes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#_, contours, _ = cv2.findContours(boxes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

(contours, boundingBoxes) = cont.sort_contours(contours, method="left-to-right")
(contours, boundingBoxes) = cont.sort_contours(contours, method="top-to-bottom")

idx = 0
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    if (w > 30 and h > 20) and w > 1*h:
        #rectangular contours
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        img = cv2.drawContours(img, [box], 0, (0,0,255), 3)


        #cell mappings
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        center = (cx, cy+20)
        if idx!=0:
            cv2.putText(img, str(idx), center, cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
            cv2.imwrite("cropped/0.jpg", img)

        #cropped cell
        cell = img_original[y:y+h, x:x+w]
        cv2.imwrite("cropped/"+str(idx)+".jpg", cell)

        imshow("image", img)
        idx+=1
