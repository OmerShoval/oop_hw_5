from overrides.overrides import *
from models.car import *


class Bycycle(Car):

    def __init__(self, kind, size):
        super().__init__(kind)
        self.size = size

    @overrides
    def honk(self):
        super().honk()
        print("Wishh Wishh")

