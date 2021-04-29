from background.MovingBackground import MovingBackground
from background.VaccineBackground import VaccineBackground
from player.Player import Player
from manager.VirusManager import VirusManager
from collectables.IndependentHeart import IndependentHeart
from collectables.IndependentVaccine import IndependentVaccine
from collectables.Heart import Heart
from collectables.Vaccine import Vaccine
from humans.HandleCrocodileToHuman import HandleCrocodileToHuman
from collision.Collisions import Collisions
from sound.Sound import Sound
import pygame



class GamePlay:

    def __init__(self):
        self.__screen = pygame.display.set_mode((1000, 700))
        self.__vaccines_background = VaccineBackground()
        self.__player = Player()
        self.__heart = Heart()
        self.__vaccine = Vaccine()
        self.__independent_heart = IndependentHeart()
        self.__independent_vaccine = IndependentVaccine()
        self.__handle_crocodile_human = HandleCrocodileToHuman()
        self.__virus_manager = VirusManager()
        self.__collision = Collisions()
        self.__sound = Sound()

    def playing(self, start):
        while start:
            self.__draw_background()

            hit_virus = self.__collision.with_virus.did_virus_collide_with_player(
                self.__player, self.__virus_manager.virus)
            hit_crocodile = self.__collision.with_crocodile.did_player_collide_with_crocodile(
                self.__player, self.__handle_crocodile_human.crocodile)

            player_is_invencible = self.__player.invencible
            self.__action_after_hit_crocodile(hit_crocodile, player_is_invencible)
            self.__action_after_hit_virus_and_player_not_invencible(hit_virus, player_is_invencible)

            self.__draw_managers()
            self.__draw_and_move_player()
            self.__draw_collectables()

            hit_heart = self.__collision.with_heart.did_heart_collide_with_player(
                self.__player, self.__independent_heart)
            self.__action_after_hit_heart(hit_heart)

            hit_vaccine = self.__collision.with_vaccine.did_vaccine_collide_with_player(
                self.__player, self.__independent_vaccine)
            self.__action_after_hit_vacine(hit_vaccine)

            self.__handle_crocodile_human.draw(self.__screen)
            pygame.display.update()

    def __action_after_hit_crocodile(self, hit_crocodile, player_is_invencible):
        if not self.__handle_crocodile_human.is_human:
            if hit_crocodile and self.__heart.zero_lives_left():
                pygame.quit()
            elif hit_crocodile and self.__vaccine.zero_vaccine_left():
                if not player_is_invencible:
                    self.__heart.lost_life()
                    self.__player.is_invencible()
                    self.__sound.lost_life_play()
            elif hit_crocodile:
                self.__handle_crocodile_human.hit_crocodile_with_vaccine()
                self.__vaccine.spend_vaccine()

    def __action_after_hit_virus_and_player_not_invencible(self, hit_virus, player_is_invencible):
        if hit_virus and not player_is_invencible:
            if self.__heart.zero_lives_left():
                pygame.quit()
            self.__heart.lost_life()
            self.__sound.lost_life_play()
            self.__player.is_invencible()

    def __action_after_hit_vacine(self, hit_vaccine):
        if hit_vaccine:
            self.__independent_vaccine.colided()
            self.__vaccine.got_vaccine()
            self.__sound.vaccine_heart_play()

    def __action_after_hit_heart(self, hit_heart):
        if hit_heart:
            self.__independent_heart.colided()
            self.__heart.win_life()
            self.__sound.vaccine_heart_play()

    def __draw_collectables(self):
        self.__heart.draw(self.__screen)
        self.__vaccine.draw(self.__screen)
        self.__independent_heart.draw(self.__screen)
        self.__independent_vaccine.draw(self.__screen)

    def __draw_managers(self):
        self.__virus_manager.draw(self.__screen)

    def __draw_and_move_player(self):
        self.__player.move()
        self.__player.draw(self.__screen)

    def __draw_background(self):
        self.__vaccines_background.draw(self.__screen)
