import cv2
import numpy as np

resim2 = cv2.imread('test.jpg')

resim1 = cv2.imread('test.jpg')
image_copy = resim1.copy()
resim1height = resim1.shape[0]
resim1width = resim1.shape[1]

cv2.imshow("orginal", resim2)
cv2.waitKey(0)
cv2.imshow("kopyalanan", resim1)
cv2.waitKey(0)
cv2.destroyAllWindows()

M = 76
N = 104
x1 = 0
y1 = 0
 
for y in range(0, resim1height, M):
    for x in range(0, resim1width, N):
        if (resim1height - y) < M or (resim1width - x) < N:
            break

        y1 = y + M
        x1 = x + N
 
        # check whether the patch width or height exceeds the image width or height
        if x1 >= resim1width and y1 >= resim1height:
            x1 = resim1width - 1
            y1 = resim1height - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(resim1, (x, y), (x1, y1), (0, 255, 0), 1)
        elif y1 >= resim1height: # when patch height exceeds the image height
            y1 = resim1height - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(resim1, (x, y), (x1, y1), (0, 255, 0), 1)
        elif x1 >= resim1width: # when patch width exceeds the image width
            x1 = resim1width - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(resim1, (x, y), (x1, y1), (0, 255, 0), 1)
        else:
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(resim1, (x, y), (x1, y1), (0, 255, 0), 1)


cv2.imshow("kırpılan resim",resim1)
cv2.imwrite("kırpılmış resim",resim1)
cv2.waitKey()
cv2.destroyAllWindows()