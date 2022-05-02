import pytest


class Product:
    def __init__(self, name, description, reference_code):
        self.name = name
        self.description = description
        self.reference_code = reference_code

    def test_product(self):
        output = "The product's name is: " + self.name
        output += "The product " + self.description
        output += "The product's SKU is: " + self.reference_code


class Components:
    def __init__(self, name, description, irritating):
        self.name = name
        self.description = description
        self.irritating = irritating

    def test_component(self):
        output = "The ingredient is: " + self.name
        output += "This ingredient " + self.description
        output += "This is an irritating ingredient: " + self.irritating
