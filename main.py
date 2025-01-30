import cv2
import numpy as np

img_path = "/Users/lxiaodoh/PycharmProjects/tufting/Picture1.png"
output_path = "/Users/lxiaodoh/PycharmProjects/tufting/dog_output.jpeg"

img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.bilateralFilter(gray, 9, 75, 75)
edges = cv2.Canny(blur, 10, 30)
kernel = np.ones((3, 3), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=1)
contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros_like(gray)
cv2.drawContours(mask, contours, -1, 255, -1)
cv2.imwrite(output_path, mask)
