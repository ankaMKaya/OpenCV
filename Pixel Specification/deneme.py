import cv2

img = cv2.imread("agac.jpg")

pixel = img[30:100, 100:200]
cv2.imshow("agac2",pixel)
cv2.imshow("agac",img)

cv2.waitKey()
cv2.destroyAllWindows()