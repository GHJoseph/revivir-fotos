# revivir-fotos
Dar color a imágenes en blanco y negro de épocas de antaño con ayuda de Deep Learning. 

# Introducción

Imagina la foto de boda de tus abuelos o bisabuelos que posiblemente está en blanco y negro, ¿no te da curiosidad saber cuáles eran los colores de los vestidos o trajes de ellos? ¿cómo era el color de la decoración?.

También imagina fotos de museos muy antigüas, ¿no te gustaría ver el contexto a color y ver cómo era la vida en esos tiempos?. 

Ver fotografías de la primera guerra mundial a color y ver cómo era la situación realmente. 

**Éstas y muchas cosas más me motivaron a investigar sobre el tema.**

# Contexto

Hay una librería que realiza ésto automáticamente en python llamada ´´´algorithmia´´´. Tenés que instalarla definir varias variables de entorno, key_acces y muchas cosas más. Sino estas familiarizado con eso, posiblemente sea un dolor de cabeza en un principio definirlas correctamente. 

Por eso, cree un script en python que analiza un archivo de texto (que obtuve haciendo web scrapping a un repositorio llamado LILKAYA), posteriormente guarda esos links de las imágenes que quiero en ese archivo. Luego mediante la automatización de procesos con pyautogui busca en el navegador un demo de algorithmia, carga los links, procesa y guarda la imágenes.

# Resultados

