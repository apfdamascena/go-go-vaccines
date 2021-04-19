import pygame
from Images import Images
from constants.PlayerConstants import PlayerConstants
from JumpAction import JumpAction

class Player:

    def __init__(self):
        self.__images = Images()
        self.__jump_action = JumpAction()

        
    def draw(self, window, axis_x, axis_y):
        window.blit(self.__images.main_character, (axis_x, axis_y, 100, 100))
        pygame.display.update()

    def move(self, axis_x, axis_y):

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    axis_x += PlayerConstants.VELOCITY

                if event.key == pygame.K_LEFT:
                    axis_x -= PlayerConstants.VELOCITY

                if not self.__jump_action.isJumping:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        self.__jump_action.i_am_jumping()

        axis_y = self.__jump_action.jumping(axis_y)

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            axis_x += PlayerConstants.VELOCITY

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            axis_x -= PlayerConstants.VELOCITY

        return axis_x, axis_y






