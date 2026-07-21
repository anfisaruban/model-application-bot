from aiogram import Router
from aiogram.types import Message

router = Router()


@router.business_message()
async def business_message_handler(message: Message):

    await message.bot.send_message(
        chat_id=message.chat.id,
        business_connection_id=message.business_connection_id,
        text="Тест: бот получил сообщение через Telegram Business ✅"
    )