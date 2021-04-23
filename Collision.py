from images.PlayerAssets import PlayerAssets
from images.ObstacleAssets import ObstacleAssets

class Collision:

    def __init__(self):
        self.__player_image = PlayerAssets()
        self.__obstacles_image = ObstacleAssets()
        self.__adjustment = 0


    def did_player_collid_with_obstacle(self, player, obstacle):
        player_rectangle = self.__player_image.character_right_run.get_rect(x= player.axis_x, y=player.axis_y)
        obstacle_rectangle = self.__obstacles_image.box_obstacle.get_rect(x=obstacle.axis_x, y=obstacle.axis_y)


        if player_rectangle.colliderect(obstacle_rectangle):
            if player_rectangle.bottom >= obstacle_rectangle.top and player_rectangle.bottom <= obstacle_rectangle.bottom:
                return True, False
            else:
                return False, True
            
        return False, False
        