
import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(lambda message: message.text == "/start")
async def start(message: types.Message):
    await message.answer("👋 Привет! Я работаю через Webhook на Render!")

async def handle(request):
    data = await request.json()
    update = types.Update(**data)
    await dp.feed_update(bot, update)
    return web.Response()

async def main():
    webhook_path = f"/{BOT_TOKEN}"
    await bot.set_webhook(WEBHOOK_URL + BOT_TOKEN)

    app = web.Application()
    app.router.add_post(webhook_path, handle)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    await site.start()
    print("🌐 Webhook сервер запущен!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
