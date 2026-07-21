from aiogram import Router
from aiogram.types import Message

from texts import WELCOME_TEXT
from keyboards.menu import welcome_keyboard

router = Router()


@router.business_message()
async def business_message_handler(message: Message):

    await message.bot.send_message(
        chat_id=message.chat.id,
        business_connection_id=message.business_connection_id,
        text=WELCOME_TEXT,
        reply_markup=welcome_keyboard
    )