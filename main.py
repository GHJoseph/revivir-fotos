import webbrowser
import pyautogui
import time
import funciones
import polling

# Abrir una nueva ventana en el navegador
def urlNavegador():
    # Cargar url donde vamos a cargar la imagen
    webbrowser.open("https://algorithmia.com/use-cases")

# Manejador de archivos
#archivo = open("links.txt", "r")
archivo = open("prueba.txt", "r")
lineas = archivo.readlines()
numeroLineas = len(lineas)
archivo.close()

for i in range(numeroLineas):

    # Abrir navegador
    urlNavegador()
    
    # Primer click
    polling.startPolling("./Recursos/photo3.png")           #Polling inicial
    pyautogui.moveTo(594, 306, 2, pyautogui.easeOutQuad)    #Da apariencia que arranca rapido el mouse y luego lento
    pyautogui.scroll(-16)
    pyautogui.click()
    #polling.startPolling("./Recursos/photo4.png")
    
    # Segundo click
    #funciones.asignarClick(214,495)
    #polling.startPolling("./Recursos/photo5.png")
    
    # Escribir en el rectangulo blanco de algorithmia
    #pyautogui.typewrite(lineas[i])
    #pyautogui.press('enter')
    #polling.startPolling("./Recursos/photo6.png")
    
    # Ahora nos movemos un poco hacia abajo, para encontrar el link y descargar la imagen
    #pyautogui.scroll(200) #FALTA DEFINIR BIEN ESE VALOR
    # Encontrar el link de descarga
    #funciones.localizarImagen("./Recursos/photo0.png")
    #polling.startPolling("./Recursos/photo7.png")
    
    # Encontrar la imagen para guardar
    #funciones.localizarImagen("./Recursos/photo1.png")
    # Hay que cersiorarse que este la opcion de guardar
    #funciones.localizarImagen("./Recursos/photo2.png")
    
    # Esto por defecto guardara las imagenes en descargas
