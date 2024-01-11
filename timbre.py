import os
import time
from datetime import datetime, timedelta
import pygame

def reproducir_musica(ruta_carpeta):
    archivos = os.listdir(ruta_carpeta)
    archivos_mp3 = [archivo for archivo in archivos if archivo.endswith(".mp3")]

    if not archivos_mp3:
        print("No se encontraron archivos MP3 en la carpeta especificada.")
        return

    pygame.init()
    pygame.mixer.init()

    for archivo_mp3 in archivos_mp3:
        pygame.mixer.music.load(os.path.join(ruta_carpeta, archivo_mp3))
        print(f"Reproduciendo: {archivo_mp3}")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Controla la frecuencia de verificación del estado de reproducción

def programar_reproduccion(hora_programada, ruta_carpeta):
    while True:
        ahora = datetime.now()
        if ahora.hour == hora_programada.hour and ahora.minute == hora_programada.minute:
            print(f"Es hora de reproducir música: {ahora}")
            reproducir_musica(ruta_carpeta)
            break
        else:
            time.sleep(30)  # Revisa cada 30 segundos si es la hora programada

# Configura la hora a la que deseas que comience la reproducción
hora_programada = datetime.now() + timedelta(minutes=1)  # Ejemplo: empieza en 1 minuto
hora_programada = hora_programada.replace(second=0, microsecond=0)  # Ajusta a la siguiente hora exacta
print(f"Programando la reproducción a las {hora_programada.hour}:{hora_programada.minute}")

ruta_musica = "ruta/a/tu/carpeta/musica"  # Reemplaza con la ruta correcta a tu carpeta de música

programar_reproduccion(hora_programada, ruta_musica)
