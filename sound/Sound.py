from pygame import mixer
import os


class Sound:

    def __init__(self):
        self.__catch_vaccine_heart = mixer.Sound(
            os.path.join('sound', 'sounds', 'vaccine_heart.ogg')
        )
        self.__jump = mixer.Sound(
            os.path.join('sound', 'sounds', 'jump.ogg')
        )
        self.__lost_life = mixer.Sound(
            os.path.join('sound', 'sounds', 'lost_life.ogg')
        )
        self.__stomp = mixer.Sound(
            os.path.join('sound', 'sounds', 'stomp.ogg')
        )
        self.__select = mixer.Sound(
            os.path.join('sound', 'sounds', 'select.ogg')
        )

    def vaccine_heart_play(self):
        self.__catch_vaccine_heart.play()

    def jump_play(self):
        self.__jump.play()

    def lost_life_play(self):
        self.__lost_life.play()

    def stomp_opponent_play(self):
        self.__stomp.play()

    def select_option_play(self):
        self.__select.play()
