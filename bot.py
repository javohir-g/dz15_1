import telebot
from buttons import start_buttons

# Укажите ваш API-ключ от BotFather
bot = telebot.TeleBot('7927478236:AAEaWaz1v2rNK9W5Oc2cZ7PPRjDhaZZMUHk')

# Константа для курса обмена
USD_TO_UZS_RATE = 12000

# Словарь для временного хранения данных пользователя
user_data = {}

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_conversion(message):
    user_id = message.from_user.id
    user_data[user_id] = {}  # Инициализируем временные данные пользователя
    bot.send_message(message.chat.id, "Введите сумму для конвертации:")
    bot.register_next_step_handler(message, get_amount)

# Получение суммы от пользователя
def get_amount(message):
    user_id = message.from_user.id
    try:
        amount = float(message.text)
        user_data[user_id]['amount'] = amount  # Сохраняем сумму
        bot.send_message(message.chat.id, "Выберите направление конверсии:", reply_markup=start_buttons())
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректную сумму.")
        bot.register_next_step_handler(message, get_amount)

# Обработчик для выбора направления конверсии
@bot.message_handler(func=lambda message: message.text in ["USD to UZS", "UZS to USD"])
def convert_currency(message):
    user_id = message.from_user.id
    amount = user_data[user_id].get('amount')

    if not amount:
        bot.send_message(message.chat.id, "Ошибка: сначала введите сумму. Используйте команду /start для перезапуска.")
        return

    if message.text == "USD to UZS":
        result = amount * USD_TO_UZS_RATE
        bot.send_message(message.chat.id, f"{amount} USD = {result} UZS")
    elif message.text == "UZS to USD":
        result = amount / USD_TO_UZS_RATE
        bot.send_message(message.chat.id, f"{amount} UZS = {result} USD")

# Запуск бота
bot.polling()
