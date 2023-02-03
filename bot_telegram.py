from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
import logging

logging.basicConfig(level=logging.INFO, filename='bot.log')

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

logging.info('Start bot')
