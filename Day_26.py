import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()
pygame.mixer.pause()

def pause():
  pygame.mixer.pause()

pause()

def play():
              # Play the sound
  pygame.mixer.unpause()
  while True:
    stop_playback = int(input("Press 2 to pause playback: "))   # Pause and return to menu 
    if stop_playback == 2:
      pause()
      return         # let's go back from this play() subroutine
    else:
      continue

while True:
  os.system("clear")
  print("My Music Player")
  time.sleep(1)
  print("Press 1 to Play")
  print("Press 2 to Exit")
  print("Press anything else for return the menu")
  userInput = int(input())
  if userInput == 1:
    print("Playing..........🎶🎶🎶🎶🎶🎶")
    play()             # call play function 
  elif userInput == 2:
    exit()
  else:
    continue
