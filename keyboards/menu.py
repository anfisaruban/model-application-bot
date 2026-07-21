from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ======================================================
# Старт
# ======================================================

welcome_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✨ Ознакомиться",
                callback_data="requirements"
            )
        ]
    ]
)

# ======================================================
# Главное меню
# ======================================================

requirements_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📝 Формат заявки",
                callback_data="application_format"
            )
        ],
        [
            InlineKeyboardButton(
                text="📸 Снепы",
                callback_data="snaps"
            )
        ],
        [
            InlineKeyboardButton(
                text="🖼 Портреты",
                callback_data="portraits"
            )
        ],
        [
            InlineKeyboardButton(
                text="🎥 Видеовизитка",
                callback_data="video"
            )
        ],
        [
            InlineKeyboardButton(
                text="❓ FAQ",
                callback_data="faq"
            )
        ]
    ]
)

# ======================================================
# Снепы
# ======================================================

snaps_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📷 Посмотреть примеры",
                callback_data="snaps_examples"
            )
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Назад к разделам",
                callback_data="requirements"
            )
        ]
    ]
)

# ======================================================
# Портреты
# ======================================================

portraits_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🖼 Посмотреть примеры",
                callback_data="portraits_examples"
            )
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Назад к разделам",
                callback_data="requirements"
            )
        ]
    ]
)
# ======================================================
# Видео
# ======================================================

video_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="▶️ Посмотреть пример",
                callback_data="video_example"
            )
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Назад к разделам",
                callback_data="requirements"
            )
        ]
    ]
)

# ======================================================
# Возврат после просмотра снепов
# ======================================================

back_to_snaps_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="⬅️ Вернуться к инструкции",
                callback_data="snaps"
            )
        ]
    ]
)

# ======================================================
# Возврат после просмотра портретов
# ======================================================

back_to_portraits_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="⬅️ Вернуться к инструкции",
                callback_data="portraits"
            )
        ]
    ]
)

# ======================================================
# Возврат после просмотра видео
# ======================================================

back_to_video_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="⬅️ Вернуться к инструкции",
                callback_data="video"
            )
        ]
    ]
)

# ======================================================
# Универсальная кнопка "Назад"
# ======================================================

back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="⬅️ Назад к разделам",
                callback_data="requirements"
            )
        ]
    ]
)

# ======================================================
# Кнопки под шаблоном заявки
# ======================================================

application_format_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ Отправить заявку",
                callback_data="send_application"
            )
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Назад",
                callback_data="requirements"
            )
        ]
    ]
)