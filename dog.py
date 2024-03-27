from models.animal import Animal


class Dog(Animal):
    def __init__(self, name, age, gender, weight, breed, tail_length, bark_volume):
        super().__init__(name, age, gender, weight)
        self.breed = breed
        self.tail_length = tail_length
        self.bark_volume = bark_volume

    def make_sound(self):
        print(f"Woof! My bark volume is {self.bark_volume}.")

    def move(self):
        print("I'm running")
