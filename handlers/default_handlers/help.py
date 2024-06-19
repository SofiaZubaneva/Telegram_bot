from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS
from loader import bot

@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    bot.reply_to(message, "Чем могу помочь?")