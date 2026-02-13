class User:
    def login(self):
        print("User logged in")

class Rider(User):
    def book_ride(self):
        print("Ride booked successfully")

class Driver(User):
    def accept_ride(self):
        print("Driver accepted the ride")

class PremiumRider(Rider):
    def priority_booking(self):
        print("Priority ride booking enabled")


# Main Program
rider = PremiumRider()
rider.login()
rider.book_ride()
rider.priority_booking()
