from enum import Enum

class UserRole(Enum, str):
    USER = "user"
    BOT = "bot"
    ADMIN = "admin"