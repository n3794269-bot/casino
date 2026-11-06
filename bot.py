import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database import init_db
from handlers import start, deposit, withdraw, admin

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

async def main():
    await init_db()
    dp.include_router(start.router)
    dp.include_router(deposit.router)
    dp.include_router(withdraw.router)
    dp.include_router(admin.router)
    print("[+] bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
