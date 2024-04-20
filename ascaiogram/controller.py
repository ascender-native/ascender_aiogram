from aiogram import Bot, Dispatcher
from aiogram.types import Update
from asccore.main import app
from .handler.base import router
from pydantic import BaseModel


class WebhookController():
    async def bot(token: str, update: Update):
        dp = Dispatcher()
        bot: Bot = Bot(token)

        dp.include_router(router)

        await dp.feed_webhook_update(bot, update)

        return True