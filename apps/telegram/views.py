from django.shortcuts import render
from aiogram import Bot, Dispatcher, types, executor
from django.conf import settings
from logging import basicConfig, INFO

from apps.telegram.models import TelegramUser

# Create your views here.
bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
basicConfig(level=INFO)

@dp.message_handler(commands='start')
async def start_bot(message:types.Message):
    await message.answer("Привет!")
    