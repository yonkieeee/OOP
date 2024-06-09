import asyncio
from aiogram import Bot, Dispatcher
from app.hanlers import router


async def main():
    bot = Bot(token='7182365786:AAFst1OE1upCvI3TjOcLHIH_seioCXHV4_U')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot is off')


