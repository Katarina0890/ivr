import telebot
import random
import difflib
from difflib import SequenceMatcher
from constants import *
bot = telebot.TeleBot(token)
bot.remove_webhook()
@bot.message_handler(commands =['start'])
def handle_start(message):
  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
  user_markup.row('/start', 'Хочу сайт', 'Команды', 'Правила', 'Усталь, пока')
  bot.send_message(message.from_user.id, "Привет, мой самый хороший друг! Я очечнь рад видеть тебя здесь! Если захочешь узнать - что я могу - нажми 'Команды'", reply_markup=user_markup)
@bot.message_handler(content_types =['text'])
def handle_text(message):
  if message.text == 'Да':
    bot.send_message(message.from_user.id, "Я рад) Выбирай команду")
  elif message.text == 'Нет':
    bot.send_message(message.from_user.id, "Я буду скучать по тебе(")  
  elif message.text == 'Хочу сайт':
    link = random.choice(RESPONSES_LINK)
    bot.send_message(message.from_user.id, link)
    link = random.choice(RESPONSES_LINK)
    bot.send_message(message.from_user.id, link)
    link = random.choice(RESPONSES_LINK)
    bot.send_message(message.from_user.id, link)
    bot.send_message(message.from_user.id, "Ты еще хочешь? работать со мной? Ответь, да или нет, позялуйста")
  elif message.text == 'Команды':
    bot.send_message(message.from_user.id, "О, я могу все, что пожелает мой повелитель) Главное - правильно попросить! -1. Захотелось еще поздороваться, не хватает тепла - пиши '/start') 0. Я умею показывтаь тебе чертежи задач из базы данных фипи, для этого нужно ввести просто правильно условие задание. 1. Если нажать команду 'Правила' - бот обязательно тебе подскажет,  как правильно написать условие :) 2. Если тебе станет тяжело с математикой и геометрий в то числе, не проблема - всего одна команда 'Хочу сайт' и целый удобный сайт-помогатор в твоем распоряжении. (P.S. Все совершенно бесплатно P.P.S. Взывать к этой команде можно не раз, помни это) 3. Захочешь уйти - не забудь попрощаться). УДАЧИ")  
    bot.send_message(message.from_user.id, "Ты еще хочешь? работать со мной? Ответь, да или нет, позялуйста")
  elif message.text == 'Правила':
    bot.send_message(message.from_user.id, rules) 
    bot.send_message(message.from_user.id, "Ты еще хочешь? работать со мной? Ответь, да или нет, позялуйста") 
  elif message.text == 'Усталь, пока':
    bot.send_message(message.from_user.id, "Я буду ждать тебя, мой самый дорогой человек) Пиши мне когда захочешь")    
  else:
    a = 0
    for i in phipi:
      if message.text==i[0]:
        a+=1
        img = open(i[1], 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
        break
    if a == 0:
      bot.send_message(message.from_user.id, "Мы не обнаружили точного совпадения в наших условиях. Давайте мы поищем еще чуть-чуть, хорошо? Не бойся, если вариантов будет слишком много:)")
      for i in phipi:
        s = SequenceMatcher(None, message.text, i[0]).ratio()
        if s >= 0.9:
          bot.send_message(message.from_user.id, "Мы нашли кое-что похожее, а вот и его условия :)")
          bot.send_message(message.from_user.id, i[0])
          bot.send_message(message.from_user.id, "А вот и чертеж к нему")
          img = open(i[1], 'rb')
          bot.send_chat_action(message.from_user.id, 'upload_photo')
          bot.send_photo(message.from_user.id, img)
          img.close()
          a+=1
          break
    if a == 0:
      bot.send_message(message.from_user.id, "Ну что за невезуха(( Чертеж так и не найден( Простите, я так не играю(")
    bot.send_message(message.from_user.id, "Ты еще хочешь работать со мной? Ответь, да или нет, позялуйста")
bot.polling(none_stop=True)