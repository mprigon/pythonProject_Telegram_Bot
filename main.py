# телеграм бот MyPersonPy_bot
# итоговое задание по модулю C5.6
# выполнил Пригон Максим FPW-82

import telebot
from config import keys, TOKEN
from utils import ConvertionException, CryptoConverter, APIServerException


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    # bot.send_message(message.chat.id, f'Добрый день, {message.chat.first_name} {message.chat.last_name}')
    text = f'Добрый день, {message.chat.first_name},\nя - бот, умею рассчитывать\n' \
           f'перевод денег из одной валюты в другую.\n' \
           f'Курс валюты в реальном времени запрашиваю на apilayer.com\n' \
           f'Чтобы начать работу, введите мне команду в следующем формате:\n' \
           '<имя валюты, цену которой хотите узнать> <имя валюты, в которой надо узнать цену первой валюты>' \
           '<количество первой валюты>\nНапример, <доллар рубль 2> означает цену 2 долларов в рублях\n' \
           'Увидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    # quote - хотим купить, base - чем оплачиваем, amount - количество
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertionException('Некорректное количество параметров, должно быть 3.')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except APIServerException as e:
        bot.reply_to(message, f'Ошибка сервера apilayer.com.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        # total_base достаточно 6 знаков после запятой, так как
        # apilayer.com в ключе rates ответа дает 6 знаков
        text = f'Цена {amount} {quote} в {base} - ' + '%.6f' % total_base
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
