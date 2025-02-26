import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('Imagenes/Fondo.jpg', 0)
#Exepcion cuando no se carga la imagen
assert img1 is not None, 'La imagen no se pudo cargar'

alto,ancho = img1.shape

img_crop1 = img1[:alto//2,:].copy()
img_crop2 = img1[alto//2:,:].copy()


plt.subplot(2, 1, 1)
plt.imshow(img_crop1,cmap="gray")

plt.subplot(2, 1, 2)
plt.imshow(img_crop2,cmap="gray")

plt.show()

#Cambiar tamaño de imagen
img_resized = cv.resize(img1,(200,400),interpolation = cv.INTER_NEAREST)

plt.subplot(1, 2, 1)
plt.imshow(img1,cmap="gray")

plt.subplot(1, 2, 2)
plt.imshow(img_resized,cmap="gray")
plt.show()

imgx2 = cv.resize(img1, None, fx = 2, fy=2, interpolation=cv.INTER_CUBIC)
imgx3 = cv.resize(img1, None, fx = 3, fy=3, interpolation=cv.INTER_LANCZOS4)


cv.imshow('Original',img1)
cv.waitKey(0)

cv.imshow('x2',imgx2)
cv.waitKey(0)
cv.imshow('x2',imgx3)
cv.waitKey(0)

#Rotar una imagen

dst = cv.flip(img1, 0) #dst = cv.flip(img1, flipCode) 0->Voltar eje X  1->voltear eje y -1->voltear ambos ejes
cv.imshow('x2',dst)
cv.waitKey(0)