import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import cv2 as cv

#Karen Eliana Muñoz Maya
#Anderson Francisco Diaz Ciro
#Carlos Felipe Suarez Rodriguez

print(' ')
print('********************************Ancho y el alto de la imagen de la imagen********************************',)
img1 = cv.imread('Imagenes/Fondo.jpg', 0)
alto,ancho = img1.shape

plt.imshow(img1,cmap="gray")
plt.show()


#Para ver el valor del largo y ancho de la imagen
print('El Largo es: ', ancho, 'y el Ancho es: ', alto, img1.shape)

print(' ')
print('********************************Valor de intensidad máximo y el valor de intensidad mínimo de la imagen********************************')
# Obtener el valor mínimo y máximo de intensidad y sus ubicaciones
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(img1)
# print(min_val, max_val, min_loc, max_loc)
print('El valor minimo es: ', min_val, 'y el valor maximo es: ', max_val)

print(' ')
print('********************************Coordenadas del pixel central pc********************************')

pc_x = ancho // 2
pc_y = alto // 2

# Mostrar las coordenadas
print(f"Coordenadas del píxel central: ({pc_x}, {pc_y})")
print(' ')

#********************************Reducir la imagen a 8 niveles de intensidad********************************
niveles = 8
imagen_8niveles = (img1 // (256 // niveles)) * (256 // niveles)

# Mostrar la imagen original y la imagen con menor resolución
plt.figure(figsize=(20, 10))

# Imagen original
plt.subplot(1, 2, 1)
plt.imshow(img1, cmap='gray')
plt.title("Imagen Original")

# Imagen con 8 niveles
plt.subplot(1, 2, 2)
plt.imshow(imagen_8niveles, cmap='gray')
plt.title("Imagen con 8 Niveles")

plt.show()

print(' ')
print('********************************Crear una nueva imagen********************************')
# Parámetro de distancia máxima
limite = 30

# Funciones de distancia
manhattan = lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2)
euclidiana = lambda x1, y1, x2, y2: max(abs(x1 - x2), abs(y1 - y2))

# Dimensiones de la imagen
alto, ancho = img1.shape

# Punto central
pc_x, pc_y = alto // 2, ancho // 2

# Crear copias de la imagen
img_d4 = img1.copy()
img_d8 = img1.copy()

# Aplicar condiciones de distancia
for x in range(alto):
    for y in range(ancho):
        if manhattan(x, y, pc_x, pc_y) > limite:
            img_d4[x, y] = 0
        if euclidiana(x, y, pc_x, pc_y) > limite:
            img_d8[x, y] = 0

# Mostrar imágenes resultantes
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

titulos = ["Distancia D4", "Distancia D8"]
imagenes = [img_d4, img_d8]

for i in range(2):
    ax[i].imshow(imagenes[i], cmap="gray", vmin=0, vmax=255)
    ax[i].set_title(titulos[i])
    ax[i].axis("off")

plt.tight_layout()
plt.show()