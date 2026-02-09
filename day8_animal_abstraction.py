from abc import ABC, abstractmethod

class Animal(ABC):

    def sleep(self):
        print("This animal is sleeping")

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Dog says: Bark")


class Cat(Animal):
    def make_sound(self):
        print("Cat says: Meow")


class Cow(Animal):
    def make_sound(self):
        print("Cow says: Moo")


# Object creation
dog = Dog()
dog.make_sound()
dog.sleep()

cat = Cat()
cat.make_sound()
cat.sleep()

cow = Cow()
cow.make_sound()
cow.sleep()
