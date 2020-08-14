# revivir-fotos
Dar color a imágenes en blanco y negro de épocas de antaño con ayuda de Deep Learning con la automatización de pyautogui. 

# Introducción

Imagina la foto de boda de tus abuelos o bisabuelos que posiblemente está en blanco y negro, ¿no te da curiosidad saber cuáles eran los colores de los vestidos o trajes de ellos? ¿cómo era el color de la decoración?.

También imagina fotos de museos muy antigüas, ¿no te gustaría ver el contexto a color y ver cómo era la vida en esos tiempos?. 

Ver fotografías de la primera guerra mundial a color y ver cómo era la situación realmente. 

**Estas y muchas cosas más me motivaron a investigar sobre el tema.**

# Contexto

Hay una librería que realiza ésto automáticamente en python llamada ```algorithmia```. Tenés que instalarla definir varias variables de entorno, key_acces y muchas cosas más. Sino estas familiarizado con eso, posiblemente sea un dolor de cabeza en un principio definirlas correctamente. 

Por eso, cree un script en python que analiza un archivo de texto (que obtuve haciendo web scrapping a un repositorio llamado _LILKAYA_), posteriormente guarda esos links de las imágenes que quiero en ese archivo. Luego mediante la automatización de procesos con pyautogui busca en el navegador un demo de algorithmia, carga los links, procesa y guarda la imágenes.

# Resultados post-curado

![compara1](https://github.com/cabustillo13/revivir-fotos/blob/master/Ejemplos/comparar1.png)

![compara0](https://github.com/cabustillo13/revivir-fotos/blob/master/Ejemplos/comparar0.png)

![compara2](https://github.com/cabustillo13/revivir-fotos/blob/master/Ejemplos/comparar2.png)

# Fuente de las imágenes

Todas las imágenes fueron obtenidas del respositorio [LILKAYA](https://lilkaya.unah.edu.hn/) de la Universidad Nacional Autónoma de Honduras. 

Ese repositorio contiene muchas imágenes y documentos obtenidos de Fototecas, museos y más de Honduras.

# Programas

**funciones.py**

Contiene todas las funciones auxiliares para el manejo de teclado, mouse y pantalla.

**polling.py**

_El polling hace referencia a una operación de consulta constante, generalmente hacia un dispositivo de hardware, para crear una actividad sincrónica sin el uso de interrupciones, aunque también puede suceder lo mismo para recursos de software._

Permite tener control de los comandos al hacer ésto, también adaptarde a las distintas velocidades de descarga de la computadora para cada caso.

**main.py**

Es el core del proyecto, acá se analiza todos los links cargados, y se obtiene su correspondiente imagen a color. El algoritmo utiliza el deep learning para clasificar objetos / regiones dentro de la imagen y colorearlos en consecuencia.

# Funcionamiento

Ejecute en su terminal: ```python main.py```

Acto siguiente su computadora va a tomar control del mouse, teclado, navegador y pantalla. **Va a parecer que su computadora cobrará vida propia.**

# Preguntas y respuestas

**¿Es lento este proceso?** 

No. Al ejecutar el programa tiene varios delays de 1 segundo para poder apreciar cada etapa, una vez que se apreció y entendió cómo funciona el programa se les puede quitar ese delay para que tenga su funcionamiento óptimo. También se puede alcanzar un mayor rendimiento utilizando acortadores de url como **bit.ly** para que ingrese más rápido el link. 

**¿Cuándo utilizar este programa?** 

Cuando tengas una cantidad relativamente grande de imágenes (unas 100 imágenes en adelante considero) y tengas muy ṕoca noción de variables de entorno, configuración de access_key, etc. Sí crees que tenes los conocimientos necesarios y tenés una alta carga de datos mejor implementa la librería.

Se puede correr éstos programas desde una Raspberry u otro microprocesador para realizar acciones automáticas con la menor cantidad de recursos y energía.

**¿Puedo correr este programa directamente en mi computadora?**

Como use pyautogui definí sus valores en función de mi teclado (uso QWERTY español), mouse, pantalla(1366x768) y navegador(Firefox). Así que deberías leer el código y adaptarlo a tu equipo.

**¿Qué otros usos puedo usar las funciones de polling.py y funciones.py?** 

* Puede ser un gran ejercicio para aprender pyautogui porque prácticamente involucra muchos de sus comandos.

* Detectar un reCAPTCHA y cargar los datos de un usuario.

* Detectar elementos de Tinder para hacer match! de manera automática.

* Responder a comentarios de venta en Facebook.

# ¡Ojalá hayas disfrutado del código!
