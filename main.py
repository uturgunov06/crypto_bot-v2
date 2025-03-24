import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(lambda message: message.text == "/start")
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="\ud83d\udcc8 График"), KeyboardButton(text="\ud83d\udcca Анализ")],
        [KeyboardButton(text="\ud83e\udde0 Совет"), KeyboardButton(text="\u2139\ufe0f Помощь")]
    ], resize_keyboard=True)

    await message.answer("\ud83d\udc4b Привет! Я бот по крипте. Что тебя интересует?", reply_markup=keyboard)

@dp.message()
async def echo(message: types.Message):
    await message.answer("Ты нажал: " + message.text)

async def main():
    print("\u2705 Бот запущен в режиме polling")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
