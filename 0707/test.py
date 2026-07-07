import pygame
import time

pygame.init()

try:
    pygame.mixer.music.load("news_Son.mp3")
    pygame.mixer.music.play()

    print("재생 중...")

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

except Exception as e:
    print("오류:", e)

finally:
    pygame.quit()