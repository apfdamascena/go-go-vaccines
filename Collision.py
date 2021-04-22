from images.PlayerAssets import PlayerAssets
from images.ObstacleAssets import ObstacleAssets

class Collision:

    def __init__(self):
        self.__player_image = PlayerAssets()
        self.__obstacles_image = ObstacleAssets()
        self.__adjustment = 0


    def did_player_collid_with_obstacle(self, player, obstacle):
        player_rectangle = self.__player_image.character_right_run.get_rect(x= player.axis_x, y=player.axis_y)

        if player_rectangle.collidepoint(obstacle.axis_x, obstacle.axis_y):
            return False, True

        if player_rectangle.collidepoint(obstacle.axis_x, obstacle.axis_y-100):
            return True, False

        if player_rectangle.collidepoint(obstacle.axis_x+25, obstacle.axis_y-100):
            return True, False

        if player_rectangle.collidepoint(obstacle.axis_x+50, obstacle.axis_y-100):
            return True, False

        return False, False
        