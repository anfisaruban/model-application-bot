from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    CallbackQuery,
    FSInputFile,
    InputMediaPhoto,
)

from texts import (
    WELCOME_TEXT,
    REQUIREMENTS_TEXT,
    APPLICATION_FORMAT_TEXT,
    SNAPS_TEXT,
    PORTRAITS_TEXT,
    VIDEO_TEXT,
    FAQ_TEXT,
    APPLICATION_TEXT,
)

from keyboards.menu import (
    welcome_keyboard,
    requirements_keyboard,
    snaps_keyboard,
    portraits_keyboard,
    video_keyboard,
    back_keyboard,
    back_to_snaps_keyboard,
    back_to_portraits_keyboard,
    back_to_video_keyboard,
    application_format_keyboard,
)
from states import ApplicationState

router = Router()


# =====================================================
# /start
# =====================================================

@router.message(CommandStart())
async def start(message: Message):

    await message.answer(
        WELCOME_TEXT,
        reply_markup=welcome_keyboard
    )


# =====================================================
# Главное меню
# =====================================================

@router.callback_query(F.data == "requirements")
async def requirements(callback: CallbackQuery):

    await callback.message.edit_text(
        REQUIREMENTS_TEXT,
        reply_markup=requirements_keyboard
    )

    await callback.answer()


# =====================================================
# Формат заявки
# =====================================================

@router.callback_query(F.data == "application_format")
async def application(callback: CallbackQuery, state: FSMContext):

    await callback.message.edit_text(
        APPLICATION_FORMAT_TEXT,
        reply_markup=application_format_keyboard
    )

    await callback.answer()

# =====================================================
# Отправить заявку
# =====================================================

@router.callback_query(F.data == "send_application")
async def send_application(callback: CallbackQuery, state: FSMContext):

    await state.set_state(ApplicationState.waiting_application)

    await callback.message.edit_text(
        APPLICATION_FORMAT_TEXT,
        reply_markup=back_keyboard
    )

    await callback.answer()

# =====================================================
# Снепы
# =====================================================

@router.callback_query(F.data == "snaps")
async def snaps(callback: CallbackQuery):

    await callback.message.edit_text(
        SNAPS_TEXT,
        reply_markup=snaps_keyboard
    )

    await callback.answer()


# =====================================================
# Требования к портретам
# =====================================================

@router.callback_query(F.data == "portraits")
async def portraits(callback: CallbackQuery):

    await callback.message.edit_text(
        PORTRAITS_TEXT,
        reply_markup=portraits_keyboard
    )

    await callback.answer()


# =====================================================
# Видеовизитка
# =====================================================

@router.callback_query(F.data == "video")
async def video(callback: CallbackQuery):

    await callback.message.edit_text(
        VIDEO_TEXT,
        reply_markup=video_keyboard
    )

    await callback.answer()

    # =====================================================
# FAQ
# =====================================================

@router.callback_query(F.data == "faq")
async def faq(callback: CallbackQuery):

    await callback.message.edit_text(
        FAQ_TEXT,
        reply_markup=back_keyboard
    )

    await callback.answer()



# =====================================================
# Примеры снепов
# =====================================================

@router.callback_query(F.data == "snaps_examples")
async def snaps_examples(callback: CallbackQuery):

    media = [
        InputMediaPhoto(
            media=FSInputFile("media/snapswomen.jpg"),
            caption="📸 Примеры правильных снепов"
        ),
        InputMediaPhoto(
            media=FSInputFile("media/snapsmen.jpg")
        ),
    ]

    await callback.message.answer_media_group(media)

    await callback.message.answer(
    "Выберите действие:",
    reply_markup=back_to_snaps_keyboard
)

    await callback.answer()

    # =====================================================
# Примеры портретов
# =====================================================

@router.callback_query(F.data == "portraits_examples")
async def portraits_examples(callback: CallbackQuery):

    media = [
        InputMediaPhoto(
            media=FSInputFile("media/portraitswomen.jpg"),
            caption="🖼 Примеры подходящих портретов"
        ),
        InputMediaPhoto(
            media=FSInputFile("media/portraitsmen.jpg")
        ),
    ]

    await callback.message.answer_media_group(media)

    await callback.message.answer(
        "Выберите действие:",
        reply_markup=back_to_portraits_keyboard
    )

    await callback.answer()


# =====================================================
# Пример видеовизитки
# =====================================================

@router.callback_query(F.data == "video_example")
async def video_example(callback: CallbackQuery):

    await callback.message.answer_video(
        video=FSInputFile("media/videoexample.mp4"),
        caption="🎥 Пример видеовизитки"
    )

    await callback.message.answer(
        "Выберите действие:",
        reply_markup=back_to_video_keyboard
    )

    await callback.answer()


