import cv2
import matplotlib
import numpy

img = cv2.imread('./images/ornek.png', cv2.IMREAD_UNCHANGED)
genislik = img.shape[0]//2
yukseklik = img.shape[1]//2
minik = cv2.resize(img, (genislik,yukseklik),cv2.INTER_NEAREST)
cv2.imshow('Siftah', img)
cv2.imshow('Minik', minik)
print("Resmin Boyutları:",img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()