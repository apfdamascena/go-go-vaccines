from background.MovingBackground import MovingBackground
from background.VaccineBackground import VaccineBackground
from player.Player import Player
from collision.ObstacleCollision import ObstacleCollision
from manager.VirusManager import VirusManager
from manager.ObstacleManager import ObstacleManager
from collision.VirusCollision import VirusCollision
import pygame

class Game:

    def __init__(self):
        self.__game_over = False
        self.__screen = pygame.display.set_mode((1000, 700))
        self.__player = Player()
        self.__vaccines_background = VaccineBackground()
        self.__virus_manager  = VirusManager()
        self.__box_manager = ObstacleManager()
        self.__collision = ObstacleCollision()
        self.__virus_collision = VirusCollision()

        pygame.init()

    def play(self):
        while not self.__game_over:
            self.__vaccines_background.draw(self.__screen)
            self.__vaccines_background.move()

            self.__virus_manager.draw(self.__screen)
            self.__virus_manager.move()

            hit_top_box, hit_side_box = self.__collision.did_player_collid_with_obstacle(self.__player, self.__box_manager.boxes)
            hit_virus = self.__virus_collision.did_virus_collide_with_player(self.__player, self.__virus_manager.virus)

            if not hit_side_box:
                self.__box_manager.move()
            self.__box_manager.draw(self.__screen)

            self.__player.change_axis_y(hit_top_box)
            self.__player.move(hit_top_box, hit_side_box)
            self.__player.draw(self.__screen)
            pygame.display.update()


if __name__ == "__main__":
    Game().play()
