import os
import sys

import pygame
from rich import json

from models import Asteroid, Spaceship
from Globals import Globals
from MUtils import mUtils
from manager import GameManager
from utils import get_random_position, load_sprite, print_text, mykwargs, load_sound
from pygame.math import Vector2

from urllib.request import urlopen

class SpaceRocks:
    MIN_ASTEROID_DISTANCE = 250

    def __init__(self):
        """
        Example: python __main__.py queue=game-01 player=player-01
        """
        url = "https://terrywgriffin.com/current_usage.json"
        response = urlopen(url)
        data_json = json.loads(response.read())
        if len(data_json['players']) >= 10:
            print(data_json['players'])
            print("max users exceed!")
            exit(111)

        args, kwargs = mykwargs(sys.argv)

        queue = kwargs.get("queue", None)
        playerId = kwargs.get("player", None)
        creds = {
            "exchange": queue,
            "port": "5672",
            "host": "terrywgriffin.com",
            "user": playerId,
            "password": playerId + "2023!!!!!",
        }

        self._init_pygame()
        mUtils.initDeltaTime()
        self.asteroids = []
        self.bullets   = []

        self.manager = GameManager(self.bullets.append)
        localSpaceShip = Spaceship((400,400),None,None,self.bullets.append,
           id=playerId,creds=creds, callback=self.manager.callBack)
        
        self.manager.addPlayer(None,None,player=localSpaceShip, localPlayer=True)
        
        # set the window title
        pygame.display.set_caption(f"{creds['user']}")

        # Background
        self.background = load_sprite("Aqua", False)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 64)
        self.message = ""
        self.gameStatus = "playing"


        self.spaceship = localSpaceShip
        self.explosion_sound = load_sound("explosion")

     


        # Generate asteroid
        for _ in range(2):
            while True:
                position = get_random_position(mUtils.screen)
                if (
                    position.distance_to(self.spaceship.position)
                    > self.MIN_ASTEROID_DISTANCE
                ):
                    break
        
            self.asteroids.append(Asteroid(position, self.asteroids.append))

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")

    def _handle_input(self):
        if self.gameStatus == "lose":
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()
            elif (
                self.spaceship
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                self.spaceship.sendShoot()
                self.spaceship.shoot(self.spaceship.angle)
                if self.spaceship.activeBulletSkill:
                    self.spaceship.shoot(self.spaceship.angle - 5)
                    self.spaceship.shoot(self.spaceship.angle + 5)

        is_key_pressed = pygame.key.get_pressed()

        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
                self.spaceship.updateData()
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
                self.spaceship.updateData()
            if is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate(1)
                self.spaceship.updateData()
            if is_key_pressed[pygame.K_DOWN]:
                self.spaceship.accelerate(-1)
                self.spaceship.updateData()
            if is_key_pressed[pygame.K_m]:
                self.spaceship.stop()

    def _process_game_logic(self):
        mUtils.initDeltaTime()
      

        self.manager.update(mUtils.screen)

        for game_object in self._get_game_objects():
            game_object.move(mUtils.screen)


        for id,player in self.manager.players.items():
            for bullet in self.bullets[:]:
                if bullet.collides_with(player) and bullet.id != id:
                    self.bullets.remove(bullet)
                    break

        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                if asteroid.collides_with(bullet):
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    asteroid.split()
                    break


        # Here if the player hit collide with the asteroids he lose 10 points and make noise.        
        if self.spaceship:
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    self.spaceship.health -= 2
                    self.explosion_sound.play()

                    self.spaceship.updateData()
                    self.asteroids.remove(asteroid)
                    asteroid.split()
                    break
                
       


        for bullet in self.bullets[:]:
                if bullet.collides_with(self.spaceship) and bullet.id != self.spaceship.id:
                    self.spaceship.getHit(int(bullet.damage))
                    self.spaceship.updateData(scoreTo=bullet.id)
                    self.bullets.remove(bullet)
                    break

        for bullet in self.bullets[:]:
            if not mUtils.screen.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)


        if self.spaceship.destroy:
            self.spaceship.updateData()
            self.message = "!!!GameOver!!!"
            self.gameStatus = "lose"


    def _draw(self):
        mUtils.screen.blit(self.background, (0, 0))

        self.manager.draw(mUtils.screen)

        for game_object in self._get_game_objects():
            game_object.draw(mUtils.screen)
            
        

        if self.message:
            print_text(mUtils.screen, self.message, self.font)

        self.drawScoreTable()

        pygame.display.flip()
        self.clock.tick(60)

    def drawScoreTable(self):
        mUtils.drawText(pygame.Vector2(680,20), self.spaceship.id + ": " + str(self.spaceship.score),(255,253,34),12)
        
        y = 20
        for id, player in self.manager.players.items():
            if id == self.spaceship.id:
                continue
            mUtils.drawText(pygame.Vector2(20, y),player.id + ": " + str(player.score), (255, 253, 233), 12)
            y += 20

    def _get_game_objects(self):
        game_objects = [*self.asteroids, *self.bullets]

        if self.spaceship:
            game_objects.append(self.spaceship)

        return game_objects
