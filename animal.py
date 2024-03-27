class Animal:
    def __init__(self, name, age, gender, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def print_animal(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Weight: {self.weight}")

    def make_sound(self):
        print("weeeeee")

    def move(self):
        print("I'm moving")
