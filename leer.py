from gtts import gTTS
import pygame
import time

def reproducir_texto_voz(texto):
    # Convertir el texto en voz utilizando gTTS
    tts = gTTS(text=texto, lang='es')
    tts.save('voz_temp.mp3')  # Guardar el archivo de voz temporal
    '''
    # Inicializar pygame
    pygame.mixer.init()
    pygame.mixer.music.load('voz_temp.mp3')

    # Reproducir la voz y controlar la reproducción y pausa
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        comando = input("Ingresa 'pausa' para pausar o 'reproducir' para reanudar: ")
        if comando.lower() == 'pausa':
            pygame.mixer.music.pause()
        elif comando.lower() == 'reproducir':
            pygame.mixer.music.unpause()

    # Limpiar después de la reproducción
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    '''

texto_a_reproducir = ''
nombre_archivo = "lectura.txt"
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        texto_a_reproducir += linea.strip()

reproducir_texto_voz(texto_a_reproducir)
