import logging
from config import BOT_TOKEN
from services import AuthorizationService
from markups import main_markup

import telebot

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html")
telebot.logger.setLevel(logging.INFO)

auth_service = AuthorizationService()


@bot.message_handler(commands=['start'])
def start(message):
    if auth_service.get_user(message) is None:
        bot.send_message(
            message.chat.id,
            "Добрый день, путник.\nЯ очень рад видеть тебя на пути освобождения",
            reply_markup=main_markup
        )
    else:
        bot.send_message(
            message.chat.id,
            "Бот иногда творит что-то неясное, все нормально.",
            reply_markup=main_markup
        )


if __name__ == '__main__':
    bot.remove_webhook()
    bot.infinity_polling()
