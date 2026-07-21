from aiogram import Router
from aiogram.types import Message

from texts import WELCOME_TEXT
from keyboards.menu import welcome_keyboard
from database import is_known_chat, add_chat

router = Router()


@router.business_message()
async def business_message_handler(message: Message):

    # Если этот чат уже видел приветствие — ничего не делаем
    if is_known_chat(message.chat.id):
        return

    # Запоминаем чат
    add_chat(message.chat.id)

    # Отправляем приветствие
    await message.bot.send_message(
        chat_id=message.chat.id,
        business_connection_id=message.business_connection_id,
        text=WELCOME_TEXT,
        reply_markup=welcome_keyboard
    )