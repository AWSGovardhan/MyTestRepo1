class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserManager, cls).__new__(cls)
            cls._instance.users = {}
        return cls._instance

    def add_user(self, user):
        if user.username not in self.users:
            self.users[user.username] = user
            print(f"User {user.username} added.")
        else:
            print(f"User {user.username} already exists.")

    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        else:
            print(f"User {username} not found.")
            return None

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
            print(f"User {username} removed.")
        else:
            print(f"User {username} not found.")

def main():
    user_manager = UserManager()

    user1 = User("john_doe", "john@example.com")
    user2 = User("alice_smith", "alice@example.com")

    user_manager.add_user(user1)
    user_manager.add_user(user2)

    user_manager.get_user("john_doe")
    user_manager.get_user("jane_doe")

    user_manager.remove_user("alice_smith")
    user_manager.remove_user("jane_doe")

if __name__ == "__main__":
    main()
