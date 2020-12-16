#! /usr/bin/env python
# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot("1485531627:AAEcbWCfQpmUhRyNiImffwKGCHg7xPG48B8")

from telebot import types

first_recipe = ["Гречка с курицей и морковью. Куриное филе нарежьте небольшими кусочками. Лук измельчите, морковь натрите на мелкой терке. В кастрюлю с толстым дном добавьте растительное масло. Филе, лук и морковь. Перемешайте, посолите (0,5 ч.л. соли), поперчите по вкусу и поджарьте до готовности овощей. Помойте гречневую крупу. Добавьте в кастрюлю к курице и овощам."]

second_recipe = ["Гречка с курицей в духовке. Промыть гречку и высыпать в отдельную миску. Вскипятить воду и залить гречку минут на 10 примерно. Туда же добавить соли и приправы. Далее нужно промыть под проточной водой куриное филе, обсушить и на эти 10 минут замариновать в соли, перце и любой любимой приправе. Духовку ставим на 180 градусов и ждем, пока разогреется. Половинку луковицы режем тонкими полукольцами, а чеснок - мелкими кубиками. Берем форму, в нее заливаем растительное масло. Если масло сливочное, то его в последний момент кладем маленькими кусочками сверху всего блюда. Высыпаем в форму лук и чеснок, гречку вместе с водой и перемешиваем, распределяя равномерно ингредиенты. Выкладываем курицу последним слоем. В разогретую духовку ставим нашу форму по центру на 1 час. Минут за 20 до финиша нужно убрать фольгу, чтобы появился вкусный золотистый оттенок."]

third_recipe = ["Гречка с курицей в горшочке. Грудку освобождаем от участков жира, кожи и костей, нарезаем не очень крупно. Лук нарезаем максимально мелко, морковку нарезаем покрупнее. В сковороде на огне выше среднего разогреваем растительное масло. Кладем в сковороду кусочки курицы и обжариваем их со всех сторон. Следом отправляем к мясу лук, морковку и чеснок. Обжариваем, помешивая, в течение 7-8 минут. Гречу перебираем, промываем под холодной водой и добавляем в сковороду. Перемешиваем и снимаем посуду с огня. Раскладываем гречу с курицей и овощами по горшочкам. Заливаем в каждый горячую воду так, чтобы она полностью покрывала содержимое. Отправляем горшочки в предварительно разогретую духовку на 40 минут. За 10 минут до конца приготовления кладем в каждый горшочек по чайной ложке сливочного масла."]

recipies = [first_recipe, second_recipe, third_recipe]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "Привет":

        bot.send_message(message.from_user.id, "Привет! Сейчас мы вместе с тобой приготовим вкусную и полезную еду из продуктов в твоём холодильнике.")

        keyboard = types.InlineKeyboardMarkup()

        key_chicken = types.InlineKeyboardButton(text='Курица', callback_data='chicken')

        keyboard.add(key_chicken)

        key_buckwheat = types.InlineKeyboardButton(text='Гречка', callback_data='buckwheat')

        keyboard.add(key_buckwheat)

        key_carrot = types.InlineKeyboardButton(text='Морковь', callback_data='carrot')

        keyboard.add(key_carrot)

        bot.send_message(message.from_user.id, text='Выбери продукты, которые у тебя есть в холодильнике', reply_markup=keyboard)

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши Привет")

    else:

        bot.send_message(message.from_user.id, "Давай готовить вместе. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == 'chicken':

        bot.send_message(call.message.chat.id, first_recipe)

    if call.data == 'buckwheat':

        bot.send_message(call.message.chat.id, second_recipe)

    if call.data == 'carrot':

        bot.send_message(call.message.chat.id, third_recipe)

bot.polling(none_stop=True, interval=0)
