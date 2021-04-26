from images.PlayerAssets import PlayerAssets
from images.CollectablesAssets import CollectablesAssets

class VaccineCollision:

    def __init__(self):
        self.__player_image = PlayerAssets()
        self.__collectables = CollectablesAssets()

    def did_vaccine_collide_with_player(self, player, vaccine):
        player_rectangle = self.__player_image.character_right_run.get_rect(x=player.axis_x, y=player.axis_y)
        vaccine_rectangle = self.__collectables.vaccine.get_rect(x=vaccine.axis_x, y=vaccine.axis_y)
        if player_rectangle.colliderect(vaccine_rectangle):
            return True       
        return False