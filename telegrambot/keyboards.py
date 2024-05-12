from telebot import types


def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    btn1 = types.KeyboardButton("Добавить этап")
    btn2 = types.KeyboardButton("Ввести данные")
    # btn3 = types.KeyboardButton("Посмотреть отчет")
    
    keyboard.row(btn1)
    keyboard.row(btn2)
    # keyboard.row(btn3)
    
    return keyboard


def get_stage_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    btn1 = types.KeyboardButton("Добавить объем")
    btn2 = types.KeyboardButton("Назад")
    
    keyboard.row(btn1)
    keyboard.row(btn2)
    
    return keyboard

def get_stageprogress_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    btn1 = types.KeyboardButton("Выполненный объем")
    btn2 = types.KeyboardButton("Назад")
    
    keyboard.row(btn1)
    keyboard.row(btn2)
    
    return keyboard


