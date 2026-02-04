# Task 2
# This program demonstrates multilevel inheritance
# Product is the parent class
# Brand is the child class
# Item is the derived class

class Product:
    def product_type(self):
        print("This is a product")

class Brand(Product):
    def brand_name(self):
        print("Brand Name: ABC Electronics")

class Item(Brand):
    def item_details(self):
        print("Item Name: Smartphone")
        print("Price: Rs. 25,000")

# Object creation
item = Item()

# Accessing methods
item.product_type()
item.brand_name()
item.item_details()
