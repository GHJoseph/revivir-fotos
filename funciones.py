import pyautogui

# Determinar posicion del mouse para dar un click
# Sirve para asignas las posiciones de cada click, una vez cargadas a las demas funciones ya no lo volvemos a utilizar 
def posicionPuntero():
    time.sleep(10)                 #Esperar 10 segundos
    print(pyautogui.position())    #Capturar posicion del mouse

# Hacer click en las coordenadas encontradas
def asignarClick(valorx,valory):
    pyautogui.click(valorx, valory)

# Localizar imagen para darle click
def localizarImagen(pathImagen):
    # Ingresar imagen que debemos buscar
    buscarlocation = pyautogui.locateOnScreen(pathImagen)
    # Posiciones donde se encuentra el elemento buscado
    buscarpoint = pyautogui.center(buscarlocation)
    buscarx, buscary = buscarpoint
    # Hacer click en las coordenadas encontradas
    pyautogui.click(buscarx, buscary)

