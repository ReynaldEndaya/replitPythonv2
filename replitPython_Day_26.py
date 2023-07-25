from replit import audio
import os, time


def play():
  source = audio.play_file('audio.wav')
  source.paused = False  # unpause the playback
  while True:
    # Start taking user input and doing something with it
    input()


while True:
  # clear the screen
  os.system("clear")

  # Show the menu
  print('MyPOD Music Player')
  print()
  print('''Press 1 to Play
Press 2 to Exit''')

  # take user's input
  print()
  userChoice = input()

  # check whether you should call the play() subroutine depending on user's input
  if userChoice == '1':
    play()
  else:
    break