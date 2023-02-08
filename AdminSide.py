import telebot
from datetime import datetime

from database import Data
import buttons

bot = telebot.TeleBot('5738312122:AAExajjeym8nkTP-NbtfGjhjYPELGSMlzSg')


@bot.message_handler(commands=['start'])
def admin_message(message):
    admin_id = message.from_user.id
    text = 'Добро пожаловать на панель администратора'
    print(message.from_user.id)
    bot.send_message(admin_id, text, reply_markup=buttons.admin_menu())

    bot.register_next_step_handler(message, main_menu)


def main_menu(message):
    user_id = message.from_user.id
    if message.text == 'База':

        if True:
            baza = Data().show_all()
            full_message = ''
            for i in baza:
                full_message += f"id: {i[0]}\nКомплекс: {i[1]} \nКомнат: {i[2]}\nЭтаж: {i[3]}\nКвадратура:{i[4]}/кв/м\nЦена: {i[5]} /cум \n\n"

            bot.send_message(user_id, full_message, reply_markup=buttons.back())

            # bot.register_next_step_handler(message, get_back)
        else:
            bot.send_message(user_id, 'Ничего нeт', reply_markup=buttons.back())


    elif message.text == 'База клиентов':
        try:
            baza = Data().show_clients()
            full_message = ''
            for i in baza:
                full_message += f"id: {i[0]}\nИмя: {i[1]} \nНомер: {i[2]}\nАдрес: {i[3]} \nДата регистрации: {i[4]}  \n\n"

            bot.send_message(user_id, full_message, reply_markup=buttons.back())
            # bot.register_next_step_handler(message, get_back)
        except:
            bot.send_message(user_id, 'Ничего нет', reply_markup=buttons.back())
    elif message.text == 'Добавить комплекс':
        bot.send_message(message.from_user.id, 'Назовите комплекс', reply_markup=buttons.catalog())
        bot.register_next_step_handler(message, get_name)

    elif message.text == 'Удаление квартиры':
        bot.send_message(message.from_user.id, 'Kakuyu kvartiru hotite udalit?',reply_markup=buttons.catalog())
        bot.register_next_step_handler(message, get_delite)


def get_name(message):
    com_name = message.text
    bot.send_message(message.from_user.id, 'Скольки комнатная?', reply_markup=buttons.numb())
    bot.register_next_step_handler(message, get_room, com_name)


def get_room(message, com_name):
    room = message.text
    bot.send_message(message.from_user.id, 'На каком этаже?', reply_markup=buttons.numb())
    bot.register_next_step_handler(message, get_floor, com_name, room)


def get_floor(message, com_name, room):
    floor = message.text
    bot.send_message(message.from_user.id, 'Сколько квадратов?')
    bot.register_next_step_handler(message, get_sqm, com_name, room, floor)


def get_sqm(message, com_name, room, floor):
    sqm = message.text
    bot.send_message(message.from_user.id, 'Стоимость?')
    bot.register_next_step_handler(message, get_price, com_name, room, floor, sqm)

def get_price(message, com_name, room, floor,sqm):
    price = message.text
    bot.send_message(message.from_user.id, 'Отправте планировку?')
    bot.register_next_step_handler(message, get_plan, com_name, room, floor, sqm,price)

def get_plan(message, com_name, room, floor,sqm,price):
    plan = message.text
    db = Data()
    db.complex_add(com_name, room, floor, sqm,price,plan)
    bot.send_message(message.from_user.id, 'Объект успешно добавлен!',reply_markup=buttons.back())
    bot.register_next_step_handler(message,get_back)


def get_back(message):
    if message.text == 'Назад':
        bot.register_next_step_handler(message,main_menu)

def get_delite(message):
    name = message.text
    bot.send_message(message.from_user.id, 'Напиши id квартиры')
    bot.register_next_step_handler(message,get_id_delite,name)

def get_id_delite(message,name):
    id = message.text
    Data().delite_comlex(name,id)
    bot.send_message(message.from_user.id, 'Комплекс удалён',reply_markup=buttons.back())
bot.polling()
