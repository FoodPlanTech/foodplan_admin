import os

import logging
import datetime
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, update, KeyboardButton, ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from environs import Env

logging.basicConfig(filename='bt.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = '6579483149:AAEULVSNl8VM8JdfssXrEEgme52uAjJMwcQ'

FIRST, SECOND = range(2)
ONE, TWO, THREE, FOUR = range(4)


def start_command(update, context):
    user = update.message.from_user
    logger.info("Пользователь %s запустил бота", user.first_name)
    keyboard = [
        [
            InlineKeyboardButton("Оформить подписку", callback_data=str(ONE)),
            InlineKeyboardButton("Еще рецепт", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        text="Привественные слова от бота И описание принципа работы", reply_markup=reply_markup
    )
    return FIRST

def payment(update, _):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="подписались!все классно")
    return SECOND 


def two(update, _):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="рецепт с картинкой"
    )
    return FIRST

def main():
    updater = Updater(token=BOT_TOKEN)
    dispatcher = updater.dispatcher
    logic_conversation = ConversationHandler(
    entry_points=[CommandHandler('start', start_command)],
    states={
            FIRST: [MessageHandler(Filters.text & ~Filters.command, payment)],
    },
        fallbacks=[]
    )
    dispatcher.add_handler(logic_conversation)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()