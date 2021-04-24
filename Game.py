from constants.BackgroundConstants import BackgroundConstants
from constants.PlayerConstants import PlayerConstants
from background.MovingBackground import MovingBackground
from background.VaccineBackground import VaccineBackground
from player.Player import Player
from obstacle.Obstacles import Obstacles
from obstacle.Box import Box
from obstacle.Boxes import Boxes 
from collision.ObstacleCollision import ObstacleCollision
from obstacle.LShapedObstacle import LShapedObstacle
from virus.Virus import Virus
from collision.VirusCollision import VirusCollision

import pygame



class Game:

    def __init__(self):
        self.__game_over = False
        self.__screen = pygame.display.set_mode((1000, 700))
        self.__player = Player()
        self.__vaccines_background = VaccineBackground()
        self.__obstacles = Obstacles()
        self.__box = Box(900, 580)
        self.__boxes = Boxes()
        self.__virus  = Virus()
        #self.__obstacles = LShapedObstacle()
        self.__collision = ObstacleCollision()
        self.__virus_collision =VirusCollision()

        pygame.init()

    def play(self):
        while not self.__game_over:
            self.__vaccines_background.draw(self.__screen)
            self.__vaccines_background.move()

            self.__virus.draw(self.__screen)
            self.__virus.move()

            hit_top_box, hit_side_box = self.__collision.did_player_collid_with_obstacle(self.__player, self.__box)
            hit_virus = self.__virus_collision.did_virus_collide_with_player(self.__player, self.__virus)

            

            if not hit_side_box:
                self.__box.move()
                self.__boxes.move()
                #self.__obstacles.move()


            self.__player.change_axis_y(hit_top_box)


            
            self.__player.move(hit_top_box, hit_side_box)
            self.__player.draw(self.__screen)
            #self.__obstacles.draw(self.__screen)
            self.__box.draw(self.__screen)
            self.__boxes.draw(self.__screen)

            #self.__obstacles.draw(self.__screen)
            pygame.display.update()


if __name__ == "__main__":
    Game().play()
