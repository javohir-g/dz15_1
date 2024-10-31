from telebot import types

def start_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_usd_to_uzs = types.KeyboardButton("USD to UZS")
    button_uzs_to_usd = types.KeyboardButton("UZS to USD")
    markup.add(button_usd_to_uzs, button_uzs_to_usd)
    return markup
