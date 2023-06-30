
import cv2

ilk_resim = cv2.imread("agac.jpg", 0)

# cv2.imshow("agac", ilk_resim)

# cv2.waitKey()
# cv2.destroyAllWindows()

ilk_resim[:,:,1] = 0

cv2.imshow("agac", ilk_resim)

cv2.waitKey()
cv2.destroyAllWindows()
