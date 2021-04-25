from virus.Virus import Virus
from constants.VirusConstants import VirusConstants
from manager.Manager import Manager
import random 

class VirusManager(Manager):

    def __init__(self):
        random_choice_virus_one = random.randint(0,3)
        random_choice_virus_two = random.randint(0,3)
        random_choice_virus_three = random.randint(0,3)
        self.__virus = [
            Virus(VirusConstants.VIRUS_ONE, random_choice_virus_one),
            Virus(VirusConstants.VIRUS_TWO, random_choice_virus_two),
            Virus(VirusConstants.VIRUS_THREE, random_choice_virus_three)
        ]

        super().__init__(self.__virus)

    @property
    def virus(self):
        return self.__virus