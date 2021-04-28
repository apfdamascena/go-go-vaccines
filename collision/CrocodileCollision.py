
from images.PlayerAssets import PlayerAssets

class CrocodileCollision:

    def __init__(self):
        self.__player_image = PlayerAssets()
        



    def did_player_collide_with_crocodile(self, player, crocodile_abstraction):
        player_rectangle = self.__player_image.character_right_run.get_rect(x= player.axis_x, y=player.axis_y)
        crocodile_rectangle = crocodile_abstraction.crocodile.get_rect(x=crocodile_abstraction.axis_x, y=crocodile_abstraction.axis_y)
        
        if player_rectangle.colliderect(crocodile_rectangle):
            return True
        return False
