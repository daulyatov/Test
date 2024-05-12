import logging
import telebot
from telebot import types

from django.conf import settings
from telegrambot.models import TelegramUser, Stage, StageProgress
from telegrambot.keyboards import get_keyboard, get_stage_keyboard, get_stageprogress_keyboard

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


bot = telebot.TeleBot(settings.TOKENBOT, parse_mode="HTML")


@bot.message_handler(commands=["start"])
def start(message):
    user = message.from_user
    
    model_user, created = TelegramUser.objects.get_or_create(user_id=user.id)
    
    if created:
        model_user.user_id = user.id
        model_user.username = user.username
        model_user.first_name = user.first_name
        model_user.last_name = user.last_name

        model_user.save()
 
        logging.info(f'Был создан новый аккаунт {model_user.get_name()}')
    
    bot.send_message(message.chat.id, f"Привет, {model_user.get_name()}!", reply_markup=get_keyboard())


def RunBot():
    try:
        logger = logging.getLogger("RunBot")
        logger.info("Запуск бота!")
        bot.polling(none_stop=True, interval=0)
        
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}!")
        raise e
    
    except KeyboardInterrupt:
        logger.info("Бот остановлен принудительно!")
    
    finally:
        logger.info("Завершение работы бота!")