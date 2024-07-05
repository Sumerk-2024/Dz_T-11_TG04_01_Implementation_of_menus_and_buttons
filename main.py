import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from keyboards import start_keyboard, link_keyboard, dynamic_keyboard, dynamic_options_keyboard

from dotenv import load_dotenv
import logging

# Загрузка переменных окружения из файла .env
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


# Обработчик команды /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=start_keyboard)


# Обработчик команды /help
@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды:\n/start\n/help\n/links\n/dynamic')


# Обработчик команды /links
@dp.message(Command('links'))
async def send_links(message: Message):
    await message.answer('Выберите ссылку:', reply_markup=link_keyboard)


# Обработчик команды /dynamic
@dp.message(Command('dynamic'))
async def send_dynamic(message: Message):
    await message.answer('Выберите опцию:', reply_markup=dynamic_keyboard)


# Обработчики нажатий на кнопки
@dp.callback_query(F.data == 'show_more')
async def show_more(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=dynamic_options_keyboard)


@dp.callback_query(F.data == 'option_1')
async def option_1(callback: CallbackQuery):
    await callback.message.answer('Вы выбрали Опцию 1')


@dp.callback_query(F.data == 'option_2')
async def option_2(callback: CallbackQuery):
    await callback.message.answer('Вы выбрали Опцию 2')


# Обработчики нажатий на кнопки "Привет" и "Пока"
@dp.message(F.text == "Привет")
async def greet_user(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')


@dp.message(F.text == "Пока")
async def farewell_user(message: Message):
    await message.answer(f'До свидания, {message.from_user.first_name}!')


# Обработчики нажатий на инлайн-кнопки с URL-ссылками
@dp.callback_query(F.data == 'news')
async def show_news(callback: CallbackQuery):
    await callback.answer("Новости подгружаются", show_alert=True)
    await callback.message.answer('Вот свежие новости!')


@dp.callback_query(F.data == 'music')
async def show_music(callback: CallbackQuery):
    await callback.answer("Музыка подгружается", show_alert=True)
    await callback.message.answer('Вот ваша музыка!')


@dp.callback_query(F.data == 'video')
async def show_video(callback: CallbackQuery):
    await callback.answer("Видео подгружается", show_alert=True)
    await callback.message.answer('Вот ваше видео!')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
