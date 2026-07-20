from aiogram import Router
from aiogram.types import Message
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from states import ApplicationState
from config import ADMIN_ID
from keyboards.menu import welcome_keyboard

router = Router()


@router.message(StateFilter(ApplicationState.waiting_application))
async def receive_application(message: Message, state: FSMContext):

    # Отправляем информацию о пользователе
    text = (
        "📩 Новая заявка\n\n"
        f"👤 Имя: {message.from_user.full_name}\n"
        f"📎 Username: @{message.from_user.username if message.from_user.username else 'нет'}\n"
        f"🆔 ID: {message.from_user.id}"
    )

    await message.bot.send_message(
        ADMIN_ID,
        text
    )

    # Копируем сообщение пользователя тебе
    await message.copy_to(ADMIN_ID)

    # Благодарим пользователя
    await message.answer(
        "🤍 Спасибо! Ваша заявка успешно получена.\n\n"
        "Я лично рассмотрю её и свяжусь с вами после проверки."
    ,  reply_markup=welcome_keyboard)
    # Выходим из режима ожидания заявки
    await state.clear()