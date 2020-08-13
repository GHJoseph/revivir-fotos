#Esto me sirve cuando carga la imagen una por una en vez de subir los link
import cv2
import numpy as np

#Ingresar numero de la foto
numero="2"

#Imagen inicial de referencia antes de agregarle un margen con photopea a la imagen
img = cv2.imread("original"+numero+".png")
alto,ancho,canales=img.shape

#Cargar imagen con borde rojo para recortar a las dimensiones de la original
imagen = cv2.imread("photo"+numero+".png")

#Recortar imagen
crop_img = imagen[0:alto, 0:ancho]
#Renombrar imagen con los cambios
renombre="foto"+numero+".png"
cv2.imwrite(renombre, crop_img)

#Concatenar imagenes
comparacion=np.concatenate((img,crop_img),axis=1)
renombre="comparar"+numero+".png"
cv2.imwrite(renombre, comparacion)
