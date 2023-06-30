
# DAİRE ÇİZME

import cv2

# Read Images
img = cv2.imread('sample.jpg')

# Display Image
cv2.imshow('Original Image', img)
cv2.waitKey(0)

# Make a copy of image
imageCircle = img.copy()
# define the center of circle
circle_center = (415,190)
# define the radius of the circle
radius =100
#  Draw a circle using the circle() Function
cv2.circle(imageCircle, circle_center, radius, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA) 
# Display the result
cv2.imshow("Image Circle",imageCircle)
cv2.waitKey(0)

# ÇİZGİ ÇİZME

import cv2

# Read Images
img = cv2.imread('sample.jpg')

# Display Image
cv2.imshow('Original Image', img)
cv2.waitKey(0)

# Print error message if image is null
if img is None:
    print('Could not read image')

# Draw line on image
imageLine = img.copy()

# Define the points A and B
pointA = (200, 80)
pointB = (450, 80)

# Draw the line from point A to B
cv2.line(imageLine, pointA, pointB, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)

cv2.imshow('Image Line', imageLine)
cv2.waitKey(0)

METİN EKLEME

import cv2

# Read Images
img = cv2.imread('sample.jpg')

# Display Image
cv2.imshow('Original Image', img)
cv2.waitKey(0)

# make a copy of the original image
imageText = img.copy()
#let's write the text you want to put on the image
text = 'I am a Happy dog!'
#org: Where you want to put the text
org = (50,350)
# write the text on the input image
cv2.putText(imageText, text, org, fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 1.5, color = (250,225,100))
# display the output image with text over it
cv2.imshow("Image Text",imageText)
cv2.waitKey(0)
cv2.destroyAllWindows()
