# This code provides two linked functions for user registration and login.
# It takes input from the console for both registering and logging in users.

user_db = {}

def register_user():
    """
    Registers a new user by taking username and password from the console.
    If the username already exists, notifies the user.
    """
    username = input("Enter a username to register: ")
    if username in user_db:
        print("Username already exists. Please choose a different username.")
        return
    password = input("Enter a password: ")
    user_db[username] = password
    print("Registration successful!")

def login_user():
    """
    Logs in a user by taking username and password from the console.
    Checks credentials and notifies the user of success or failure.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user_db and user_db[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Example usage:
# The following loop allows the user to register or login.
while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Select an option: ")
    if choice == '1':
        register_user()
    elif choice == '2':
        login_user()
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid option. Please try again.")




