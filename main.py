import cv2
import numpy as np

image1 = cv2.imread("1.jpg")
image2 = cv2.imread("2.jpg")
image3 = cv2.imread("3.jpg")

image1 = cv2.resize(image1, (800, 600))
image2 = cv2.resize(image2, (800, 600))
image3 = cv2.resize(image3, (800, 600))

difference = cv2.absdiff(image1, image2)

gray_difference = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

if np.sum(gray_difference) <= 0:
    print("Images are similar")
else:
    print("Images are different")

cv2.imshow('Difference', gray_difference)
cv2.waitKey(0)
cv2.destroyAllWindows()
