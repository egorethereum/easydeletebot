import telebot
import configs
import time
import random
from words import *
import traceback

bot = telebot.TeleBot(configs.Token)

print(bot.get_me())

@bot.message_handler(commands=['delete_all'])
def handle_text(message):
    for m in range(message.message_id, message.message_id == 0, -1):
        if message.message_id == 0:
            break
        else:
            try:
                bot.delete_message(message.chat.id, m)
            except:
                print("fail", traceback.format_exc())
                if message.message_id == 0:
                    break

@bot.message_handler(func=lambda msg: True, content_types=["text", "sticker", "photo", "audio", "video", "contact"])
def ban_user(message):
    try:
        ban_time = random.randint(120, 600)
        bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time.time() + ban_time)
        bot.reply_to(message,
                     bad_response[random.randint(0, len(bad_response))] + ', лови бан на ' + str(ban_time) + 'секунд')

    except Exception:
        print('Error in bad messages:\n', traceback.format_exc())


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        time.sleep(15)