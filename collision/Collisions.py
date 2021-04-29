from collision.VirusCollision import VirusCollision
from collision.HeartCollision import HeartCollision
from collision.VaccineCollision import VaccineCollision
from collision.CrocodileCollision import CrocodileCollision

class Collisions:

    def __init__(self):
        self.__crocodile_collision = CrocodileCollision()
        self.__vaccine_collision = VaccineCollision()
        self.__virus_collision = VirusCollision()
        self.__heart_collision = HeartCollision()

    @property
    def with_crocodile(self):
        return self.__crocodile_collision
    
    @property
    def with_vaccine(self):
        return self.__vaccine_collision

    @property
    def with_virus(self):
        return self.__virus_collision
    
    @property
    def with_heart(self):
        return self.__heart_collision
