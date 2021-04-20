import pygame
from background.Images import Images
from constants.PlayerConstants import PlayerConstants
from player.JumpAction import JumpAction
from player.SquatAction import SquatAction

class Player:

    def __init__(self):
        self.__images = Images()
        self.__jump_action = JumpAction()
        self.__squat_action = SquatAction()

        
    def draw(self, window, axis_x, axis_y):
        if self.__squat_action.is_squatting:
            self.__squat_action.squatting(window, axis_x, axis_y)
        else: 
            window.blit(self.__images.character_right_run, (axis_x, axis_y, 100, 100))
        pygame.display.update()

    def move(self, axis_x, axis_y):

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    axis_x += PlayerConstants.VELOCITY

                if event.key == pygame.K_LEFT:
                    axis_x -= PlayerConstants.VELOCITY
            
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    self.__jump_action.player_is_jumping()
                
                if event.key == pygame.K_DOWN:
                    self.__squat_action.player_is_squatting()

        axis_y = self.__jump_action.jumping(axis_y)

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            axis_x += PlayerConstants.VELOCITY

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            axis_x -= PlayerConstants.VELOCITY

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.__squat_action.player_is_squatting()

        return axis_x, axis_y






