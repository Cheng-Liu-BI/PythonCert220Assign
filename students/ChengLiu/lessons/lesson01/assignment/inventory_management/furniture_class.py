#!/usr/bin/env python3
"""
Furniture class
"""

from inventory_class import Inventory


class Furniture(Inventory):
    """
    furniture class
    """

    def __init__(self, product_code, description, market_price,
                 rental_price, material, size):
        """
        init
        """
        Inventory.__init__(self, product_code, description, market_price, rental_price)  # Creates common instance variables from the parent class

        self.material = material
        self.size = size

    def return_as_dictionary(self):
        """
        return
        """
        output_dict = {}
        output_dict['productCode'] = self.product_code
        output_dict['description'] = self.description
        output_dict['marketPrice'] = self.market_price
        output_dict['rentalPrice'] = self.rental_price
        output_dict['material'] = self.material
        output_dict['size'] = self.size

        return output_dict
