class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password   # private variable

    def check_password(self, password):
        if self.__password == password:
            return "Login successful"
        else:
            return "Wrong password"

    def change_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            return "Password updated successfully"
        else:
            return "Old password is incorrect"


# object creation
user1 = UserAccount("student01", "abc123")

# checking password
print(user1.check_password("abc123"))

# changing password
print(user1.change_password("abc123", "newpass456"))
