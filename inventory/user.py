import json


class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username in self.users:
            print("Username already taken.")
        else:
            self.users[username] = password
            self.save_users_to_json()

    def login_user(self, username, password):
        if self.users.get(username) == password:
            return True
        return False

    def save_users_to_json(self, file_path="inventory/users.json"):
        """Save user data to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump(self.users, f, indent=4)
        except Exception as e:
            print(f"Error saving users to JSON: {e}")
