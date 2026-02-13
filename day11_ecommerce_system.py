class Product:
    def __init__(self, product_name):
        self.product_name = product_name

class Electronics(Product):
    def show_electronics(self):
        print("Electronics Product:", self.product_name)

class Clothing(Product):
    def show_clothing(self):
        print("Clothing Product:", self.product_name)

class Mobile(Electronics):
    def show_mobile(self):
        print("Mobile Product:", self.product_name)


# Main Program
mobile = Mobile("iPhone")
mobile.show_mobile()
