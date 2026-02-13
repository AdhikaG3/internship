class Device:
    def power_on(self):
        print("Device is powered ON")

class SmartFeatures(Device):
    def connect_wifi(self):
        print("Device connected to WiFi")

class EntertainmentFeatures(Device):
    def play_music(self):
        print("Playing music...")

class SmartTV(SmartFeatures, EntertainmentFeatures):
    def watch_tv(self):
        print("Watching Smart TV")


# Main Program
tv = SmartTV()
tv.power_on()
tv.connect_wifi()
tv.play_music()
tv.watch_tv()
