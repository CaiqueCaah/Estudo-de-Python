# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O AÚDIO DE UM ARQUIVO MP3
#import playsound
#playsound.playsound('ex021.mp3')
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
