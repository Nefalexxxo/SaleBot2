import telebot.types
from telebot import types
from database import Data


# Number send
def num_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    number = types.KeyboardButton('Отправить номер')
    kb.add(number)
    return kb


# User side menu
def main_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    catalog = types.KeyboardButton('Каталог комлексов')

    call = types.KeyboardButton('Связаться с нами')

    kb.add(catalog, call)
    return kb


# Admin menu
def admin_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    base = types.KeyboardButton('База')
    add_com = types.KeyboardButton('Добавить комплекс')
    clients = types.KeyboardButton('База клиентов')
    del_com = types.KeyboardButton('Удаление квартиры')
    del_base = types.KeyboardButton('Очистка базы')
    kb.add(base, add_com, clients, del_com, del_base)
    return kb


# Catalog button
def catalog():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    infinity = types.KeyboardButton('Infinity')
    ozmahal = types.KeyboardButton('OzMahal')
    sohil = types.KeyboardButton('Sohil')
    ozmakon = types.KeyboardButton('OzMakon')
    green = types.KeyboardButton('Greenwich')
    havo = types.KeyboardButton('Havo')
    back = types.KeyboardButton('Назад')
    kb.add(infinity, ozmahal, sohil, ozmakon, green, havo, back)
    return kb


def numb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    num1 = types.KeyboardButton('1')
    num2 = types.KeyboardButton('2')
    num3 = types.KeyboardButton('3')
    num4 = types.KeyboardButton('4')
    num5 = types.KeyboardButton('5')
    num6 = types.KeyboardButton('6')
    num7 = types.KeyboardButton('7')
    num8 = types.KeyboardButton('8')
    num9 = types.KeyboardButton('9')
    kb.add(num1, num2, num3, num4, num5, num6, num7, num8, num9)
    return kb


def rooms():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    r1 = types.KeyboardButton('Однокомнатная')
    r2 = types.KeyboardButton('Двухкомнатная')
    r3 = types.KeyboardButton('Трехкомнатная')
    r4 = types.KeyboardButton('Четырехкомнатная')
    r5 = types.KeyboardButton('Пятикомнатная')
    r6 = types.KeyboardButton('Щестикомнатная')
    r7 = types.KeyboardButton('Семикомнатная')
    back = types.KeyboardButton('Назад')
    kb.add(r1, r2, r3, r4, r5, r6, r7, back)
    return kb


def back():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Назад')
    menu = types.KeyboardButton('Главное меню')
    call = types.KeyboardButton('Связаться с нами')
    kb.add(back, call, menu)
    return kb
a = telebot.types.ReplyKeyboardRemove