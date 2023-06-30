import cv2
import numpy as np

resim = cv2.imread('testimage.jpg')

print(resim.shape)

cropped_resim = resim[80:280, 150:330]

cv2.imshow("original", resim)
cv2.waitKey(0)
cv2.imshow("cropped", cropped_resim)
cv2.waitKey(0)