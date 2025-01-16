from inventory.user import User, UserRole

class UserManager:
    def __init__(self):
        """Inițializează managerul de utilizatori cu un utilizator admin implicit."""
        self.users = {
            "admin": User("admin", "admin123", UserRole.ADMIN)
        }

    def register_user(self, username: str, password: str, role: UserRole):
        """Înregistrează un nou utilizator dacă numele nu este deja folosit."""
        if username in self.users:
            raise ValueError("Acest nume de utilizator este deja folosit.")
        self.users[username] = User(username, password, role)

    def authenticate_user(self, username: str, password: str):
        """Autentifică utilizatorul și returnează obiectul User dacă este valid."""
        user = self.users.get(username)
        if user and user.check_password(password):
            return user
        return None

    def get_all_users(self):
        """Returnează lista utilizatorilor existenți."""
        return list(self.users.values())
