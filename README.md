# Rune Scape bot
## Overview
### What is this project?

Firstly, I never made this program to profit in or out of the game. When I was younger and used to play this game, I always
wondered how 'bots' worked. Now I've finished my Full Stack course I thought I'd put my new found knowledge to use and try make a bot
myself.

## Features
### Existing Features
- Woodcutting bot:
    - Cuts willows at Dreanor manor and banks them in a loop
    - Drop loop instead
- Attack bot:
    - Attacks the giant rats behind Lumbridge castle
### Future Features
- Woodcutting bot:
    - Cutting Yews
- Mine Bot
- Fletch Bot
- Fishing Bot

## Tech Used
### Some the tech used includes:
- [cv2](https://opencv.org/)
	- we use cv2 to match the triggers with images taken by pyautogui, basically mimicing how a human would see items in game.
- [pyAutoGui](https://pyautogui.readthedocs.io/en/latest/)
    - After matching the images and gettting the coorindates we use pyautogui to use the mouse and keybored to interact with the game 
## Contributing
### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone <project's Github URL>``` command
2. Make sure all dependicies in requirements.txt are all installed
3. The project should be ready to run and work on now! ```python run bot.py```