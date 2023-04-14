from .models import Person
from django.shortcuts import render, redirect
import telebot
from django.conf import settings

general_keybord = telebot.types.InlineKeyboardMarkup()

task_keybord = telebot.types.InlineKeyboardButton('Мои задачи', callback_data='show_task')
archive_keybord = telebot.types.InlineKeyboardButton('Архив', callback_data='show_archive')

general_keybord.add(task_keybord, archive_keybord)

def bind_acc_with_telegram(request, tele_id):
    if request.user.is_authenticated:
        persons = Person.objects.filter(tele_id=tele_id)
        if len(persons):
            if persons[0].user == request.user:
                message = 'Ваш телеграм уже привязан к вашему аккаунту.'
            else:
                message = 'Вы пытаетесь привязать телеграм, который уже был привязан к другому аккаунту.'
        else:
            Person.objects.create(user=request.user, tele_id=tele_id)
            text = 'Ваш телеграм был только что привязан к основному аккаунту. Если это были не вы, вы можете отвязать телеграм в опциях данного бота.'
            send_message_by_telegram(text=text, tele_id=tele_id)
            send_general_message(tele_id)
            message = 'Ваш телеграм успешно привязан.'
    else:
        message = ''
    return render(request, 'registration/id.html', {'message': message, 'id': tele_id})


def send_message_by_telegram(text:str, tele_id:int, markup=None):
    bot = telebot.TeleBot(settings.BOT_TOKEN)
    bot.send_message(tele_id, text, parse_mode='HTML', reply_markup=markup)

def send_general_message(id: int):
    text = 'Чем могу помочь?'
    send_message_by_telegram(text, id, general_keybord)