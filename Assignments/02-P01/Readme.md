

## Tetris
### Venkata Nageswar Reddy Nandipati, Revanth Rajaboina
### Description:
This code is an implementation of the classic game Tetris using Pygame, a popular Python library for game development. Tetris is a tile-matching puzzle game where players manipulate falling blocks to create complete rows, which are then cleared from the game board.


The code starts by importing the required libraries, pygame and random. Pygame is a library for writing video games in Python, and random is used to generate random numbers for various game features.
- Make sure you install library pygame using `pip install pygame`

    - `python main.py`


### Files

|   #   | File                                              | Description                                        |
| :---: | ------------------------------------------------- | -------------------------------------------------- |
|   1   |[Main.py](/Assignments/02-P01/Readme.md)           | Main driver of my project that launches game.      |
|   2   |[Screenshots](/https://github.com/nageswarnandipati/5443-2D-nandipati/tree/main/Assignments/02-P01/Screenshots) | Screenshots of game window |
  

[Main.py](/Assignments/02-P01/Readme.md) has three classes: Tetris, Block, MySprite. 
Class MySprite, which was inherited from pygame.sprite.Sprite. This class represents the main character sprite in the game and loads a series of images to be used as animation frames for the character's walking animation.

Block class represents the individual blocks that make up the Tetris game pieces. This class has properties like x and y coordinates, block types, colors, and rotations. It also has methods to initialize the block, get the current Tetris block, rotate the block, and check for collisions with other blocks on the game field.

Tetris class represents the main game logic. It has properties like level, score, state, field, height, width, block, and others. The Tetris class has methods to initialize the game field, create a new block, check for collisions, remove lines, move the block, update the game state, and draw the game field and sprites on the screen.





