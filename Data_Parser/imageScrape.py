import numpy as np
import cv2
from PIL import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
from pytesseract import Output


def test():
    img = cv2.imread('report2.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 300, apertureSize=3)
    cv2.imshow("canny", edges)
    minLineLength = 25
    maxLineGap = 100
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("houghlines", img)
    cv2.waitKey(delay=0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    test()
