import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

#Karen Eliana Muñoz Maya
#Anderson Francisco Diaz Ciro
#Carlos Felipe Suarez Rodriguez
#Ingeneiria de Sistemas Octavo Semestre
#Procesamiento de Imagenes

img1 = cv.imread('Imagenes/img6.png', 0)
#Exepcion cuando no se carga la imagen
assert img1 is not None, 'La imagen no se pudo cargar'

alto,ancho = img1.shape

plt.imshow(img1,cmap="gray")
plt.show()

#Cambiar tamaño de imagen
interpVecino = cv.resize(img1,(alto*10,ancho*10),interpolation = cv.INTER_NEAREST)
interpBilineal = cv.resize(img1,(alto*10,ancho*10),interpolation = cv.INTER_LINEAR)
interpBicubica = cv.resize(img1,(alto*10,ancho*10),interpolation = cv.INTER_CUBIC)

plt.subplot(2, 2, 1)
plt.title('Original')
plt.imshow(img1, cmap="gray")

plt.subplot(2, 2, 2)
plt.title('Vecino cercano')
plt.imshow(interpVecino, cmap="gray")

plt.subplot(2, 2, 3)
plt.title('Bilineal')
plt.imshow(interpBilineal, cmap="gray")

plt.subplot(2, 2, 4)
plt.title('Bicubica')
plt.imshow(interpBicubica, cmap="gray")

plt.subplots_adjust(hspace=0.5, wspace=0.5)

plt.show()

print(' ')
print('********************************Crear una nueva imagen********************************')

os.makedirs("imagenes_redimensionadas", exist_ok=True)

for img in os.listdir("ImagenesTaller2"):
    img_data = cv.imread(f"ImagenesTaller2/{img}")
    if img_data is None: continue

    h, w = img_data.shape[:2]
    img_resized = cv.resize(img_data, (int(w * (100 / h)), 100))

    cv.imwrite(f"imagenes_redimensionadas/{os.path.splitext(img)[0]}.png", img_resized)

print("Proceso finalizado.")

