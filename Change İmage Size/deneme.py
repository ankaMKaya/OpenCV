import cv2
import numpy as ny #cv2 vw numpy kütüphanemizi import komutu ile çağırdık ardından as ile numpy kısaltmış olduk.

image = cv2.imread('testimage.jpg')
cv2.imshow('Orijinal Resim', image) 
#Burada ise image ile bir değişken atadık ve cv2 kütüphanesi ile çağırdığımız resmi imread ile okumasını sağladık.
#Daha sonra imshow ile pencere açmasını ve ilk parametrede pencerenin başlığı "Orijinal resim" olarak belirledik.
#image değişkenimizi de 2 parametredi belirtiyoruz ki çağrılan resmi pencere içerisinde göstersin.

down_width = 300
down_height = 200
down_points = (down_width, down_height)
resized_down = cv2.resize(image, down_points, interpolation = cv2.INTER_LINEAR)
# interpolation: Boyut değiştirme işlemi sırasında kullanılan interpolasyon yöntemini belirleyen bir parametre. 
# OpenCV'de çeşitli interpolasyon yöntemleri bulunur ve bunlar arasından birini seçebilirsiniz. Bu örnekte, cv2.INTER_LINEAR yöntemi kullanılmaktadır.
# Interpolasyon, bir nokta kümesi verildiğinde, bilinen değerleri kullanarak bilinmeyen noktaların değerlerini tahmin etme sürecidir. 
# Görüntü boyutunu değiştirirken, interpolasyon yöntemi, yeni boyut için piksellerin değerlerini tahmin etmek için kullanılır.
# cv2.INTER_LINEAR, iki nokta arasında doğrusal bir eğri oluşturur ve bu eğri üzerindeki değerleri kullanarak yeni boyuttaki piksellerin değerlerini tahmin eder. 
# Bu yöntem, genellikle görüntüyü küçültmek veya büyütmek için iyi sonuçlar verir.

up_width = 600
up_height = 400
up_points = (up_width, up_height)
resized_up = cv2.resize(image, up_points, interpolation = cv2.INTER_LINEAR)

cv2.imshow('Resized Down by defining height and width', resized_down)
cv2.waitKey()
cv2.imshow('Resized Up image by defining height and width', resized_up)
cv2.waitKey() #waitkey ile kullanıcı bir tuşa bastığında pencere kapanır.

cv2.destroyAllWindows()