from telebot import types

main_markup = types.ReplyKeyboardMarkup()
time_button = types.KeyboardButton('Сколько я уже свободен?')
money_button = types.KeyboardButton('Сколько денег я могу отложить в фонд свободы?')
reasons_button = types.KeyboardButton('И все же почему я освободился от рабства?')

main_markup.row(time_button)
main_markup.row(money_button)
main_markup.row(reasons_button)
