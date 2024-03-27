class Chair:
    def __init__(self, model, number_of_legs, price):
        self._model = model
        self._number_of_legs = number_of_legs
        self.price = price

    # getter and setters

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def number_of_legs(self):
        return self._number_of_legs

    @number_of_legs.setter
    def number_of_legs(self, number_of_legs):
        if isinstance(number_of_legs, int) and number_of_legs > 0:
            self.number_of_legs = number_of_legs
        else:
            raise ValueError("Number of legs must be a positive integer")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._price = price

    # methods
    def print_attributes(self):
        print(self.model)
        print(self.price)
        print(self.number_of_legs)

    def calculate_price(self, number_of_chairs):
        price_to_pay = int(self.price * number_of_chairs)
        print(f"you need to pay {price_to_pay}")

