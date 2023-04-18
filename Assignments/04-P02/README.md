# Space Fight!

## Venkata Nageswar Reddy Nandipati, Thivya Tanneedi

## Description:

This is a two-player game created using the Pygame library in Python. The game involves two spaceships, one controlled by the red player and 
one by the green player. The objective of the game is to shoot the opponent until its health reaches zero. The game has sound effects 
for firing bullets and getting hit by them. The health of each spaceship is displayed on the screen. The game is played on a background image 
of space. The game ends when one of the spaceships runs out of health, and the winner is declared on the screen for 5 seconds before the game restarts.

The project is a basic implementation of a two-player game using Pygame library in Python. The game window has a width of 900 pixels and a height of 500 pixels. The game window has a person image, and on the right side, there is another person image. These spaceships can be controlled by the players to move in four directions - up, down, left, and right.

The game includes sound effects for bullet hits and bullet fires, which are loaded from external audio files. Also, includes two fonts for displaying health and winner messagesThe game runs at a frame rate of 60 frames per second (FPS) and defines the velocity (VEL) of the spaceships as 5 pixels per frame. The velocity of bullets (BULLET_VEL) is set to 7 pixels per frame, and the maximum number of bullets allowed on the screen (MAX_BULLETS) is set to 3.

The game window displays a background image of space that covers the entire window. The health of both spaceships is displayed at the top-right corner (for red spaceship) and top-left corner (for yellow spaceship) of the window using the HEALTH_FONT. The health values are dynamically updated during the game.

The game includes functions to handle movement of the yellow and red spaceships based on the keys pressed by the players. It also includes functions to handle bullets fired by the spaceships. The bullets are represented as rectangles on the screen, with red bullets for the yellow spaceship and green bullets for the red spaceship.

The game also includes a function to display the winner of the game using the WINNER_FONT. The text of the winner is centered on the screen based on the width and height of the game window.

