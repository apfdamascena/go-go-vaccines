from images.PlayerAssets import PlayerAssets
from images.CollectablesAssets import CollectablesAssets

class HeartCollision:

    def __init__(self):
        self.__player_image = PlayerAssets()
        self.__collectables = CollectablesAssets()

    def did_heart_collide_with_player(self, player, heart):
        player_rectangle = self.__player_image.character_right_run.get_rect(x=player.axis_x, y=player.axis_y)
        heart_rectangle = self.__collectables.heart.get_rect(x=heart.axis_x, y=heart.axis_y)
        if player_rectangle.colliderect(heart_rectangle):
            return True       
        return False