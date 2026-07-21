import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.application import router as application_router
from handlers.business import router as business_router


bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(application_router)
dp.include_router(business_router)


async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())