from abc import ABC
from typing import Any

from aiogram import Router
from aiogram.types import Message
from aiogram.handlers import BaseHandler

router = Router()

@router.message()
class MyHandler(BaseHandler[Message]):
    async def handle(self) -> Any:
         await self.event.answer("Hello!")