import cv2

img = cv2.imread("agac.jpg")

pixel = img[30:100, 100:200]
cv2.rectangle(img, (100,30), (200,120), (255,255,0), 4) #cv.rectangle("görsel veri","1.nokta", "2.nokta", "renk tonu", "dikdörtgen kalınlığı")
cv2.imshow("agac",img)

cv2.waitKey()
cv2.destroyAllWindows()