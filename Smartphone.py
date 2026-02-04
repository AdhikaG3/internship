# Task 1
# This program demonstrates multiple inheritance
# Camera and MusicPlayer are parent classes
# SmartPhone is the derived class

class Camera:
    def take_photo(self):
        print("Photo captured using camera")

class MusicPlayer:
    def play_music(self):
        print("Music is playing")

class SmartPhone(Camera, MusicPlayer):
    def make_call(self):
        print("Calling from smartphone")

# Object creation
phone = SmartPhone()

# Accessing methods
phone.make_call()
phone.take_photo()
phone.play_music()
