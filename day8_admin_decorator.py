def admin_only(func):
    def wrapper(user_role):
        if user_role == "admin":
            func(user_role)
        else:
            print("Access Denied: Admin only")
    return wrapper


@admin_only
def dashboard(user_role):
    print("Welcome to Admin Dashboard")


# Function calls
dashboard("admin")
dashboard("user")
