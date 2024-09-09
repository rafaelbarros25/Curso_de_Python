# Faca um programa q abra e reproduza o audio de um arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load("belo.mp3")
pygame.mixer.music.play()
pygame.event.wait()

#  NAO FUNCIONOU, O PYTHON NAO ESTA LENDO O MP3