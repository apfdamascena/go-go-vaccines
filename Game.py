from background.MovingBackground import MovingBackground
from background.VaccineBackground import VaccineBackground
from player.Player import Player
from collision.ObstacleCollision import ObstacleCollision
from manager.VirusManager import VirusManager
from manager.ObstacleManager import ObstacleManager
from collision.VirusCollision import VirusCollision
from collision.HeartCollision import HeartCollision
from collectables.IndependentHeart import IndependentHeart
from collectables.Heart import Heart
from collectables.Vaccine import Vaccine
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
        self.__heart = Heart()
        self.__heart_collision = HeartCollision()
        self.__independent_heart = IndependentHeart()
        self.__vaccine = Vaccine()
        pygame.init()

    def play(self):
        while not self.__game_over:
            self.__vaccines_background.draw(self.__screen)
            self.__vaccines_background.move()

            self.__virus_manager.draw(self.__screen)
            self.__virus_manager.move()

            hit_top_box, hit_side_box = self.__collision.did_player_collid_with_obstacle(self.__player, self.__box_manager.boxes)
            hit_virus = self.__virus_collision.did_virus_collide_with_player(self.__player, self.__virus_manager.virus)
            hit_heart = self.__heart_collision.did_heart_collide_with_player(self.__player, self.__independent_heart)

            if not hit_side_box:
                self.__box_manager.move()
            self.__box_manager.draw(self.__screen)

            self.__player.change_axis_y(hit_top_box)
            self.__player.move(hit_top_box, hit_side_box)
            self.__player.draw(self.__screen)
            self.__heart.draw(self.__screen)
            self.__independent_heart.draw(self.__screen)
            if hit_heart:
                self.__independent_heart.colided()
                self.__heart.win_life()
            
            self.__vaccine.draw(self.__screen)
            pygame.display.update()


if __name__ == "__main__":
    Game().play()
