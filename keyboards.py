from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


def size_keyboard():
    btn1 = KeyboardButton('Большую')
    btn2 = KeyboardButton('Маленькую')
    markup_size = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1).add(btn2)
    return markup_size


def payment_keyboard():
    btn1 = KeyboardButton('Наличкой')
    btn2 = KeyboardButton('Картой')
    markup_payment = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1).add(btn2)
    return markup_payment


def confirm_an_order():
    btn1 = KeyboardButton('Да')
    btn2 = KeyboardButton('Нет')
    markup_confirmation = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1).add(btn2)
    return markup_confirmation
