
from images.PlayerAssets import PlayerAssets
from images.VirusAssets import VirusAssets
import pygame



class VirusCollision:

    def __init__(self):
        self.__player_image = PlayerAssets()
        self.__virus_image = VirusAssets()

    def did_virus_collide_with_player(self, player, amount_of_virus):
        player_rectangle = self.__player_image.character_right_run.get_rect(x=player.axis_x, y=player.axis_y)

        for virus in amount_of_virus:
            virus_rectangle = self.__virus_image.virus_blue.get_rect(x=virus.axis_x, y=virus.axis_y)

            if player_rectangle.colliderect(virus_rectangle):
                return True
                
        return False

