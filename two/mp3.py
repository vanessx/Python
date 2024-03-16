import pygame

pygame.init()
pygame.mixer.music.load('') # escrever aqui o nome do ficheiro .mp3
pygame.mixer.play()
pygame.event.wait()