import logging
import random
import time

from bot_telegram import dp
from aiogram import types
import text
import game
from keyboard import kb, kb_start


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    logging.info(f'{time.asctime()} - {message.from_user.full_name} - {message.get_command()} ')
    await message.answer(f"{message.from_user.first_name}{text.greeting}")


@dp.message_handler(commands=['new_game'])
async def process_new_game(message: types.Message):
    logging.info(f'{time.asctime()} - {message.from_user.full_name} - {message.get_command()} ')
    game.restart()
    if game.game():
        draw = random.randint(0, 1)
        if draw:
            await player_turn(message)
        else:
            await enemy_turn(message)


@dp.message_handler(commands=['stop_game'])
async def process_stop_game(message: types.Message):
    logging.info(f'{time.asctime()} - {message.from_user.full_name} - {message.get_command()} ')
    game.restart()
    await message.reply('ИГРА ОКОНЧЕНА!', reply_markup=kb_start)


async def player_turn(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, твой ход! Сколько возьмешь конфет?', reply_markup=kb)


@dp.message_handler()
async def take(message: types.Message):
    name = message.from_user.first_name
    if game.game():
        if message.text.isdigit():
            take = int(message.text)
            if 0 < take < 29 and take <= game.get_total():
                game.take_candies(take)
                if await winner(message, 'player'):
                    return
                await message.answer(f'{name}, ты взял {take} конфет. На столе осталось {game.get_total()}. '
                                     f'Теперь я...')
                await enemy_turn(message)
            else:
                await message.answer('Можешь взять только от 1 до 28 конфет!')
        else:
            await message.answer('Введи целое число!')


async def enemy_turn(message: types.Message):
    total = game.get_total()
    if total <= 28:
        take = total
    else:
        take = total % 29
        if take == 0:
            take = random.randint(1, 28)
    game.take_candies(take)
    await message.answer(f'Я взял {take} конфет. На столе осталось {game.get_total()}.')
    if await winner(message, 'Бот'):
        return
    await player_turn(message)


async def winner(message: types.Message, player: str):
    if game.get_total() == 0:
        await message.answer(f'{message.from_user.first_name}' + text.win_player
                             if player == "player" else text.win_bot)
        game.restart()
        return True
    else:
        return False

