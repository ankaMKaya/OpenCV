import cv2

resim = cv2.imread('testimage.png')

height, width = resim.shape[:2]

center = (width/2, height/2)

dndrme_matrisi = cv2.getRotationMatrix2D(center=center, angle=45, scale=1)

dndrlms_resim = cv2.warpAffine(src=resim, M=dndrme_matrisi, dsize=(width, height))

cv2.imshow('Döndürülen resim', resim)
cv2.imshow('Döndürülmüş resim', dndrlms_resim)
cv2.waitKey(0)

cv2.imwrite('Dönderilmiş kopya resim', dndrme_matrisi)