import telebot.types
from models import User


class AuthorizationService:

    def get_user(self, message: telebot.types.Message) -> User:
        return User(message.chat.id)

