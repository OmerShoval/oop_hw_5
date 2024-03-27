from models.chair import *
from overrides.overrides import *

class Bar_chair(Chair):

    def __init__(self, model, number_of_legs, price, is_allow_adjustments, is_spinning, discount_amount,
                 has_discount_amount):
        super().__init__(model, number_of_legs, price)
        self.is_allow_adjustments = is_allow_adjustments
        self.is_spinning = is_spinning
        self.discount_amount = discount_amount
        self.has_discount_amount = has_discount_amount

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

    @property
    def is_allow_adjustments(self):
        return self.is_allow_adjustments

    @is_allow_adjustments.setter
    def is_allow_adjustments(self, is_allow_adjustments):
        self._model = is_allow_adjustments

    @property
    def is_spinning(self):
        return self.is_spinning

    @is_spinning.setter
    def is_spinning(self, is_spinning):
        self._model = is_spinning

    @property
    def discount_amount(self):
        return self.discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        self._model = discount_amount

    @property
    def has_discount_amount(self):
        return self.has_discount_amount

    @has_discount_amount.setter
    def has_discount_amount(self, has_discount_amount):
        self._model = has_discount_amount

    @overrides
    def print_attributes(self):
        print(f"{self._price}, {self._model}, {self.is_spinning}, {self.model}"
              f"{self.is_allow_adjustments}, {self.has_discount_amount}, {self.has_discount_amount}")

    @overrides
    def calculate_price(self, number_of_chairs):
        if self.has_discount_amount:
            return super().calculate_price(number_of_chairs) - self.discount_amount
        else:
            super().calculate_price(number_of_chairs)


    